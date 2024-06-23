import os
from PIL import Image

img_path = os.getcwd() + '/input/'
save_path = os.getcwd() + '/output/'
img_list = os.listdir(img_path)

count = 0

for i in img_list:
    img = Image.open(img_path + i)
    width, height = img.size
    padding_size = 200
    bbox = (padding_size, padding_size, width - padding_size, height - padding_size)
    cropped_img = img.crop(bbox)
    cropped_img.save(save_path + i)
    count = count + 1
    print(str(count) + '/' + str(len(img_list)) + '   ' + str(round((float(count) / float(len(img_list))) * 100, 1))+ '% complete')