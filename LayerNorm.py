import torch
import torch.nn as nn


class CustomLayerNorm(nn.Module):
    def __init__(self, normalized_shape, eps=1e-5):
        super().__init__()

        # normalized_shape is usually the embedding dimension (e.g., 768)
        if isinstance(normalized_shape, int):
            self.normalized_shape = (normalized_shape,)
        else:
            self.normalized_shape = tuple(normalized_shape)

        self.eps = eps

        # Learnable Parameters (Gamma and Beta)
        # Gamma (scale) initializes to 1, Beta (shift) initializes to 0
        self.gamma = nn.Parameter(torch.ones(self.normalized_shape))
        self.beta = nn.Parameter(torch.zeros(self.normalized_shape))

    def forward(self, x):
        # x shape: [batch_size, seq_len, embedding_dim]

        # 1. Determine dimensions to reduce
        # LayerNorm reduces over the last N dimensions given by normalized_shape
        # Typically just the last dimension (-1)
        dims_to_reduce = list(range(len(x.shape) - len(self.normalized_shape), len(x.shape)))

        # 2. Calculate Mean and Variance
        # keepdim=True is critical so shapes match for subtraction (Broadcasting)
        # mean shape becomes [batch, seq_len, 1]
        mean = x.mean(dim=dims_to_reduce, keepdim=True)

        # Layer Norm uses biased variance (division by N), not N-1
        var = x.var(dim=dims_to_reduce, keepdim=True, unbiased=False)

        # 3. Normalize
        # (x - mean) / sqrt(var + eps)
        x_normalized = (x - mean) / torch.sqrt(var + self.eps)

        # 4. Scale and Shift (Affine transformation)
        # y = gamma * x_normalized + beta
        output = self.gamma * x_normalized + self.beta

        return output


# --- Verification ---

# Create random input: Batch=2, SeqLen=3, Embed=4
torch.manual_seed(42)
input_data = torch.randn(2, 3, 4)

# Initialize both layers
custom_ln = CustomLayerNorm(4)
official_ln = nn.LayerNorm(4)

# Ensure weights are identical for comparison
with torch.no_grad():
    official_ln.weight.copy_(custom_ln.gamma)
    official_ln.bias.copy_(custom_ln.beta)

# Forward pass
custom_out = custom_ln(input_data)
official_out = official_ln(input_data)

# Check for differences
diff = (custom_out - official_out).abs().max().item()
print(f"Max difference: {diff:.9e}")

# --- Proof of Independence ---
# Modify one token in the batch and show it doesn't affect neighbors
print("\nChecking independence...")
input_mutated = input_data.clone()
input_mutated[0, 1, :] = 1000.0  # Change neighboring token drastically

# Re-run forward pass
custom_out_mutated = custom_ln(input_mutated)

# Check if the first token [0,0] changed
# It should be EXACTLY the same as before
change = (custom_out[0, 0] - custom_out_mutated[0, 0]).abs().sum().item()
print(f"Did neighbor mutation affect current token? {'YES' if change > 1e-6 else 'NO'}")