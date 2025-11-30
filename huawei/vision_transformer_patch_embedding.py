img_size, patch_size, channel, embedding_dim = list(map(int, input().split()))

num_patches = int((img_size / patch_size) ** 2)

print(num_patches + 1, embedding_dim)