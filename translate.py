from googletrans import Translator

translator = Translator()
text = [['', '불쌍해서어떡해: 서른도되기전에  으 요절을 ……'], ['네?', '아니요.', '최팀장님 성격상 바로인도하라고하실 텐데…'],
        ["은         개 에엠..?  | 왜요? '", ''], ['. 왜그렇게 생각하세요?']]


def translate(text):
    result = ''
    # iterate over the inner lists and concatenate each string
    for inner_list in text:
        for string in inner_list:
            result += string
            result += '`'
    # split the concatenated string into a list of strings

    result = " ".join(result.split())
    print(result)
    hj = result.split('`')
    print(hj)
    # translate the list of strings
    translated = translator.translate(result)
    print(translated.text)
    hj = translated.text.split('`')
    print(hj)


translate(text)
