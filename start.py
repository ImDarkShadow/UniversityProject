import os
import shutil
import zipfile
import cv2 as cv
from natsort import natsorted
from ocr import ocr
from printRegional import putText
from translation import translate
from cleanRawText import cleanRaw


def getUserInput(text):
    """
    The getUserInput function prompts the user for input and returns it as a string.
        It is used to prompt the user for their input, which will be stored in a variable called 'userInput'.


    :param text: Display a message to the user
    :return: The user input
    :doc-author: Trelent
    """
    userInput = input(text)
    return userInput


def createFolder(folderPath):
    """
    The createFolder function creates a folder at the specified path if it does not already exist.
    If exist it will delete the contents of the folder.

    :param folderPath: Specify the path to the folder that is being created
    :return: A boolean value
    :doc-author: Trelent
    """
    if os.path.exists(folderPath):
        shutil.rmtree(folderPath)
    os.mkdir(folderPath)


def getFiles(directory='./files/raw'):
    """
    The getFiles function returns a list of all the files in the specified directory.
    The default directory is ./files/raw, but this can be changed by passing an argument.

    :param directory='./files/raw': Tell the function where to look for files
    :return: A list of all the files in the specified directory
    :doc-author: Trelent
    """
    return os.listdir(directory)


os.makedirs('./files/output', exist_ok=True)

directory = './files/raw'
file_list = getFiles(directory)
createFolder('./files/temp')
createFolder('./files/steps')


def print_comic_list(comic_list):
    """
    The print_comic_list function prints out a list of comics in the comic_list.
    It takes one argument, comic_list, which is a list of strings.

    :param comic_list: Pass a list of comic files to the print_comic_list function
    :return: A list of comic files
    :doc-author: Trelent
    """
    for i, file in enumerate(comic_list):
        print(f'{i + 1}. {file}')


print_comic_list(file_list)

comicNumber = getUserInput("Enter the comic number: ")
comicName = file_list[int(comicNumber) - 1]


def extract_comic(comic_name):
    """
    The extract_comic function extracts the comic from its zip file and places it in a temporary folder.
    The function takes one argument, which is the name of the comic.

    :param comic_name: Tell the function which comic to extract
    :doc-author: Trelent
    """
    with zipfile.ZipFile(f'./files/raw/{comic_name}', 'r') as zip_ref:
        zip_ref.extractall(f'./files/temp/{comic_name}')


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


def read_images(images):
    """
    The read_images function reads in the images from the list of image paths using cv.imread
     and returns a list of images.

    :return: A list of images
    :doc-author: Trelent
    """
    img = []
    for i in images:
        print(i)
        img.append(cv.imread(i))
    return img


def get_crop_coordinates(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (7, 7), 0)
    thresh = cv.threshold(
        blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

    crop_array = [0]
    i = 600
    while i < row:
        flag = 0
        for j in range(1, col, 1):
            if thresh[i][j] == thresh[i][0]:
                continue
            else:
                flag = 1
                break
        if flag == 0:
            crop_array.append(i)
            i += 600
        else:
            i += 3
    crop_array.append(row)
    return crop_array


img_array = read_images(images)
image = cv.vconcat(img_array)
row = image.shape[0]
col = image.shape[1]

crop_array = get_crop_coordinates(image)
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
    print(type(text))
    if len(text) != 0:
        texts.append(text)
    cords.append(cord)
print("here will be actual output")
print(texts)
trans = translate(*texts)
print("here will be english translation")
font = cv.FONT_HERSHEY_SIMPLEX
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
