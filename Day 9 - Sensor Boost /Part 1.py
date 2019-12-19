#int_code_list = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
int_code_list = '1102,34915192,34915192,7,4,7,99,0'
#int_code_list = '104,1125899906842624,99'
int_code_list = [int(x) for x in int_code_list.split(',')]


def test_diagnostic_program(int_code, input_value):
    test_results = 0
    int_code = int_code
    relative_base = 0
    position = 0

    log = {'int code': int_code, 'test results': test_results}
    while position in range(len(int_code)):

        mode_opcode = str(int_code[position]).zfill(5)  # add zeros to full opcode
        mode_opcode_list = list(mode_opcode)  # make list
        # convert list strings to ints
        opcode_modes = [int(x) for x in mode_opcode_list]
        opcode = str(opcode_modes[3]) + str(opcode_modes[4])
        opcode = int(opcode)
        params_mode = opcode_modes[:3]
        param_pairs = list(enumerate(params_mode[::-1], start=1))
        param_values = []

        for param_position, mode in param_pairs:
            if opcode in (3, 9, 99):
                break
            if opcode == 4 and param_position == 1:
                if mode == 0:
                    param_value = int_code[int_code[position + param_position]]
                    param_values.append(param_value)
                    break
                if mode == 1 and param_position == 1:
                    param_value = int_code[position + param_position]
                    param_values.append(param_value)
                    break
            if param_position == 3:
                param_value = int_code[position + param_position]
                param_values.append(param_value)
            elif mode == 0:  # position mode
                param_value = int_code[int_code[position + param_position]]
                param_values.append(param_value)
            elif mode == 1:  # immediate mode
                param_value = int_code[position + param_position]
                param_values.append(param_value)
            elif mode == 2:  # relative mode
                if relative_base == 0:
                    param_value = int_code[int_code[position + param_position]]
                    param_values.append(param_value)
                elif relative_base != 0:
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
            int_code[int_code[position + 1]] = input_value
            position += 2

        elif opcode == 4:
            test_results = param_values[0] 
            position += 2

        elif opcode == 5:
            if param_values[0] != 0:
                position = param_values[1]
            else:
                position += 3

        elif opcode == 6:
            if param_values[0] == 0:
                position = param_values[1]
            else:
                position += 3

        elif opcode == 7:
            position += 4
            if param_values[0] < param_values[1]:
                int_code[param_values[2]] = 1
            else:
                int_code[param_values[2]] = 0

        elif opcode == 8:
            position += 4
            if param_values[0] == param_values[1]:
                int_code[param_values[2]] = 1
            else:
                int_code[param_values[2]] = 0

        elif opcode == 9:
            position += 2
            relative_base = relative_base + int_code[position + 1]
        elif opcode == 99:
            log['halted'] = True
            break

        else:
            continue

    log['int code'] = int_code
    log['test results'] = test_results
    return log


output = test_diagnostic_program(int_code_list, 0)
print(output['test results'])
