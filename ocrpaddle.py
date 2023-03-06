from paddleocr import PaddleOCR
import cv2 as cv

ocr = PaddleOCR(use_angle_cls=True, lang='korean')  # need to run only once to load model into memory
img_path = '0005.jpg'
result = ocr.ocr(img_path, cls=True)
print(result)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line[1][0])
