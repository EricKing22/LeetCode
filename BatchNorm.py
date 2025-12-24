import torch
import torch.nn as nn

class CustomBatchNorm1d(nn.Module):
    def __init__(self, num_features, eps=1e-5, momentum=0.1):
        super().__init__()
        self.num_features = num_features
        self.eps = eps
        self.momentum = momentum

        # 1. Learnable Parameters (Gamma and Beta)
        # Gamma (scale) initialized to 1, Beta (shift) initialized to 0
        self.gamma = nn.Parameter(torch.ones(num_features))
        self.beta = nn.Parameter(torch.zeros(num_features))

        # 2. Running Statistics (Non-learnable buffers)
        # These track the global mean/var for inference time
        # We use register_buffer so they are saved with the model state_dict
        # but are not updated by the optimizer.
        self.register_buffer('running_mean', torch.zeros(num_features))
        self.register_buffer('running_var', torch.ones(num_features))

    def forward(self, x):
        # x shape: [batch_size, num_features]

        if self.training:
            # --- TRAINING MODE ---

            # Calculate mean and variance along the batch dimension (dim=0)
            batch_mean = x.mean(dim=0)

            # Note: Standard BN uses biased variance (1/N) for normalization
            batch_var = x.var(dim=0, unbiased=False)

            # Update running statistics (using exponential moving average)
            # Note: PyTorch uses unbiased variance (1/(N-1)) for tracking running stats
            n = x.numel() / x.size(1)
            batch_var_unbiased = x.var(dim=0, unbiased=True)

            with torch.no_grad():
                self.running_mean = (1 - self.momentum) * self.running_mean + self.momentum * batch_mean
                self.running_var = (1 - self.momentum) * self.running_var + self.momentum * batch_var_unbiased

            # Use current batch stats for normalization
            mean = batch_mean
            var = batch_var

        else:
            # --- INFERENCE/EVAL MODE ---
            # Use the tracked running stats
            mean = self.running_mean
            var = self.running_var

        # 3. Normalization
        # (x - mean) / sqrt(var + eps)
        x_normalized = (x - mean) / torch.sqrt(var + self.eps)

        # 4. Scale and Shift (Affine transformation)
        # y = gamma * x_norm + beta
        output = self.gamma * x_normalized + self.beta

        return output


# --- Verification ---

# Create a random input
torch.manual_seed(42)
input_data = torch.randn(20, 10)  # Batch size 20, 10 features

# Instantiate our custom layer and PyTorch's official layer
custom_bn = CustomBatchNorm1d(num_features=10)
official_bn = nn.BatchNorm1d(num_features=10)

# Initialize them with the same weights for fair comparison
official_bn.weight.data = custom_bn.gamma.data.clone()
official_bn.bias.data = custom_bn.beta.data.clone()

# Forward pass (Training Mode)
custom_out = custom_bn(input_data)
official_out = official_bn(input_data)

# Check differences
diff = (custom_out - official_out).abs().max().item()
print(f"Max difference between Custom and Official implementation: {diff:.9f}")