import pytesseract
from PIL import Image
import app.routes as router


PYTESSERACT_CONFIG = r'--psm 6 -c tessedit_char_whitelist="[]{}:;\'\"/\,.?!@%^№&*()<>`~ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789₽ЙЦУКЕНГШЩЗХЪФЫАПРОЛДЯЧВЖЭСМИТЬБЮЁйцукенгшщзхъфывапролджэячсмитьбюё \|"'


def process_image(image_path:str):
    img = Image.open(router.UPLOAD_FOLDER + image_path)
    data = pytesseract.image_to_data(img, "rus+eng", PYTESSERACT_CONFIG,\
                                 output_type=pytesseract.Output.DICT)
    img_width, img_height = img.size 

    text, top, left = [], [], []

    for i in range(len(data["text"])):
        if data["conf"][i] < 10:
            continue

        x, y = data["left"][i], data["top"][i]

        text.append(data["text"][i])
        # (left, top) - координаты верхней левой точки
        left.append(x / img_width * 100)
        top.append(y / img_height * 100)

    res = {
        "text": text,
        "top": top,
        "left": left,
        "len": range(len(text)),
    }

    return res


def group_to_strings(data: dict):
    pass


if __name__ == "main":
    pass
