import torch
from img_tensor import pic_to_tensors
from PIL import Image
import os
import numpy as np
from torchvision.datasets import ImageFolder
from torch.nn.functional import conv2d
from torchvision.utils import save_image
from train import Net

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


def gen_line(img, width=50):
    chars = open('files/chars.txt').read()[:-1]

    # return 1 - sobelize(Image.open(img))
    img_t = pic_to_tensors(1 - sobelize(Image.open(img)), ascii_w=width, tw=30)
    img_t = torch.flatten(img_t, end_dim=1)

    model = torch.load('files/model.pth')
    model = Net()
    model.load_state_dict(torch.load('files/model.pth'))
    model.eval()

    # return model(img_t).argmax(axis=1)
    counter = width
    art = ''
    for ch in model(img_t).argmax(axis=1):
        if counter <= 0:
            art += '\n'
            counter = width
        art += chars[ch]
        counter -= 1
    return art


# with open('test.txt', 'w') as f:
#     f.write(gen_line('files/test2.jpg'))
# save_image(gen_line('files/test_line.jpg'), 'test.jpg')
