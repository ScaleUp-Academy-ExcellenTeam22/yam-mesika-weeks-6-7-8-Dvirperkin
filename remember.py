from PIL import Image


def image_decoder(image_path):
    """
    :param image_path: The path to the requested image.
    :return: The encrypted message in the image as a string.
    """
    with Image.open(image_path) as img:
        img = Image.open(image_path)
        img_data = list(img.getdata())
        rows = img.size[1]
        cols = img.size[0]
        return "".join([chr(row) for col in range(cols) for row in range(rows) if img_data[row * cols + col] == 1])


if __name__ == '__main__':
    print(image_decoder("code.png"))
