def op_code_program(x,y):
    ## store file into variable
    int_code = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,6,23,27,1,6,27,31,2,31,9,35,1,35,6,39,1,10,39,43,2,9,43,47,1,5,47,51,2,51,6,55,1,5,55,59,2,13,59,63,1,63,5,67,2,67,13,71,1,71,9,75,1,75,6,79,2,79,6,83,1,83,5,87,2,87,9,91,2,9,91,95,1,5,95,99,2,99,13,103,1,103,5,107,1,2,107,111,1,111,5,0,99,2,14,0,0"
    int_code = [int(x) for x in int_code.split(',')]
    int_code[1] = x
    int_code[2] = y
    start_position = 0

    for code in range(0, len(int_code),4) :
        code = int_code[start_position]
        if code == 1:
            factor_one_position = int_code[start_position + 1]
            factor_two_position = int_code[start_position + 2]
            factor_three_position = int_code[start_position + 3]
            int_code[factor_three_position] = int_code[factor_one_position] + int_code[factor_two_position]
            start_position += 4
        if code == 2:
            factor_one_position = int_code[start_position + 1]
            factor_two_position = int_code[start_position + 2]
            factor_three_position = int_code[start_position + 3]
            int_code[factor_three_position] = int_code[factor_one_position] * int_code[factor_two_position]
            start_position += 4
        if code == 99:
            return int_code
            break
        else:
            continue
        
    return int_code
        
for x in range(100):
    for y in range (100):
        final_int_code = op_code_program(x,y)
        if final_int_code[0] == 19690720:
            noun = final_int_code[1]
            verb = final_int_code[2]
            product = 100 * noun + verb
            print(product)
            
            


