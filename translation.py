import json

from googletrans import Translator

translator = Translator()
def translate(*text):
    print(text)
    result = ''
    # iterate over the inner lists and concatenate each string
    for inner_list in text:
        for string in inner_list:
            result += string
            result += '#'
    # split the concatenated string into a list of strings
    # trim a string
    yu = json.dumps(text, ensure_ascii=False)
    yu = yu.replace("'", "\'")
    result = result.strip()
    print(yu)
    print(type(yu))
    # result = " ".join(result.split())
    print(text)
    print(yu)
    print(result.split('#'))
    hj = result.split('#')
    print(hj)
    print(len(hj))
    # translate the list of strings
    translated = translator.translate(yu)
    print(translated.text)
    hj = translated.text.split('#')
    print(hj)
    print(len(hj))

    lo = json.loads(translated.text)
    # translatedText = []
    # index = 0
    # for i in range(len(text)):
    #     tempText = []
    #     for j in range(len(text[i])):
    #         tempText.append(hj[index])
    #         index += 1
    #     translatedText.append(tempText)
    print(lo)
    return translated.text

