import math
with open ('/Users/anthonynguyen/Desktop/Advent-Of-Code-2019/Day 8 - Space Image Format/Input.txt') as file:
    Image = file.read()

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
            layers_by_row[row_number].append(list(layer_row))
            start += width

    return layers_by_row
        
Width = 25
Height = 6
file_layers = create_row_layers(Image, Width, Height)
print(file_layers)
##
##def generate_file_image(row_layers):
##    full_image_pixels
##    for row_number, row in enumerate(row_layers):
##        row.pop()
##        for layer in row:
##            if
##            
generate_file_image(file_layers)
hex_black = '#000000'
hex_white = '#FFFFFF'
hex_transparent = '#ffffff00'

##def layer_counter(number_of_layer, layer):
##    zero_count = 0
##    one_count = 0
##    two_count = 0
##    log = {}
##
##    for digit_position, digit in enumerate(layer):
##        if digit == '0':
##            zero_count += 1
##        if digit == '1':
##            one_count += 1
##        if digit == '2':
##            two_count += 1
##        if digit_position == len(layer) - 1:
##            number_of_layer = number_of_layer + 1
##            log['layer %s' % number_of_layer] =  number_of_layer
##            log['zero count'] = zero_count
##            log['one count'] = one_count
##            log['two count'] = two_count
##    
##    return log            
##
##def generate_log(files):
##    full_log = []
##    for layer_number, layer in enumerate(files):
##        layer_log = layer_counter(layer_number, layer)
##        full_log.append(layer_log)
##    return full_log
##
##complete_logs = generate_log(file_layers)
##del complete_logs[-1]
##print(complete_logs)
##
##min_zero = min(complete_logs, key=lambda x:x['zero count']) #key=lambda allows for anonymous functions inline
##print(min_zero)
