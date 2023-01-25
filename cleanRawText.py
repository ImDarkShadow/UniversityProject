import cv2 as cv
import numpy as np
import dominantColor


def cleanRaw(image, cords, compexbg=False):
    color = (255, 255, 255)
    for i in range(len(cords)):
        if len(cords) == 0:
            return image
        x, y, w, h = cords[i]
        if compexbg:
            color = dominantColor(image[y:y + h, x:x + w])
        else:
            color = (255, 255, 255)
        cv.rectangle(image, (x, y), (x + w, y + h), color, -1)
    return image
