import shutil
import os
import zipfile
import cv2 as cv


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


def extract_comic(comic_name):
    """
    The extract_comic function extracts the comic from its zip file and places it in a temporary folder.
    The function takes one argument, which is the name of the comic.

    :param comic_name: Tell the function which comic to extract
    :doc-author: Trelent
    """
    with zipfile.ZipFile(f'./files/raw/{comic_name}', 'r') as zip_ref:
        zip_ref.extractall(f'./files/temp/{comic_name}')


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


def get_crop_coordinates(image, row, col):
    """
    The get_crop_coordinates function takes in an image and returns a list of coordinates that indicate the start
    and end of each crop. The function first converts the image to grayscale, then blurs it using a Gaussian blur,
    then thresholds it using Otsu's method. It then iterates through every row in the thresholded image until it finds
    a row where all pixels are black (indicating that this is a blank space). Once such a row is found, we know that this
    is the top boundary for our crop. We increment i by 600 pixels and continue searching for rows with no black pixels until


    :param image: Pass the image to be cropped
    :return: An array of the coordinates where each row is cropped
    :doc-author: Trelent
    """
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
