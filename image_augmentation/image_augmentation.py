import os
import imageio.v2 as imageio
import imgaug.augmenters as iaa
import numpy as np
import imgaug.parameters as iap
import cv2
import albumentations as A


input_path = os.getcwd() + '/images/'
label_path = os.getcwd() + '/labels/'
output_path = os.getcwd() + '/output/'

def fog_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[fog]' + input_image
        image = imageio.imread(input_image_path)
        fog = iaa.imgcorruptlike.Fog(severity=2)
        fog_image = fog(image=image)
        imageio.imwrite(output_image_path, fog_image)

        filename = os.path.splitext(input_image)[0]
        input_label_path = label_path + filename + '.txt'
        output_label_path = output_path + '[fog]' + filename + '.txt'
        if os.path.exists(input_label_path):
            with open(input_label_path, 'r') as f:
                label_data = f.read()
            with open(output_label_path, 'w') as f:
                f.write(label_data)

def snow_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[snow]' + input_image
        image = imageio.imread(input_image_path)
        snow = iaa.imgcorruptlike.Snow(severity=1)
        snow_image = snow(image=image)
        imageio.imwrite(output_image_path, snow_image)

        filename = os.path.splitext(input_image)[0]
        input_label_path = label_path + filename + '.txt'
        output_label_path = output_path + '[snow]' + filename + '.txt'
        if os.path.exists(input_label_path):
            with open(input_label_path, 'r') as f:
                label_data = f.read()
            with open(output_label_path, 'w') as f:
                f.write(label_data)

def rain_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[rain]' + input_image
        image = imageio.imread(input_image_path)
        rain = iaa.Rain(drop_size=(0.1))
        rain_image = rain(image=image)
        imageio.imwrite(output_image_path, rain_image)

        filename = os.path.splitext(input_image)[0]
        input_label_path = label_path + filename + '.txt'
        output_label_path = output_path + '[rain]' + filename + '.txt'
        if os.path.exists(input_label_path):
            with open(input_label_path, 'r') as f:
                label_data = f.read()
            with open(output_label_path, 'w') as f:
                f.write(label_data)

def clouds_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[clouds]' + input_image
        image = imageio.imread(input_image_path)
        clouds = iaa.Clouds()
        clouds_image = clouds(image=image)
        imageio.imwrite(output_image_path, clouds_image)

        filename = os.path.splitext(input_image)[0]
        input_label_path = label_path + filename + '.txt'
        output_label_path = output_path + '[clouds]' + filename + '.txt'
        if os.path.exists(input_label_path):
            with open(input_label_path, 'r') as f:
                label_data = f.read()
            with open(output_label_path, 'w') as f:
                f.write(label_data)

def spatter_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[spatter]' + input_image
        image = imageio.imread(input_image_path)
        spatter = iaa.imgcorruptlike.Spatter(severity=2)
        spatter_image = spatter(image=image)
        imageio.imwrite(output_image_path, spatter_image)

        filename = os.path.splitext(input_image)[0]
        input_label_path = label_path + filename + '.txt'
        output_label_path = output_path + '[spatter]' + filename + '.txt'
        if os.path.exists(input_label_path):
            with open(input_label_path, 'r') as f:
                label_data = f.read()
            with open(output_label_path, 'w') as f:
                f.write(label_data)

def gaussian_blur_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[gaussian_blur]' + input_image
        image = imageio.imread(input_image_path)
        gaussian_blur = iaa.imgcorruptlike.GaussianBlur(severity=5)
        gaussian_blur_image = gaussian_blur(image=image)
        imageio.imwrite(output_image_path, gaussian_blur_image)

        filename = os.path.splitext(input_image)[0]
        input_label_path = label_path + filename + '.xml'
        output_label_path = output_path + '[gaussian_blur]' + filename + '.xml'
        if os.path.exists(input_label_path):
            with open(input_label_path, 'r') as f:
                label_data = f.read()
            with open(output_label_path, 'w') as f:
                f.write(label_data)

def blend_alpha_simplex_noise_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[blend_alpha_simplex_noise_aug]' + input_image
        image = imageio.imread(input_image_path)
        blend_alpha_simplex_noise = iaa.BlendAlphaSimplexNoise(
                #iaa.EdgeDetect(alpha=0.5),
                iaa.TotalDropout(0.5),
                sigmoid_thresh=iap.Normal(4.0, 1.0))
        blend_alpha_simplex_noise_image = blend_alpha_simplex_noise(image=image)
        imageio.imwrite(output_image_path, blend_alpha_simplex_noise_image)

        filename = os.path.splitext(input_image)[0]
        input_label_path = label_path + filename + '.txt'
        output_label_path = output_path + '[blend_alpha_simplex_noise_aug]' + filename + '.txt'
        if os.path.exists(input_label_path):
            with open(input_label_path, 'r') as f:
                label_data = f.read()
            with open(output_label_path, 'w') as f:
                f.write(label_data)

def gaussian_noise_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[gaussian_noise_aug]' + input_image
        image = imageio.imread(input_image_path)
        gaussian_noise = iaa.AdditiveGaussianNoise(scale=(0, 0.2*255))
        gaussian_noise_image = gaussian_noise(image=image)
        imageio.imwrite(output_image_path, gaussian_noise_image)

def poisson_noise_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[poisson_noise_aug]' + input_image
        image = imageio.imread(input_image_path)
        poisson_noise = iaa.AdditivePoissonNoise(50)
        poisson_noise_image = poisson_noise(image=image)
        imageio.imwrite(output_image_path, poisson_noise_image)

