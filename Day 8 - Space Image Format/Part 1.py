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
file_layers = create_sub_list(Image, Width, Height)

def layer_counter(number_of_layer, layer):
    zero_count = 0
    one_count = 0
    two_count = 0
    log = {}

    for digit_position, digit in enumerate(layer):
        if digit == '0':
            zero_count += 1
        if digit == '1':
            one_count += 1
        if digit == '2':
            two_count += 1
        if digit_position == len(layer) - 1:
            number_of_layer = number_of_layer + 1
            log['layer %s' % number_of_layer] =  number_of_layer
            log['zero count'] = zero_count
            log['one count'] = one_count
            log['two count'] = two_count
    
    return log            

def generate_log(files):
    full_log = []
    for layer_number, layer in enumerate(files):
        layer_log = layer_counter(layer_number, layer)
        full_log.append(layer_log)
    return full_log

complete_logs = generate_log(file_layers)
del complete_logs[-1]
print(complete_logs)

min_zero = min(complete_logs, key=lambda x:x['zero count']) #key=lambda allows for anonymous functions inline
print(min_zero)
