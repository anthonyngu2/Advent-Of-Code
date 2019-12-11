import math
with open ('/Users/anthonynguyen/Desktop/Advent-Of-Code-2019/Day 8 - Space Image Format/Input.txt') as file:
    Image = file.read()

def create_sub_list(file, width, height):
    layer_size = width * height
    list_of_layers = []
    
    for start in range(0, len(file), layer_size):
        end = start + layer_size
        sub_list = file[start:end]
        list_of_layers.append(sub_list)
        
    return list_of_layers

Width = 25
Height = 6
layered_file = create_sub_list(Image, Width, Height)

def decoder(number_of_layer, layer):
    zero_count = 0
    one_count = 0
    two_count = 0
    log = {}

    for digit in layer:
        if digit == '0':
            zero_count += 1
        if digit == '1':
            one_count += 1
        if digit == '2':
            two_count += 1
        if zero_count + one_count + two_count == len(layer):
            log['layer %s' % number_of_layer] =  number_of_layer 
            log['zero count in layer %s' % number_of_layer] = zero_count
            log['one count layer %s' % number_of_layer] = one_count
            log['two count layer %s' % number_of_layer] = two_count
    
    return log            

full_log = []
for layer_number, layer in enumerate(layered_file):
    layer_log = decoder(layer_number, layer)
    full_log.append(layer_log)

print(full_log)