def add_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[add_aug]' + input_image
        image = imageio.imread(input_image_path)
        add = iaa.Add((-40, 40))
        add_image = add(image=image)
        imageio.imwrite(output_image_path, add_image)

def cutout_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[cutout_aug]' + input_image
        image = imageio.imread(input_image_path)
        cutout = iaa.Cutout(nb_iterations=5)
        cutout_image = cutout(image=image)
        imageio.imwrite(output_image_path, cutout_image)

def blend_alpha_elementwise_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[blend_alpha_elementwise_aug]' + input_image
        image = imageio.imread(input_image_path)
        blend_alpha_elementwise = iaa.BlendAlphaElementwise([0.25, 0.75], iaa.MedianBlur(13))
        blend_alpha_elementwise_image = blend_alpha_elementwise(image=image)
        imageio.imwrite(output_image_path, blend_alpha_elementwise_image)

def bilatera_blur_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[bilatera_blur_aug]' + input_image
        image = imageio.imread(input_image_path)
        bilatera_blur = iaa.BilateralBlur(d=(3, 10), sigma_color=(10, 250), sigma_space=(10, 250))
        bilatera_blur_image = bilatera_blur(image=image)
        imageio.imwrite(output_image_path, bilatera_blur_image)

def mean_shift_blur_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[mean_shift_blur_aug]' + input_image
        image = imageio.imread(input_image_path)
        mean_shift_blur = iaa.MeanShiftBlur()
        mean_shift_blur_image = mean_shift_blur(image=image)
        imageio.imwrite(output_image_path, mean_shift_blur_image)

        filename = os.path.splitext(input_image)[0]
        input_label_path = label_path + filename + '.txt'
        output_label_path = output_path + '[mean_shift_blur_aug]' + filename + '.txt'
        if os.path.exists(input_label_path):
            with open(input_label_path, 'r') as f:
                label_data = f.read()
            with open(output_label_path, 'w') as f:
                f.write(label_data)

def add_to_hue_and_saturation_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[add_to_hue_and_saturation_aug]' + input_image
        image = imageio.imread(input_image_path)
        add_to_hue_and_saturation = iaa.AddToHueAndSaturation((-50, 50), per_channel=True)
        add_to_hue_and_saturation_image = add_to_hue_and_saturation(image=image)
        imageio.imwrite(output_image_path, add_to_hue_and_saturation_image)

        filename = os.path.splitext(input_image)[0]
        input_label_path = label_path + filename + '.txt'
        output_label_path = output_path + '[add_to_hue_and_saturation_aug]' + filename + '.txt'
        if os.path.exists(input_label_path):
            with open(input_label_path, 'r') as f:
                label_data = f.read()
            with open(output_label_path, 'w') as f:
                f.write(label_data)

def grayscale_augmentation(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[grayscale_aug]' + input_image
        image = imageio.imread(input_image_path)
        grayscale = iaa.Grayscale(alpha=(0.8, 1.0))
        grayscale_image = grayscale(image=image)
        imageio.imwrite(output_image_path, grayscale_image)

        filename = os.path.splitext(input_image)[0]
        input_label_path = label_path + filename + '.txt'
        output_label_path = output_path + '[grayscale_aug]' + filename + '.txt'
        if os.path.exists(input_label_path):
            with open(input_label_path, 'r') as f:
                label_data = f.read()
            with open(output_label_path, 'w') as f:
                f.write(label_data)


def main():
    image_list = os.listdir(input_path)

    # imgaug
    #fog_augmentation(image_list)
    #snow_augmentation(image_list)
    #rain_augmentation(image_list)
    #clouds_augmentation(image_list)
    #spatter_augmentation(image_list)
    gaussian_blur_augmentation(image_list)
    #blend_alpha_simplex_noise_augmentation(image_list)
    #gaussian_noise_augmentation(image_list)
    #poisson_noise_augmentation(image_list)
    #add_augmentation(image_list)
    #cutout_augmentation(image_list)
    #blend_alpha_elementwise_augmentation(image_list)
    #bilatera_blur_augmentation(image_list)
    #mean_shift_blur_augmentation(image_list)
    #add_to_hue_and_saturation_augmentation(image_list)
    #grayscale_augmentation(image_list)
    
    # albumentations
    #albumentations_spatter(image_list)
    
def albumentations_spatter(image_list):
    for input_image in image_list:
        input_image_path = input_path + input_image
        output_image_path = output_path + '[albumentations_spatter]' + input_image
        image = cv2.imread(input_image_path)
        transform = A.Compose([
            A.augmentations.transforms.Spatter(mean=0.67, std=0.3, gauss_sigma=10, cutout_threshold=0.68, intensity=-10.0, mode='mud', color=(20, 42, 63), p=1.0),
            #A.augmentations.transforms.Spatter(mean=0.67, std=0.3, gauss_sigma=10, cutout_threshold=0.68, intensity=-10.0, mode='mud', color=(43, 62, 82), p=1.0),
        ])
        augmented = transform(image=image)
        augmented_image = augmented['image']
        cv2.imwrite(output_image_path, augmented_image)

        filename = os.path.splitext(input_image)[0]
        input_label_path = label_path + filename + '.txt'
        output_label_path = output_path + '[albumentations_spatter]' + filename + '.txt'
        if os.path.exists(input_label_path):
            with open(input_label_path, 'r') as f:
                label_data = f.read()
            with open(output_label_path, 'w') as f:
                f.write(label_data)

if __name__ == "__main__":
    main()