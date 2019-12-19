int_code_list = [int(x) for x in int_code_list.split(',')]

def test_diagnostic_program(int_code_original, sequence_value, output_value, final_output_log, log_position):
    second_loop = 0
    final_log = final_output_log
    sequence = sequence_value
    test_results = 0
    halted = False
    if len(final_log) != 5:
        int_code = int_code_original.copy()
        position = 0
        test_results = 0
        second_loop = 0
    else:
        second_loop = 1
        int_code = final_log[log_position-1]['int code']
        position = final_log[log_position-1]['end position']
        test_results = final_log[log_position-1]['test results']

    log_position = log_position - 1
    log = {'sequence': sequence , 'end position': position, 'int code': int_code ,'test results': test_results, 'halted' : halted}
    opcode_three_counter = 0
    while position in range(len(int_code)) :
        
        mode_opcode = str(int_code[position]).zfill(5) #add zeros to full opcode
        mode_opcode_list = list(mode_opcode) #make list
        opcode_modes = [int(x) for x in mode_opcode_list] #convert list strings to ints
        opcode = str(opcode_modes[3]) + str(opcode_modes[4])
        opcode = int(opcode)
        params_mode = opcode_modes[:3]
        param_pairs = list(enumerate(params_mode[::-1], start=1))
        param_values = []
        relative_base = 0

        
        for param_position,mode in param_pairs:
            if param_position == 3:
                param_value = int_code[position + param_position]
                param_values.append(param_value)
            elif mode == 0: #position mode
                param_value = int_code[int_code[position + param_position]]
                param_values.append(param_value)
            elif mode == 1: #immediate mode
                param_value = int_code[position + param_position]
                param_values.append(param_value)
            elif mode == 2: #relative mode
                if relative_base == 0 and param_position == 0:
                    param_value = int_code[int_code[position + param_position]]
                    param_values.append(param_value)
                elif relative_base != 0 and param_position == 0:
                    param_value = int_code[relative_base + int_code[position + param_position]]
                    param_values.append(param_value)
                else:
                    break
        if opcode == 1:
            int_code[param_values[2]] = param_values[0] + param_values[1]
            position += 4
            
        elif opcode == 2:
            int_code[param_values[2]] = param_values[0] * param_values[1]
            position += 4
            
        elif opcode == 3:
            if second_loop == 0:
                input_value_one = sequence_value
                input_value_two = int(output_value)
            else:
                input_value_one = int(output_value)
                
            if opcode_three_counter == 0:
                int_code[int_code[position + 1]] = input_value_one
                opcode_three_counter += 1
            elif opcode_three_counter == 1:
                int_code[int_code[position + 1]] = input_value_two
                opcode_three_counter += 1
            else:
                break
            position += 2
            
        elif opcode == 4:
            test_results = param_value[0]
            position += 2
            break
            
        elif opcode == 5:
            if param_values[0] != 0:
                position = param_values[1]
            else:
                position += 3
                
        elif opcode  == 6:
            if param_values[0] == 0:
                position = param_values[1]
            else:
                position += 3
                
        elif opcode  == 7:
            position += 4
            if param_values[0] < param_values[1]:
                int_code[param_values[2]] = 1
            else:
                int_code[param_values[2]] = 0
                
        elif opcode  == 8:
            position += 4
            if param_values[0] == param_values[1]:
                int_code[param_values[2]] = 1
            else:
                int_code[param_values[2]] = 0
        elif opcode == 9:
            position += 2
            relative_base = relative_base + param_values[0]
        elif opcode == 99:
            log['halted'] = True
            break
        
        else:
            continue
    log['sequence'] = sequence_value
    log['end position'] = position
    log['int code'] = int_code
    log['test results'] = test_results
    return log
        
#system_id = input() -> store as 1 for now
output = test_diagnostic_program(int_code_list,'1')
print(output)

