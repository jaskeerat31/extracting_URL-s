#Pillow library for working with images
from PIL import Image

#optical character recognition(OCR) tool for python
import pytesseract

#opencv library
import cv2

#library for regular expression
import re

#for interacting with operating system
import os

#for displaying web pages 
import webbrowser

#to read an image
img=cv2.imread("Testing.png")

#converting image into grayscale
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#get the process id of current process
file="{}.png" .format(os.getpid())

#saves gray images to the specified file
cv2.imwrite(file,gray)

#converting contents of image into string
text=pytesseract.image_to_string(Image.open(file))

#delete the file
os.remove(file)

print(text)


#using regular expression to search all the possible URL's in our text
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[.]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)


print(urls[0])


#opening the extracted URLs in default browser
webbrowser.open(urls[0])
