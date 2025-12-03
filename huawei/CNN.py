import numpy as np
C, H_in, W_in = list(map(int, input().split()))

img_tensor = []
for _ in range(C * H_in):
    img_tensor.append(list(map(int,input().split())))

img_tensor = np.array(img_tensor).reshape((C,H_in,W_in)).tolist()

C, K_h, K_w = list(map(int, input().split()))

kernal_tensor = []
for _ in range(C * K_h):
    kernal_tensor.append(list(map(int, input().split())))
kernal_tensor = np.array(kernal_tensor).reshape((C, K_h, K_w)).tolist()

stride, padding = list(map(int, input().split()))

# # pad
# def pad(img_tensor):
#     pad_image_tensor = []
#     if padding != 0:
#         for row in img_tensor:
#             row = [0] * padding + row + [0] * padding
#             pad_image_tensor.append(row)
#         pad_image_tensor = [[0]*(2*padding+W_in)] * padding + pad_image_tensor + [[0]*(2*padding+W_in)] * padding
#     else:
#         pad_image_tensor = img_tensor
#     return pad_image_tensor
#
# pad_img_tensor = []
# from pprint import pprint
# for channel in img_tensor:
#     padded_channel = pad(channel)
#     pad_img_tensor.append(padded_channel)

pad_img_tensor = np.pad(img_tensor, ((0,0), (padding,padding),(padding,padding)), mode="constant")

def forward(img, kernal): # 2D, 2D
    H_out = (H_in+2*padding-K_h)//stride+1
    W_out = (W_in+2*padding-K_w)//stride+1

    img = np.array(img)
    kernal = np.array(kernal)

    result = np.zeros((H_out, W_out))
    for i in range(H_out):
        for j in range(W_out):
            h_start = i * stride
            h_end = h_start + K_h
            w_start = j * stride
            w_end = w_start + K_w

            region = img[h_start:h_end, w_start:w_end]
            if region.shape == kernal.shape:
                result[i, j] = np.sum(region * kernal)
    return result

output_channel_results = []
for img_channel, kernal_channel in zip(pad_img_tensor, kernal_tensor):
    results = []

    forward_channel = forward(img_channel, kernal_channel)
    results.append(forward_channel)

    img_channel_output = np.zeros(results[0].shape)
    for result in results:
        img_channel_output += result

    output_channel_results.append(img_channel_output)

final = np.zeros(output_channel_results[0].shape)
for output_channel in output_channel_results:
    final += output_channel


ans = final.tolist()
for row in ans:
    print(" ".join([str(int(item)) for item in row]))


