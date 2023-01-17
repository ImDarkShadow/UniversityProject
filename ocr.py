import cv2 as cv
import numpy as np
from paddleocr import PaddleOCR
from pytesseract import *


def ocr(image, lang, imnumber):
    image3 = np.copy(image)
    # need to run only once to download and load model into memory
    ocr = PaddleOCR(use_angle_cls=True, lang=lang, use_gpu=False)
    # need to run only once to download and load model into memory
    result = ocr.ocr(image, rec=False)
    X = np.array(result)
    X = np.asarray(X, dtype='int')
    print("value of x")
    print(X)
    external_poly = np.array(X[0], dtype=np.int32)

    blankImage = np.zeros((image.shape[0], image.shape[1], 1), np.uint8)

    cv.fillPoly(blankImage, external_poly, 255)

    cv.imwrite(f"files/steps/blank{imnumber}.jpg", blankImage)
    #    Create rectangular structuring element and dilate
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 5))
    dilate = cv.dilate(blankImage, kernel, iterations=5)
    cv.imwrite(f"files/steps/dilate{imnumber}.jpg", dilate)

    # Find contours and draw rectangle
    if (lang == 'korean'):
        lang = 'kor'
    elif (lang == 'japanese'):
        lang = 'jpn'
    elif (lang == 'en'):
        lang = 'eng'
    elif (lang == 'ch'):
        lang = 'chi_sim'
    ROIs = []
    areas = []
    cnts = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    mask = np.zeros(image.shape, dtype=np.uint8)

    for c in cnts:
        if len(c) < 5:
            continue
        ec = cv.fitEllipse(c)
        cv.ellipse(mask, ec, (255, 255, 255), -1)
        cv.bitwise_and(image, mask)


    for c in cnts:
        x, y, w, h = cv.boundingRect(c)
        cv.rectangle(image3, (x, y), (x + w, y + h), (150, 80, 255), 2)
        crop = image[y:y + h, x:x + w]

        scaling_factor = 2

        # Get the dimensions of the original image
        original_height, original_width = crop.shape[:2]

        # Calculate the dimensions of the scaled image
        scaled_height = int(original_height * scaling_factor)
        scaled_width = int(original_width * scaling_factor)

        # Resize the image
        newim = cv.resize(crop, (scaled_width, scaled_height), interpolation=cv.INTER_LINEAR)
        gray = cv.cvtColor(newim, cv.COLOR_BGR2GRAY)
        # newim = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

        blurred = cv.GaussianBlur(gray, (3, 3), 0)

        # Sharpen the image
        sharpened = cv.addWeighted(blurred, 1.5, blurred, -0.5, 0)

        # gray = cv.cvtColor(crop, cv.COLOR_BGR2GRAY)
        # thresh = cv.threshold(
        #     gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
        # cv.imshow('thresh', crop)
        # cv.waitKey()
        # cv.imshow('dilate', sharpened)
        # cv.waitKey()

        ROIs.append(crop)
        areas.append([x, y, w, h])
        print(x, y, w, h)
    cv.imwrite(f"files/steps/outline{imnumber}.jpg", image3)
    extracted_text = []
    file1 = open("output.txt", "w")
    print(f'Number of ROIs: {len(ROIs)}')

    for i in range(len(ROIs)):
        print(f'Number of ROIs inside OCR: {len(ROIs)}')
        text = pytesseract.image_to_string(ROIs[i], lang=lang)
        lh = text.strip()
        lh = lh.replace("\n", " ")
        if lh != '':
            extracted_text.append(lh)
        else:
            extracted_text.append('are')
    print(areas)
    return areas, extracted_text
