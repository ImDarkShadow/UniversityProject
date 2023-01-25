import cv2 as cv
from dominantColor import dominantColor


def cleanRaw(image, cords, compexbg=False):
    color = (255, 255, 255)
    colors = []
    for i in range(len(cords)):
        if len(cords) == 0:
            return image
        x, y, w, h = cords[i]
        if compexbg:
            tempimg = image[y:y + h, x:x + w]
            colorz = dominantColor(tempimg)
            color = tuple(map(int, colorz))
            colors.append(colorz)
        else:
            color = (255, 255, 255)
            colors.append(color)
        print(f'color: {color}')
        cv.rectangle(image, (x, y), (x + w, y + h), color, -1)
    return image, colors
