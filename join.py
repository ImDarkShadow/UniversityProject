import cv2 as cv
import numpy as np
import sys
from natsort import natsorted
from ocr import ocr

# total arguments
# n = len(sys.argv)

# sys.argv.pop(0)

jk = [
    '0.rawkuma.com.jpeg',  '1.rawkuma.com.jpeg',  '10.rawkuma.com.jpeg',
    '11.rawkuma.com.jpeg', '12.rawkuma.com.jpeg', '13.rawkuma.com.jpeg',
    '14.rawkuma.com.jpeg', '15.rawkuma.com.jpeg', '16.rawkuma.com.jpeg',
    '17.rawkuma.com.jpeg', '18.rawkuma.com.jpeg', '19.rawkuma.com.jpeg',
    '2.rawkuma.com.jpeg',  '20.rawkuma.com.jpeg', '21.rawkuma.com.jpeg',
    '22.rawkuma.com.jpeg', '23.rawkuma.com.jpeg', '24.rawkuma.com.jpeg',
    '25.rawkuma.com.jpeg', '26.rawkuma.com.jpeg', '27.rawkuma.com.jpeg',
    '28.rawkuma.com.jpeg', '29.rawkuma.com.jpeg', '3.rawkuma.com.jpeg',
    '30.rawkuma.com.jpeg', '31.rawkuma.com.jpeg', '32.rawkuma.com.jpeg',
    '33.rawkuma.com.jpeg', '34.rawkuma.com.jpeg', '35.rawkuma.com.jpeg',
    '36.rawkuma.com.jpeg', '37.rawkuma.com.jpeg', '38.rawkuma.com.jpeg',
    '39.rawkuma.com.jpeg', '4.rawkuma.com.jpeg',  '40.rawkuma.com.jpeg',
    '41.rawkuma.com.jpeg', '42.rawkuma.com.jpeg', '43.rawkuma.com.jpeg',
    '44.rawkuma.com.jpeg', '45.rawkuma.com.jpeg', '46.rawkuma.com.jpeg',
    '47.rawkuma.com.jpeg', '48.rawkuma.com.jpeg', '49.rawkuma.com.jpeg',
    '5.rawkuma.com.jpeg',  '50.rawkuma.com.jpeg', '51.rawkuma.com.jpeg',
    '52.rawkuma.com.jpeg', '53.rawkuma.com.jpeg', '54.rawkuma.com.jpeg',
    '55.rawkuma.com.jpeg', '56.rawkuma.com.jpeg', '57.rawkuma.com.jpeg',
    '58.rawkuma.com.jpeg', '59.rawkuma.com.jpeg', '6.rawkuma.com.jpeg',
    '60.rawkuma.com.jpeg', '61.rawkuma.com.jpeg', '62.rawkuma.com.jpeg',
    '63.rawkuma.com.jpeg', '64.rawkuma.com.jpeg', '65.rawkuma.com.jpeg',
    '66.rawkuma.com.jpeg', '67.rawkuma.com.jpeg', '68.rawkuma.com.jpeg',
    '69.rawkuma.com.jpeg', '7.rawkuma.com.jpeg',  '70.rawkuma.com.jpeg',
    '71.rawkuma.com.jpeg', '72.rawkuma.com.jpeg', '73.rawkuma.com.jpeg',
    '74.rawkuma.com.jpeg', '75.rawkuma.com.jpeg', '76.rawkuma.com.jpeg',
    '77.rawkuma.com.jpeg', '78.rawkuma.com.jpeg', '79.rawkuma.com.jpeg',
    '8.rawkuma.com.jpeg',  '80.rawkuma.com.jpeg', '81.rawkuma.com.jpeg',
    '82.rawkuma.com.jpeg', '83.rawkuma.com.jpeg', '84.rawkuma.com.jpeg',
    '85.rawkuma.com.jpeg', '86.rawkuma.com.jpeg', '87.rawkuma.com.jpeg',
    '88.rawkuma.com.jpeg', '89.rawkuma.com.jpeg', '9.rawkuma.com.jpeg',
    '90.rawkuma.com.jpeg', '91.rawkuma.com.jpeg', '92.rawkuma.com.jpeg',
    '93.rawkuma.com.jpeg', '94.rawkuma.com.jpeg', '95.rawkuma.com.jpeg',
    '96.rawkuma.com.jpeg', '97.rawkuma.com.jpeg', '98.rawkuma.com.jpeg',
    '99.rawkuma.com.jpeg'
]
lang = 'korean'
jk = natsorted(jk)
print(jk)
images = [
    "files/temp/a-returners-magic-should-be-special-chapter-191.zip/" + x for x in jk]
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
texts = []

for i in range(len(jk)-1):
    crop = image[jk[i]:jk[i + 1], 0:col]
    # cv.imshow('image', crop)
    # cv.waitKey()
    texts.append(ocr(crop, lang))
print(texts)
