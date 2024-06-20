import os
import cv2

# config
input_ext = '.png'
output_ext = '.jpg'
input_path = os.getcwd() + '/input/'
output_path = os.getcwd() + '/output/'

origin_files = os.listdir(input_path)

file_list_jpg = [file for file in origin_files if file.endswith(input_ext)]

print(origin_files)
print(file_list_jpg)

for image in file_list_jpg:
    input_image = cv2.imread(input_path + image)

    output_image = output_path + image.rstrip(input_ext) + output_ext
    try:
        cv2.imwrite(output_image, input_image)
    except cv2.error:
        #print(input_image)
        continue