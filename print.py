import cv2 as cv
import textwrap
import numpy as np


def putText(image, text, cords, font, size, color, thickness,fileNumber):
    print("putText called")
    print(text)
    for i in range(len(text)):
        if text[i] == '':
            continue
        x, y, w, h = cords[i]
        print(x, y, w, h)

        # characterWidth = cv.getTextSize(text[i], font, size, 1)
        (text_width, text_height), baseline = cv.getTextSize(text[i], font, size, thickness)

        cv.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), -1)
        charwidth = text_width / len(text[i])
        charLength = int(w / charwidth)
        print(charLength, w, charwidth)
        # Draw the text on the image
        lines = textwrap.wrap(text[i], charLength)
        for line in lines:
            cv.putText(image, line, (x, y), font, size, color, 1, cv.LINE_AA, False)
            cv.imwrite(f"files/output/{fileNumber}.jpg", image)
    return image
