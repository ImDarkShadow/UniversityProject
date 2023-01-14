import json

from googletrans import Translator

translator = Translator()


def translate(*text):
    print(len(text))
    result = ''
    # iterate over the inner lists and concatenate each string
    for inner_list in text:
        for string in inner_list:
            result += string
            result += ' \n '
    print(result)

    #

    translated = translator.translate(result, dest='bn')
    print(translated.text)
    # save result in output.txt
    file1 = open("output.txt", "w")
    file1.write(translated.text)
    print(translated.text)
    translatedText = translated.text.split('\n')
    #translatedText.pop()
    print(translatedText)
    print(len(translatedText))
    translatedTextArray = []

    counter = 0
    for i in range(len(text)):
        tempArray = []
        print(f'length of inner list {i} is {len(text[i])}')
        for j in range(len(text[i])):
            print(f'counter is {counter}')
            print(f'j is {j}')
            # translatedTextArray[i][j] = translatedText[counter]
            tempArray.append(translatedText[counter])
            counter += 1
        translatedTextArray.append(tempArray)
    return translatedTextArray
