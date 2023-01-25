# import cv2 as cv
# from paddleocr import PaddleOCR
# import numpy as np
#
# img = cv.imread('test.png')
# image3 = np.copy(img)
# ocr = PaddleOCR(use_angle_cls=True, use_gpu=False)
# # need to run only once to download and load model into memory
# result = ocr.ocr(img, rec=False)
#
# print(result)
# X = np.array(result)
# X = np.asarray(X, dtype='int')
# mask = np.zeros(img.shape[:2], dtype=np.uint8)
# x, y, w, h = cv.boundingRect(X[0][0])
# img[y:y + h, x:x + w] = 0
# mask[y:y + h, x:x + w] = 255
# x, y, w, h = cv.boundingRect(X[0][1])
# img[y:y + h, x:x + w] = 0
# mask[y:y + h, x:x + w] = 255
#
# kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))
# mask = cv.dilate(mask, kernel, iterations=6)
#
# cv.imshow('mask', img)
# cv.imshow('mask2', mask)
# cv.waitKey(0)
# inpainted = cv.inpaint(img, mask, 3, cv.INPAINT_TELEA)
#
# # Save the inpainted image
# cv.imshow('maskuyh2', inpainted)
# cv.waitKey(0)
# cv.imwrite('inpainted.jpg', inpainted)

# import numpy as np
# import cv2 as cv
#
# img = cv.imread('test.png')
# mask = cv.imread('mask.jpg', cv.IMREAD_GRAYSCALE)
# dst = cv.inpaint(img, mask, 3, cv.INPAINT_NS)
# cv.imshow('dst', dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

import cv2
import numpy as np

a = cv2.imread('image.jpg', cv2.IMREAD_UNCHANGED)
a2D = a.reshape(-1, a.shape[-1])
col_range = (256, 256, 256)  # generically : a2D.max(0)+1
a1D = np.ravel_multi_index(a2D.T, col_range)
print(np.unravel_index(np.bincount(a1D).argmax(), col_range))
