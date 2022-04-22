import torch
from PIL import Image, ImageDraw, ImageFont
import torchvision
import torchvision.transforms as transforms


def totensor(ch, width=30, texttoframe=1.5):
    # переводим аскии-код в символ если необходимо
    try:
        ch = chr(ch)
    except TypeError:
        pass

    # рисуем картинку
    img = Image.new('RGB', (width, width * 2), (255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', int(width * texttoframe))

    d.text((width / 2, width), ch, fill=(0, 0, 0), font=font, anchor='mm')

    # делаем тензором
    tf = transforms.ToTensor()
    return tf(img)
