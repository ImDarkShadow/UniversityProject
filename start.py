import os
import zipfile
import cv2 as cv
from natsort import natsorted
from ocr import ocr
from printRegional import putText
from translation import translate
from cleanRawText import cleanRaw
from utils import getUserInput, createFolder, getFiles, print_comic_list, extract_comic, read_images, \
    get_crop_coordinates

# Create the output folder if it doesn't exist
os.makedirs('./files/output', exist_ok=True)

directory = './files/raw'
file_list = getFiles(directory)
createFolder('./files/temp')
createFolder('./files/steps')

print_comic_list(file_list)

comicNumber = getUserInput("Enter the comic number: ")
comicName = file_list[int(comicNumber) - 1]

extract_comic(comicName)

comicLanguage = getUserInput("Enter the comic language: ")
chapterImages = getFiles(f'./files/temp/{comicName}')

createFolder(f'./files/output/{comicName}')
isComplexBG = (getUserInput("Is there complex text background? (y/n): ") == 'y')
lang = comicLanguage

comicFile = chapterImages

comicFile = natsorted(comicFile)
print(comicFile)
images = [
    "./files/temp/" + comicName + "/" + x for x in comicFile]

img_array = read_images(images)
image = cv.vconcat(img_array)
row = image.shape[0]
col = image.shape[1]

crop_array = get_crop_coordinates(image, row, col)
texts = []
cords = []
croppedImages = []
imageNumber = 0
for i in range(len(crop_array) - 1):
    crop = image[crop_array[i]:crop_array[i + 1], 0:col]
    cv.imwrite(f"files/steps/crop{i}.jpg", crop)
    croppedImages.append(crop)
    cord, text = ocr(crop, lang, imageNumber)
    imageNumber += 1
    if len(text) != 0:
        texts.append(text)
    cords.append(cord)
trans = translate(*texts)
colors = []
for i in range(len(croppedImages)):
    croppedImages[i], tempColor = cleanRaw(croppedImages[i], cords[i], isComplexBG)
    colors.append(tempColor)
j = 0
for i in range(len(croppedImages)):
    if len(cords[i]) == 0:
        continue
    putText(croppedImages[i], trans[j], cords[i], i, comicName, colors[i], isComplexBG)
    j += 1
translatedImages = os.listdir(f'./files/output/{comicName}')

with zipfile.ZipFile(f'./files/output/Tanslated- {comicName}', mode='w') as archive:
    for file in translatedImages:
        archive.write(f'./files/output/{comicName}/{file}',
                      arcname=os.path.basename(f'./files/output/{comicName}/{file}'))
