'''
DRAWBACKS:
-This code won't run if there are other files other than the images in the folder
-Imagine quality of the pdf produced is low
'''

from PIL import Image
import os

folder = "pdf_images"
files = os.listdir(folder)

img=Image.open(folder + '/' + files[0])
first = img.convert('RGB')
files.pop(0)

images_list=[]
for file in files:
    img=Image.open(folder + '/' + file)
    pdf_img = img.convert('RGB')
    images_list.append(pdf_img)

first.save('output.pdf', save_all = True, append_images = images_list)

