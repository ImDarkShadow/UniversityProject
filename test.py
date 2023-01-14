import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time

## Make canvas and set the color
img = np.zeros((200, 400, 3), np.uint8)
b, g, r, a = 0, 255, 0, 0

# Use simsum.ttc to write Chinese.
fontpath = "./Atma-Regular.ttf"
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((50, 80), "যেহেতু মানব", font=font, fill=(b, g, r, a))
img = np.array(img_pil)

# cv2.imwrite("res.png", img)
from googletrans import Translator

translator = Translator()
text = "SIENNA?{0}YOU'LL FIND...{0}YOU MISS HER TOO, RIGHT?{0}OF COURSE I...{0}HUH? YEAH...{0}SIENNA’S IS A REAL MOTHERFUCKER, ISN’T SHE?{0}THEN THAT'S  EVEN MORE REASON TO FIND HER.{0}SHE ABANDONED HER FAMILIAR FOR OVER 200 YEARS.{0}DON'T INSULT SIENNA.{0}DO YOU KNOW HOW MUCH SHE INSULTED ME 300 YEARS AGO?{0}I GET SPECIAL PERMISSION.{0}IN FRONT OF THE WITCH CRAFT?{0}CAN YOU SWEAR THAT YOU TRULY ARE THE REINCARNATION OF THE FOOLISH HAMEL{0}.. EUGENE.{0}"
translated = translator.translate(text, dest='bn')
print(translated.text)
# save translated to trs.txt text file

# generate a random number


