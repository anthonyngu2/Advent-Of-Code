import pprint
from collections import Counter
#int_code_list = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
#int_code_list = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
#int_code_list = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'
int_code_list = '3,8,1001,8,10,8,105,1,0,0,21,34,51,64,81,102,183,264,345,426,99999,3,9,102,2,9,9,1001,9,4,9,4,9,99,3,9,101,4,9,9,102,5,9,9,1001,9,2,9,4,9,99,3,9,101,3,9,9,1002,9,5,9,4,9,99,3,9,102,3,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,5,9,101,3,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99'
int_code = [int(x) for x in int_code_list.split(',')]

def test_diagnostic_program(int_code, sequence_value, output_value):
    position = 0
    test_results = []
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
        
        for param_position,mode in param_pairs:
            if opcode in (3,4,99):
                break
            if param_position == 3:
                param_value = int_code[position + param_position]
                param_values.append(param_value)
            elif mode == 0: #position mode
                param_value = int_code[int_code[position + param_position]]
                param_values.append(param_value)
            elif mode == 1: #immediate mode
                param_value = int_code[position + param_position]
                param_values.append(param_value)
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
            input_value_one = sequence_value
            input_value_two = output_value
            if opcode_three_counter == 0:
                int_code[int_code[position + 1]] = input_value_one
                opcode_three_counter += 1
            elif opcode_three_counter == 1:
                int_code[int_code[position + 1]] = output_value
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
                position += 3
        elif opcode  == 6:
            test_results.append(0)
            if param_values[0] == 0:
                position = param_values[1]
            else:
                position += 3
        elif opcode  == 7:
            test_results.append(0)
            position += 4
            if param_values[0] < param_values[1]:
                int_code[param_values[2]] = 1
            else:
                int_code[param_values[2]] = 0
        elif opcode  == 8:
            test_results.append(0)
            position += 4
            if param_values[0] == param_values[1]:
                int_code[param_values[2]] = 1
            else:
                int_code[param_values[2]] = 0
        elif opcode == 99:
            break
        else:
            continue
            
    return test_results[-1]
        
def initiate_thrusters(int_code_list, sequence_output, counter, sequence):
    if counter == 5:
        return sequence_output
    else:
        counter += 1
        sequence_output = test_diagnostic_program(int_code_list, sequence[counter-1], sequence_output)
        return initiate_thrusters(int_code_list, sequence_output, counter, sequence)
    
def generate_list():
    integer_list = []
    for a in range(4:10):
        for b in range(4:10):
            for c in range(4:10):
                for d in range(4:10):
                    for e in range(4:10):
                        sequence = [a,b,c,d,e]
                        integer_list.append(sequence)
                        
    total_sequences_lists = []
    for possible_sequence in integer_list:
        count = Counter(possible_sequence)
        check_empty = [number for number, repeats in count.items() if repeats > 1]
        if not check_empty:
            total_sequences_lists.append(possible_sequence)
    return total_sequences_lists

sequence_list = generate_list()

def determine_thruster_signal():
    thruster_signals = []
    for sequence in sequence_list:
        max_thruster_signal = initiate_thrusters(int_code, 0, 0, sequence)
        thruster_signals.append(max_thruster_signal)
    return thruster_signals

#print(max(determine_thruster_signal()))
for i in range(4:10):
    print i
