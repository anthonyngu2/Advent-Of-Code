import math
from PIL import Image
import numpy as np

with open ('/Users/anthonynguyen/Desktop/Advent-Of-Code-2019/Day 8 - Space Image Format/Input.txt') as file:
    read_file = file.read()

Width = 25
Height = 6

#splits the whole string into a list of lists, each row and layer grouped together
def create_row_layers(file, width, height):
    layer_size = width * height
    layers_by_row  = [[] for i in range(height)]
    row = []
    start = 0
    end = 0
    
    while end < len(file):
        for row_number in range(height):
            end = start + width
            layer_row = file[start:end]
            layers_by_row[row_number].append(layer_row)
            start += width

    return layers_by_row
        
file_layers = create_row_layers(read_file, Width, Height)
def decoder(row):
    full_row = []
    for position in range(Width):
        for layer_number, layer in enumerate(row):
            if layer[position] == '2': #transparent
                continue
            elif layer[position] == '1': #white
                full_row.append((255,255,255))
                break
            elif layer[position] == '0': #black
                full_row.append((0,0,0))
                break
    return full_row
            
def generate_file_image(row_layers):
    full_image_pixels = []
    for row in row_layers:
        row.pop()
        corrected_row = decoder(row)
        full_image_pixels.append(corrected_row)
        
    return full_image_pixels

image = generate_file_image(file_layers)

array = np.array(image, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save('DecodedImage.png')
