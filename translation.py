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
            result += '{0}'
    # split the concatenated string into a list of strings
    # trim a string
    # yu = json.dumps(text, ensure_ascii=False)
    # yu = yu.replace("'", "\'")
    # result = result.strip()
    # print(yu)
    # print(type(yu))
    # # result = " ".join(result.split())
    # print(text)
    # print(yu)
    # print(result.split('#'))
    # hj = result.split('#')
    # print(hj)
    # print(len(hj))
    # translate the list of strings
    translated = translator.translate(result)
    print(translated.text)
    translatedText = translated.text.split('{0}')
    translatedText.pop()
    print(translatedText)
    print(len(translatedText))
    # hu = translated.text.replace("“", "\"")
    # hu = hu.replace("”", "\"")
    # hu = hu.replace("‘", "\'")
    # hu = hu.replace("’", "\'")
    # hu = hu.replace("'", "\'")
    # hu = hu.replace('"', "\"")
    # print(hu)
    # lo = json.loads(hu)
    # translatedText = []
    # index = 0
    # for i in range(len(text)):
    #     tempText = []
    #     for j in range(len(text[i])):
    #         tempText.append(hj[index])
    #         index += 1
    #     translatedText.append(tempText)
    translatedTextArray = []

    counter =0
    for i in range(len(text)):
        tempArray = []
        print(f'length of inner list {i} is {len(text[i])}')
        for j in range(len(text[i])):
            print(f'counter is {counter}')
            print(f'j is {j}')
            #translatedTextArray[i][j] = translatedText[counter]
            tempArray.append(translatedText[counter])
            counter += 1
        translatedTextArray.append(tempArray)
    return translatedTextArray
