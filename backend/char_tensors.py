import torch
from PIL import Image, ImageDraw, ImageFont
import torchvision
import torchvision.transforms as transforms


def totensor(ch, width=30, textsize=1.5, tratio=2):
    # переводим аскии-код в символ если необходимо
    try:
        ch = chr(ch)
    except TypeError:
        pass

    # рисуем картинку
    img = Image.new('RGB', (width, width * tratio), (255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype('DejaVuSansMono.ttf', int(width * textsize))

    d.text((width / 2, width), ch, fill=(0, 0, 0), font=font, anchor='mm')

    # делаем тензором
    tf = transforms.ToTensor()
    return tf(img)
