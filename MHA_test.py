import torch
import torch.nn as nn

class MHA(nn.Module):
    def __init__(self, hidden_dim, num_heads, p=0):
        super(MHA).__init__()

        assert hidden_dim % num_heads == 0

        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.head_dim = self.hidden_dim // self.num_heads

        self.query = nn.Linear(hidden_dim,hidden_dim)
        self.key = nn.Linear(hidden_dim,hidden_dim)
        self.value = nn.Linear(hidden_dim, hidden_dim)
        self.output = nn.Linear(hidden_dim,hidden_dim)

        self.dropout = nn.Dropout(p)

    def forward(self, hidden_state, attention_mask = None):

        batch_size, seq_len, _ = hidden_state.size()
        query = self.query(hidden_state)
        key = self.key(hidden_state)
        value = self.value(hidden_state)

        query = query.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1,2)
        key = key.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1,2)
        value = value.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1,2)

        attention_weight = torch.matmul(query, key.transpose(-1,-2)) / (self.hidden_dim ** 0.5)


        if attention_mask is not None:
            attention_weight = attention_weight.masked_fill(attention_mask[:,None,None,:]==0, float("-inf"))

        attention_weight = torch.softmax(attention_weight, dim=-1)
        attention_weight = self.dropout(attention_weight)

        context = torch.matmul(attention_weight, value)
        context = context.transpose(1,2).contiguous().view(batch_size, seq_len, self.hidden_dim)

        output = self.output(context)
        return output