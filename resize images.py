from os import listdir
from PIL import Image

def get_files(input_folder):
    file_names = []
    for file in listdir(input_folder):
        if file.endswith('.png'):
            file_names.append(file)
    return file_names

def flip(image, input_folder, output_folder):
    img = Image.open(input_folder + image)
    resized_img = img.resize((100,100), resample=Image.BICUBIC, box=None)
    new_image_name = image
    resized_img.save(output_folder + new_image_name)

input_folder = 'resize/input/'
output_folder = 'resize/output/'
images = get_files('resize/input')

for image in images:
     flip(image, input_folder, output_folder)
