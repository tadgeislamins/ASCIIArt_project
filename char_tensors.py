from PIL import Image, ImageDraw, ImageFont
import torchvision.transforms as T


def char_t(ch, width=30, textsize=1.5, tratio=2):
    """
    Принимает числовой код символа из ASCII таблицы или
    сам символ ASCII. Возвращает тензор заданных размеров,
    полученный из картинки с изображеием этого символа.
    """
    # переводим числовой ASCII-код в символ, если необходимо
    try:
        ch = chr(ch)
    except TypeError:
        pass

    # рисуем картинку с изображением ASCII-символа
    img = Image.new('RGB', (width, width * tratio), (255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype('files/font.ttf', int(width * textsize))

    d.text((width / 2, width), ch, fill=(0, 0, 0), font=font, anchor='mm')

    # преобразуем картинку в тензор
    tf = T.ToTensor()
    return tf(img)
