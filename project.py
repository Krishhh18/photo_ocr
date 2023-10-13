import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('1.jpg')
imgg = cv2.imread('2.jpg')
imggg = cv2.imread('3.jpg')

img = cv2.resize(img,None,fx=2,fy=2)
imgg = cv2.cvtColor(imgg,cv2.COLOR_BGR2RGB)
print('Result for 1st image')
print(pytesseract.image_to_string(img))
print('Result for 2nd image')
print(pytesseract.image_to_string(imgg,lang = "eng" , config="--psm 6"))
print('Result for 3rd image')
print(pytesseract.image_to_string(imggg))

cv2.imshow('Result',imgg)
cv2.imshow('Result1',img)
cv2.imshow('Result3',imggg)
cv2.waitKey(0)
