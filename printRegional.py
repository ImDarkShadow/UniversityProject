import cv2 as cv
import textwrap
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def putText(image, text, cords, font, size, color, thickness, fileNumber):
    b, g, r, a = 0, 0, 0, 0

    # Use simsum.ttc to write Chinese.
    fontpath = "./Atma-Regular.ttf"
    font = ImageFont.truetype(fontpath, 32)
    # img_pil = Image.fromarray(img)
    # draw = ImageDraw.Draw(img_pil)
    # draw.text((50, 80), "যেহেতু মানব", font=font, fill=(b, g, r, a))
    # img = np.array(img_pil)
    print("putText called")
    print(text)
    for i in range(len(cords)):
        if len(cords) == 0:
            return image
        x, y, w, h = cords[i]
        print(x, y, w, h)

        # # characterWidth = cv.getTextSize(text[i], font, size, 1)
        # (text_width, text_height), baseline = cv.getTextSize(text[i], font, size, thickness)
        # print("text_width", text_width)
        # print(text_width, text_height)
        #
        cv.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), -1)
        # charwidth = text_width / len(text[i])
        # charLength = int(w / charwidth)
        # print(charLength, w, charwidth)
        # # Draw the text on the image
        # lines = textwrap.wrap(text[i], charLength)
        # print(lines)
        # k = y
        # for line in lines:
        #     print(line)
        #     cv.putText(image, line, (x, k), font, size, color, 1, cv.LINE_AA)
        #     cv.imwrite(f"files/output/{fileNumber}.jpg", image)
        #     k += text_height

        img_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(img_pil)
        draw.text((x, y), text[i], font=font, fill=(b, g, r, a))
        image = np.array(img_pil)
        cv.imwrite(f"files/output/{fileNumber}.jpg", image)
    return image
