import torch
from img_tensor import pic_to_tensors
from PIL import Image
import matplotlib.pyplot as plt
import os
import numpy as np
from torchvision.datasets import ImageFolder
from torchvision.transforms import ToTensor, Grayscale, Compose
from torchvision.transforms.functional import invert
from torch.nn.functional import conv2d
from torchvision.utils import save_image


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


def gen_line(img, width=20):
    tf = Compose([Grayscale, invert])
    img_t = tf(sobelize(img))
    return img_t

    model = torch.load('files/model.pth')

    transform = ToTensor()

    test_list = []

    # for file in os.listdir("./MyDrive/neurowood/archive/testset"):
    #     filename = os.fsdecode(file)
    #     img = Image.open("./MyDrive/neurowood/archive/testset/" + filename)
    #     img = transform(img)
    #     test_list.append(img)


    test_tens = torch.stack(test_list)


save_image(gen_line('files/test2.jpg'), 'test.jpg')
