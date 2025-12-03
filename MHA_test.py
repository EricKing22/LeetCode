import torch
import torch.nn as nn


class MHA(nn.Module):
    def __init__(self, hidden_size, num_heads, dropout=0.0):
        super(MHA, self).__init__()

        assert hidden_size % num_heads == 0

        self.hidden_size = hidden_size
        self.num_heads = num_heads
        self.head_dim = self.hidden_size // self.num_heads

        self.query = nn.Linear(hidden_size,hidden_size)
        self.key = nn.Linear(hidden_size,hidden_size)
        self.value = nn.Linear(hidden_size, hidden_size)
        self.output = nn.Linear(hidden_size, hidden_size)

        self.dropout = nn.Dropout(dropout)

    def forward(self, hidden_state, attention_mask=None):

        batch_size, seq_length, _ = hidden_state.size()

        query = self.query(hidden_state)
        key = self.key(hidden_state)
        value = self.value(hidden_state)

        query = query.view(batch_size, seq_length, self.num_heads, self.head_dim).transpose(1,2)
        key = key.view(batch_size, seq_length, self.num_heads, self.head_dim).transpose(1,2)
        value = value.view(batch_size, seq_length, self.num_heads, self.head_dim).transpose(1,2)

        attention_weights = torch.matmul(query,key.transpose(-2,-1)) / (self.hidden_size ** 0.5)
        attention_weights = torch.softmax(attention_weights, dim=-1)
        attention_weights = self.dropout(attention_weights)

        context = torch.matmul(attention_weights, value)
        # 合并
        context = context.transpose(1,2).contiguous().view(batch_size, seq_length, self.hidden_size)

        output = self.output(context)

        return output

if __name__ == "__main__":
    # 示例
    batch_size = 2
    seq_len = 10
    hidden_size = 256
    num_heads = 8

    # 创建一个 MHA 实例
    mha = MHA(hidden_size, num_heads)

    # 创建一个随机的 hidden_state
    hidden_state = torch.randn(batch_size, seq_len, hidden_size)

    # 创建一个 attention mask (可选)
    attention_mask = torch.ones(batch_size, seq_len)
    attention_mask[:, 5:] = 0  # 屏蔽掉每个 batch 中 seq_len 的后 5 个位置

    # 通过 MHA 层
    output = mha(hidden_state, attention_mask)

    # 打印输出形状
    print("输出形状:", output.shape)  # torch.Size([2, 10, 256])







