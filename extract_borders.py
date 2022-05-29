import numpy as np
import matplotlib.pyplot as plt
import torch
from PIL import Image
from torch.nn.functional import conv2d


def sobelize(img):
    # получаем тензор
    # img = pic_to_tensors(img, split=False).unsqueeze_(0)

    img_matrix = np.array(Image.open(img))
    img_tensor = torch.tensor(np.array([img_matrix]), dtype=torch.float)

    img_tensor = img_tensor.permute(0, 3, 1, 2)

    sobel_hor = [[-1, -2, -1],
                 [ 0,  0,  0],
                 [ 1,  2,  1]]

    # одна матрица на каждый канал картинки
    kernel = [[sobel_hor, sobel_hor, sobel_hor]]
    kernel = torch.tensor(kernel, dtype=torch.float)

    # свернём картинку с подготовленным ядром свёртки
    img_conv_hor = conv2d(img_tensor, kernel)
    img_conv_hor = img_conv_hor.permute(0, 2, 3, 1)

    sobel_ver = [[-1, 0, 1],
                 [-2, 0, 2],
                 [-1, 0, 1]]

    # одна матрица на каждый канал картинки
    kernel = [[sobel_ver, sobel_ver, sobel_ver]]
    kernel = torch.tensor(kernel, dtype=torch.float)

    img_conv_ver = conv2d(img_tensor, kernel)
    img_conv_ver = img_conv_ver.permute(0, 2, 3, 1)

    img_conv = torch.sqrt(img_conv_ver**2 + img_conv_hor**2).permute(0, 3, 1, 2)[0]

    return img_conv


img_conv = sobelize('files/test1.jpg')
# plt.figure(figsize=(1.5 * 7, 1.5 * 4))
# plt.imshow(img_conv[0, :, :, 0])
# plt.show()
img_conv
