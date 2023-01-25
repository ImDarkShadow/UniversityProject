import cv2 as cv
import numpy as np


def dominantColor(image):
    # Convert the image to the HSV color space
    img_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Create a histogram of the hue channel
    hist = cv.calcHist([img_hsv], [0], None, [180], [0, 180])

    # Find the index of the bin with the highest value
    most_used_color = np.argmax(hist)

    # Convert the hue value back to BGR
    most_used_color = cv.cvtColor(np.uint8([[[most_used_color, 255, 255]]]), cv.COLOR_HSV2BGR)[0][0]

    # convert numpy array to tuple
    return tuple(most_used_color)

