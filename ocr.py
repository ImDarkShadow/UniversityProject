import cv2
import numpy as np
from paddleocr import PaddleOCR, draw_ocr
import matplotlib.pyplot as plt
from pytesseract import *
import asyncio

# Load image, grayscale, Gaussian blur, Otsu's threshold
# image = cv2.imread('1.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (7, 7), 0)
# thresh = cv2.threshold(
#     blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# # Create rectangular structuring element and dilate
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# dilate = cv2.dilate(thresh, kernel, iterations=4)

# # Find contours and draw rectangle
# cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if len(cnts) == 2 else cnts[1]
# for c in cnts:
#     x, y, w, h = cv2.boundingRect(c)
#     cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)

# cv2.imshow('thresh', thresh)
# cv2.imshow('dilate', dilate)
# cv2.imshow('image', image)
# cv2.waitKey()


def ocr(image, lang):
    # need to run only once to download and load model into memory
    ocr = PaddleOCR(use_angle_cls=True, lang=lang, use_gpu=False)
 # need to run only once to download and load model into memory
    result = ocr.ocr(image, rec=False)
    X = np.array(result)
    X = np.asarray(X, dtype='int')
    external_poly = np.array(X[0], dtype=np.int32)
    blankImage = np.zeros((image.shape[0], image.shape[1], 1), np.uint8)
    blankImage[:] = 255
    cv2.fillPoly(blankImage, external_poly, (0, 0, 0))

    blur = cv2.GaussianBlur(blankImage, (7, 7), 0)
    thresh = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    #    Create rectangular structuring element and dilate
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=4)

    # Find contours and draw rectangle
    if (lang == 'korean'):
        lang = 'kor'
    elif (lang == 'japanese'):
        lang = 'jpn'
    elif (lang == 'ch'):
        lang = 'chi_sim'
    ROIs = []
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        # print(c)
        crop = image[y:y+h, x:x+w]
        ROIs.append(crop)
        print(x, y, w, h)
    extracted_text = []
    for i in range(len(ROIs)):
        text = pytesseract.image_to_string(ROIs[i], lang=lang)
        extracted_text.append(text)
    return [extracted_text, X]
