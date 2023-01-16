import os
import zipfile
import cv2 as cv
from natsort import natsorted
from ocr import ocr
from printRegional import putText
from translation import translate
from cleanRawText import cleanRaw


def getUserInput(text):
    userInput = input(text)
    return userInput


directory = './files/raw'

os.makedirs('./files/output', exist_ok=True)
os.makedirs('./files/steps', exist_ok=True)
file_list = os.listdir(directory)

for i, file in enumerate(file_list):
    print(f'{i + 1}. {file}')

comicNumber = getUserInput("Enter the comic number: ")
comicName = file_list[int(comicNumber) - 1]
print(f'Your chosen comic is : {comicName}')

with zipfile.ZipFile(f'./files/raw/{comicName}', 'r') as zip_ref:
    zip_ref.extractall(f'./files/temp/{comicName}')

comicLanguage = getUserInput("Enter the comic language: ")
chapterImages = os.listdir(f'./files/temp/{comicName}')
print(chapterImages)

os.makedirs(f'./files/output/{comicName}', exist_ok=True)

lang = comicLanguage

comicFile = chapterImages

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
j = 0
for i in range(len(croppedImages)):
    if len(cords[i]) == 0:
        continue
    putText(croppedImages[i], trans[j], cords[i], font, .5, (0, 0, 0), 1, i, comicName)
    j += 1
translatedImages = os.listdir(f'./files/output/{comicName}')

with zipfile.ZipFile(f'./files/output/Tanslated- {comicName}', mode='w') as archive:
    for file in translatedImages:
        archive.write(f'./files/output/{comicName}/{file}',
                      arcname=os.path.basename(f'./files/output/{comicName}/{file}'))
