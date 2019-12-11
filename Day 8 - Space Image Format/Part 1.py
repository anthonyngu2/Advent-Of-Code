import math
with open ('/Users/anthonynguyen/Desktop/Advent-Of-Code-2019/Day 8 - Space Image Format/Input.txt') as file:
    Image = file.read()

def decoder(file, width, height):
    complete_log = []
    layer_size = width * height
    zero_count = 0
    one_count = 0
    two_count = 0
    log = {}
    list_of_layers = []
    
    for start in range(0, len(file), layer_size):
        end = start + layer_size
        sub_list = file[start:end]
        list_of_layers.append(sub_list)

    for layer_number, layer_set in enumerate(list_of_layers):
        for digit in layer_set:
            if digit == '0':
                zero_count += 1
            if digit == '1':
                one_count += 1
            if digit == '2':
                two_count += 1
            if zero_count + one_count + two_count == layer_size:
                log['layer %s' % layer_number] =  layer_number 
                log['zero count in layer %s' % layer_number] = zero_count
                log['one count layer %s' % layer_number] = one_count
                log['two count layer %s' % layer_number] = two_count
                layer_number += 1
                zero_count = one_count = two_count = 0
                complete_log.append(log)
                break
    
    return complete_log            
    

Width = 25
Height = 6
image_log = decoder(Image, Width, Height)
print(image_log)
