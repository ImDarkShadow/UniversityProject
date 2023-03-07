import pytesseract


def main(region_of_interest, areas, lang):
    extracted_text = []
    for i in range(len(region_of_interest)):
        # print(f'Number of ROIs inside OCR: {len(ROIs)}')
        text = pytesseract.image_to_string(region_of_interest[i], lang=lang)
        lh = text.strip()
        lh = lh.replace("\n", " ")
        if lh != '':
            extracted_text.append(lh)
        else:
            extracted_text.append('are')
    # print(areas)
    return areas, extracted_text


if __name__ == '__main__':
    import sys

    main(sys.argv[1:])

