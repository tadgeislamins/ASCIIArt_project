import torch
from img_tensor import pic_to_tensors
from PIL import Image
import os
import numpy as np
from torchvision.datasets import ImageFolder
from torch.nn.functional import conv2d
from torchvision.utils import save_image

def sobelize(img):
    # получаем тензор
    img_matrix = np.array(img)[:, :, 0:3]
    img_tensor = torch.tensor([img_matrix], dtype=torch.float)

    img_tensor = img_tensor.permute(0, 3, 1, 2)

    sobel_hor = [[-1, -2, -1],
                 [ 0,  0,  0],
                 [ 1,  2,  1]]

    # одна матрица на каждый канал картинки
    kernel = [[sobel_hor, sobel_hor, sobel_hor]]
    kernel = torch.tensor(kernel, dtype=torch.float)

    # свернём картинку с подготовленным ядром свёртки
    img_conv_hor = conv2d(img_tensor, kernel)

    sobel_ver = [[-1, 0, 1],
                 [-2, 0, 2],
                 [-1, 0, 1]]

    # одна матрица на каждый канал картинки
    kernel = [[sobel_ver, sobel_ver, sobel_ver]]
    kernel = torch.tensor(kernel, dtype=torch.float)

    img_conv_ver = conv2d(img_tensor, kernel)

    img_conv = torch.sqrt(img_conv_ver**2 + img_conv_hor**2)[0].expand([3, -1, -1])

    return img_conv / (img_conv.max())


def gen_line(img, width=50, tw=20):
    chars = open('files/chars.txt').read()[:-1]

    img_t = pic_to_tensors(1 - sobelize(Image.open(img)), ascii_w=width, tw=tw)
    img_t = torch.flatten(img_t, end_dim=1)
    # return img_t.shape
    # t = torch.zeros(size=[1, 3, 20, 10])

    model = torch.load('files/model.pth')

    counter = width
    art = ''
    for ch in model(img_t).argmax(axis=1):
        if counter <= 0:
            art += '\n'
            counter = width
        art += chars[ch]
        counter -= 1
    return art


with open('test.txt', 'w') as f:
    for i in range(10, 100, 10):
        f.write(str(i))
        f.write(gen_line('files/test2.jpg', tw=i))
        f.write('\n')
# save_image(1 - sobelize(Image.open('test2.jpg')), 'test.jpg')
# gen_line('files/test2.jpg')
