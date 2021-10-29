from PIL import Image
# import os

# GUI
# Show width of pillow.Image
# Input number of pillow.Images left-to-right
# Calculate sprite width
# Show height of sprites
# Input number of pillow.Image top-to-botttom
# Calculate height of the sprites

def main():
    # os.mkdir("assets/icons")
    spritesheet = Image.open('spritesheet/spritesheet.png')
    num_columns = 1
    num_rows = 5
    left_margin = 0
    right_margin = 0
    top_margin = 30
    bottom_margin = 15
    sprite_height = (spritesheet.height - top_margin - bottom_margin) // num_rows
    sprite_width = (spritesheet.width - left_margin - right_margin) // num_columns
    print(spritesheet.height)
    print(spritesheet.width)
    count = 1
    for col in range(num_columns):  # col starts at 0
        for row in range(num_rows): # row starts at 0
            x_pos = col * sprite_width + left_margin
            y_pos = row * sprite_height + top_margin
            icon = spritesheet.crop((x_pos, y_pos, x_pos + sprite_width, y_pos + sprite_height))
            icon.save(f'spritesheet/output/output_{count}.png')
            count += 1

if __name__ == '__main__':
    main()
