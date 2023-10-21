import qrcode

img = qrcode.make("https://www.youtube.com/channel/UCd9S_Fka8-AIhwRaPKJDweQ")
img.save('cyiza.png')

qrcode.make("Cyiza Will be a US Dollar Billionaire in Two years coming")
img.save('rich.png')

import cv2
d = cv2.QRCodeDetector()
val,points, straight_qrcode = d.detectoAndDecode(cv2.imread('rich.png'))
print(val)

