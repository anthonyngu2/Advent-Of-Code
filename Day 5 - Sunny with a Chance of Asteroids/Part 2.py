int_code_list = '3,225,1,225,6,6,1100,1,238,225,104,0,2,136,183,224,101,-5304,224,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1101,72,47,225,1101,59,55,225,1101,46,75,225,1101,49,15,224,101,-64,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,102,9,210,224,1001,224,-270,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,101,14,35,224,101,-86,224,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1102,40,74,224,1001,224,-2960,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1101,10,78,225,1001,39,90,224,1001,224,-149,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1002,217,50,224,1001,224,-1650,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1102,68,8,225,1,43,214,224,1001,224,-126,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1102,88,30,225,1102,18,80,225,1102,33,28,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,677,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1107,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,108,226,226,224,102,2,223,223,1005,224,359,1001,223,1,223,1108,677,226,224,102,2,223,223,1006,224,374,101,1,223,223,108,677,226,224,102,2,223,223,1006,224,389,1001,223,1,223,107,226,226,224,102,2,223,223,1005,224,404,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,419,101,1,223,223,1107,677,677,224,102,2,223,223,1006,224,434,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,449,101,1,223,223,7,677,677,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,494,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,509,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,524,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,539,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,554,101,1,223,223,107,226,677,224,1002,223,2,223,1005,224,569,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,584,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,599,101,1,223,223,1008,677,677,224,102,2,223,223,1005,224,614,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226'
#int_code_list = '3,9,8,9,10,9,4,9,99,-1,8'
#int_code_list = '3,9,7,9,10,9,4,9,99,-1,8'
#int_code_list = '3,3,1108,-1,8,3,4,3,99'
#int_code_list = '3,3,1107,-1,8,3,4,3,99'
#int_code_list = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
int_code_list = [int(x) for x in int_code_list.split(',')]

def test_diagnostic_program(int_code, system_id):

    position = 0
    test_results = []
    if system_id == '1':
        while position in range(len(int_code)) :
            print(int_code[:position+4])

            mode_opcode = str(int_code[position]).zfill(5) #add zeros to full opcode
            mode_opcode_list = list(mode_opcode) #make list
            opcode_modes = [int(x) for x in mode_opcode_list] #convert list strings to ints
            opcode = str(opcode_modes[3]) + str(opcode_modes[4])
            opcode = int(opcode)
            params_mode = opcode_modes[:3]
            param_pairs = list(enumerate(params_mode[::-1], start=1))

            param_values = []
            for param_position,mode in param_pairs:
                if opcode in (3,4,99):
                    break
                elif opcode in (5,6):
                    if param_position < 3:
                        param_value = int_code[position + param_position]
                        param_values.append(param_value)
                    else:
                        break
                elif opcode in (7,8):
                    param_value = int_code[position + param_position]
                    param_values.append(param_value)
                elif param_position == 3:
                    param_value = int_code[position + param_position]
                    param_values.append(param_value)
                elif mode == 0:
                    param_value = int_code[int_code[position + param_position]]
                    param_values.append(param_value)
                elif mode == 1:
                    param_value = int_code[position + param_position]
                    param_values.append(param_value)

            print('position: ' + str(position) + ' || opcode: ' + str(opcode))
            print(param_pairs)
            print(param_values)
            if opcode == 1:
                int_code[param_values[2]] = param_values[0] + param_values[1]
                test = int_code[param_values[2]]
                test_results.append(0)
                position += 4
            elif opcode == 2:
                int_code[param_values[2]] = param_values[0] * param_values[1]
                test = int_code[param_values[2]]
                test_results.append(0)
                position += 4
            elif opcode == 3:
                input_value = 5 
                int_code[int_code[position + 1]] = input_value
                test_results.append(0)
                position += 2
            elif opcode == 4:
                test_results.append(int_code[int_code[position + 1]])
                position += 2
            elif opcode == 5:
                test_results.append(0)
                if param_values[0] != 0:
                    position = param_values[1]
                else:
                    continue
            elif opcode  == 6:
                test_results.append(0)
                if param_values[0] == 0:
                    position = param_values[1]
                else:
                    continue
            elif opcode  == 7:
                test_results.append(0)
                position += 4
                if param_values[0] < param_values[1]:
                    int_code[param_values[2]] == 1
                else:
                    int_code[param_values[2]] == 0
            elif opcode  == 8:
                test_results.append(0)
                position += 4
                if param_values[0] == param_values[1]:
                    int_code[param_values[2]] == 1
                else:
                    int_code[param_values[2]] == 0
            elif opcode == 99:
                break
            else:
                continue
                
    return test_results
        
#system_id = input() -> store as 1 for now
output = test_diagnostic_program(int_code_list,'1')
print(output)

