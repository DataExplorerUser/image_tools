from os import listdir
from PIL import Image

def get_music_files(folder):
    file_names = []
    for file in listdir(folder):
        if file.endswith('.png'):
            file_names.append(file)
    return file_names

def flip(image):
    img = Image.open(image)
    flip_img = img.transpose(Image.FLIP_LEFT_RIGHT) # flip anti-clockwise
    # flip_img.show()
    new_image_name = 'left_' + image
    flip_img.save(new_image_name)

images = get_music_files('images/')

# flip(images[0])
for image in images:
     flip(image)
