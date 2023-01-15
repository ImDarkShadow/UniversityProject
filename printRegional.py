import cv2 as cv
import textwrap
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def putText(image, text, cords, font, size, color, thickness, fileNumber, comicNmae):
    b, g, r, a = 0, 0, 0, 0
    printedImages = []

    # Use simsum.ttc to write Chinese.
    fontpath = "./Atma-Regular.ttf"
    font = ImageFont.truetype(fontpath, 32)
    # img_pil = Image.fromarray(img)
    # draw = ImageDraw.Draw(img_pil)
    # draw.text((50, 80), "যেহেতু মানব", font=font, fill=(b, g, r, a))
    # img = np.array(img_pil)
    print("putText called")
    print(text)
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    for i in range(len(cords)):
        if len(cords) == 0:
            return image
        x, y, w, h = cords[i]
        print(x, y, w, h)
        text_width, text_height = draw.textsize(text[i], font)

        print("text_width", text_width)
        print(text_width, text_height)

        charwidth = text_width / len(text[i])
        charLength = int(w / charwidth)
        print(charLength, w, charwidth)
        # Draw the text on the image
        lines = textwrap.wrap(text[i], charLength)
        print(lines)
        k = y
        for line in lines:
            print(line)
            # cv.putText(image, line, (x, k), font, size, color, 1, cv.LINE_AA)
            draw.text((x, k), line, font=font, fill=(b, g, r, a))
            k += text_height
        image = np.array(img_pil)
    cv.imwrite(f"files/output/{comicNmae}/{fileNumber}.jpg", image)
    return 0
