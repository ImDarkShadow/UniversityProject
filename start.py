import os
import cv2 as cv
from natsort import natsorted

from printRegional import putText
from translation import translate
from utils import getUserInput, createFolder, getFiles, print_comic_list, extract_comic, read_images, \
    get_crop_coordinates, crop_image, get_dominant_colors, zip_files

# Create the output folder if it doesn't exist
os.makedirs('./files/output', exist_ok=True)

file_list = getFiles('./files/raw')
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

croppedImages, texts, cords = crop_image(crop_array, image, col, lang)
trans = translate(*texts)

colors = get_dominant_colors(croppedImages, *cords, isComplexBG=isComplexBG)
j = 0
for i in range(len(croppedImages)):
    if len(cords[i]) == 0:
        continue
    putText(croppedImages[i], trans[j], cords[i], i, comicName, colors[i], isComplexBG)
    j += 1

zip_files(comicName)
