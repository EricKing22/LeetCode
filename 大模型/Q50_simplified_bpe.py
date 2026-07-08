from collections import Counter, defaultdict


def train_bpe(words, num_merges=10):
    # 1. 初始词表把每个单词拆成字符，并追加 </w> 表示词尾。
    vocab = Counter(tuple(word) + ("</w>",) for word in words)
    merges = []
    for _ in range(num_merges):
        # 2. 统计当前词表中相邻 token pair 的出现频次。
        pair_count = defaultdict(int)
        for tokens, freq in vocab.items():
            for pair in zip(tokens, tokens[1:]):
                pair_count[pair] += freq
        if not pair_count:
            break

        # 3. 每轮选择频次最高的一对 token 合并。
        best = max(pair_count, key=pair_count.get)
        merges.append(best)
        new_vocab = Counter()
        for tokens, freq in vocab.items():
            # 4. 在每个词内部从左到右执行本轮 best pair 合并。
            i, merged = 0, []
            while i < len(tokens):
                if i + 1 < len(tokens) and (tokens[i], tokens[i + 1]) == best:
                    merged.append(tokens[i] + tokens[i + 1])
                    i += 2
                else:
                    merged.append(tokens[i])
                    i += 1
            new_vocab[tuple(merged)] += freq
        vocab = new_vocab
    return merges


def bpe_encode(word, merges):
    # 1. 编码时从字符级 token 开始，按训练得到的 merge 顺序依次合并。
    tokens = tuple(word) + ("</w>",)
    for pair in merges:
        i, merged = 0, []
        while i < len(tokens):
            # 2. 如果当前位置匹配当前 merge pair，就合并成一个新 token。
            if i + 1 < len(tokens) and (tokens[i], tokens[i + 1]) == pair:
                merged.append(tokens[i] + tokens[i + 1])
                i += 2
            else:
                merged.append(tokens[i])
                i += 1
        tokens = tuple(merged)

    # 3. 返回最终 BPE token 序列。
    return list(tokens)


if __name__ == "__main__":
    merges = train_bpe(["low", "lower", "newest", "widest"], 5)
    print(merges)
    print(bpe_encode("lower", merges))
