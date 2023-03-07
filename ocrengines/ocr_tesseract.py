import pytesseract


def main(region_of_interest, areas, lang):
    extracted_text = []
    temp = []
    for i in range(len(region_of_interest)):
        # print(f'Number of ROIs inside OCR: {len(ROIs)}')

        text = pytesseract.image_to_string(region_of_interest[i], lang=lang)
        lh = text.strip()
        lh = lh.replace("\n", " ")
        if lh != '':
            extracted_text.append(lh)
        else:
            print(f"area {i} is empty")
            temp.append(i)

    # print(areas)
    for i in range(len(temp)):
        areas.pop(temp[i] - i)
    print(f"areas inside: {areas}")
    return areas, extracted_text


if __name__ == '__main__':
    import sys

    main(sys.argv[1:])
