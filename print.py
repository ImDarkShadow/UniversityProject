import cv2 as cv
import textwrap


def putText(image, text, cords, font, size, color, thickness):
    lines = textwrap.wrap(text, width=20)
    for i, line in enumerate(lines):
        cv.putText(
            image, line, (cords[0], cords[1] + (i * 25)), font, size, color, thickness)
    return image
