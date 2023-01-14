import cv2 as cv
import numpy as np
import sys
from natsort import natsorted
from ocr import ocr
from printRegional import putText
from translation import translate
from cleanRawText import cleanRaw
import json

sys.argv = ["join.py", "Archive.zip", "en", "03.jpg"]
# total arguments
# n = len(sys.argv)
sys.argv.pop(0)
comicName = sys.argv[0]
lang = sys.argv[1]
sys.argv.pop(0)
sys.argv.pop(0)
comicFile = sys.argv[0].split(",")

comicFile = natsorted(comicFile)
print(comicFile)
images = [
    "./files/temp/" + comicName + "/" + x for x in comicFile]
print(images)
img = []
for i in images:
    print(i)
    img.append(cv.imread(i))

im_v = cv.vconcat(img)
hh = im_v.shape[0]
ww = im_v.shape[1]
print(hh, ww)
image = im_v
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (7, 7), 0)
thresh = cv.threshold(
    blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

# # Create rectangular structuring element and dilate
# kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
# dilate = cv.dilate(thresh, kernel, iterations=4)

# Find contours and draw rectangle
# cnts = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if len(cnts) == 2 else cnts[1]
# for c in cnts:
#     x, y, w, h = cv.boundingRect(c)
#     cv.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)
# cv.imshow('thresh', thresh)
# #cv.imshow('dilate', dilate)
# cv.imshow('image', crop)
# cv.waitKey()
# print(image.shape[0])
# a forloop to check the image row
# for i in range(image.shape[0]):
#     # a forloop to check the image column
#     print(image[i])
row = image.shape[0]
col = image.shape[1]
jk = [0]
i = 600
while i < row:
    # print(len(thresh[i]))
    flag = 0
    for j in range(1, col, 1):
        if thresh[i][j] == thresh[i][0]:
            continue
        else:
            flag = 1
            break
    if flag == 0:
        jk.append(i)
        i += 600
    else:
        i += 3
jk.append(row)
texts = []
cords = []
croppedImages = []
imageNumber = 0
for i in range(len(jk) - 1):
    crop = image[jk[i]:jk[i + 1], 0:col]
    # cv.imshow('image', crop)
    # cv.waitKey()
    cv.imwrite(f"files/steps/crop{i}.jpg", crop)
    croppedImages.append(crop)
    cord, text = ocr(crop, lang, imageNumber)
    imageNumber += 1
    print(type(text))
    if len(text) != 0:
        texts.append(text)
    cords.append(cord)
print("here will be actual output")
print(texts)
trans = translate(*texts)
print("here will be english translation")
font = cv.FONT_HERSHEY_SIMPLEX
for i in range(len(croppedImages)):
    croppedImages[i] = cleanRaw(croppedImages[i], cords[i])
for i in range(len(croppedImages)):
    print(f'i in printRegional is {i}')
    putText(croppedImages[i], trans[i], cords[i], font, .5, (0, 0, 0), 1, i)
