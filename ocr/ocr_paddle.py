from paddleocr import PaddleOCR

if __name__ == '__main__':
    def main(region_of_interest, areas, lang):
        ocr = PaddleOCR(use_angle_cls=True, lang=lang,
                        show_log=False)  # need to run only once to load model into memory
        extracted_text = []
        for i in range(len(region_of_interest)):
            # print(f'Number of ROIs inside OCR: {len(ROIs)}')
            result = ocr.ocr(region_of_interest[i], cls=True, )
            for idx in range(len(result)):
                res = result[idx]
                for line in res:
                    extracted_text.append(line[1][0])
        # print(areas)
        return areas, extracted_text
