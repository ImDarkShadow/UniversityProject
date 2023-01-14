# import numpy as np
# from PIL import ImageFont, ImageDraw, Image
# import cv2
# import time
#
# ## Make canvas and set the color
# img = np.zeros((200,400,3),np.uint8)
# b,g,r,a = 0,255,0,0
#
# ## Use cv2.FONT_HERSHEY_XXX to write English.
# text = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime())
# cv2.putText(img,  text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (b,g,r), 1, cv2.LINE_AA)
#
#
# ## Use simsum.ttc to write Chinese.
# fontpath = "./Atma-Regular.ttf" # <== 这里是宋体路径
# font = ImageFont.truetype(fontpath, 32)
# img_pil = Image.fromarray(img)
# draw = ImageDraw.Draw(img_pil)
# draw.text((50, 80),  "যেহেতু মানব", font = font, fill = (b, g, r, a))
# img = np.array(img_pil)
#
# cv2.putText(img,  "--- by Silencer", (200,150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (b,g,r), 1, cv2.LINE_AA)
#
#
# ## Display
# cv2.imshow("res", img);cv2.waitKey();cv2.destroyAllWindows()
# #cv2.imwrite("res.png", img)
from googletrans import Translator

translator = Translator()
text = "SIENNA?{0}YOU'LL FIND...{0}YOU MISS HER TOO, RIGHT?{0}OF COURSE I...{0}HUH? YEAH...{0}SIENNA’S IS A REAL MOTHERFUCKER, ISN’T SHE?{0}THEN THAT'S  EVEN MORE REASON TO FIND HER.{0}SHE ABANDONED HER FAMILIAR FOR OVER 200 YEARS.{0}DON'T INSULT SIENNA.{0}DO YOU KNOW HOW MUCH SHE INSULTED ME 300 YEARS AGO?{0}I GET SPECIAL PERMISSION.{0}IN FRONT OF THE WITCH CRAFT?{0}CAN YOU SWEAR THAT YOU TRULY ARE THE REINCARNATION OF THE FOOLISH HAMEL{0}.. EUGENE.{0}"
translated = translator.translate(text, dest='bn')
print(translated.text)
#save translated to trs.txt text file

#generate a random number


