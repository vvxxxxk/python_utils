import os
from PIL import Image

# config
input_ext = '.png'
output_ext = '.png'
input_path = os.getcwd() + '/input/'
output_path = os.getcwd() + '/output/'

new_width = 16
new_height = 16

# 입력 폴더 내의 모든 이미지 파일 처리
for filename in os.listdir(input_path):
    if filename.endswith(input_ext):
        input_image_path = os.path.join(input_path, filename)
        output_image_path = os.path.join(output_path, os.path.splitext(filename)[0] + output_ext)
        
        with Image.open(input_image_path) as image:
            # 원본 비율 유지하면서 최대 크기로 리사이즈
            width_ratio = new_width / image.width
            height_ratio = new_height / image.height
            resize_ratio = min(width_ratio, height_ratio)
            
            new_size = (int(image.width * resize_ratio), int(image.height * resize_ratio))
            resized_image = image.resize(new_size, Image.Resampling.LANCZOS)
            
            # 리사이즈된 이미지 저장
            resized_image.save(output_image_path)

print("All images resized and saved successfully.")