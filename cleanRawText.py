import cv2 as cv


def cleanRaw(image, cords):
    for i in range(len(cords)):
        if len(cords) == 0:
            return image
        x, y, w, h = cords[i]
        cv.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), -1)
    return image
