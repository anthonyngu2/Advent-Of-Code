import pprint
from collections import Counter
int_code_list = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'
int_code = [int(x) for x in int_code_list.split(',')]

def test_diagnostic_program(int_code_original, sequence_value, output_value, final_output_log, log_position):
    final_log = final_output_log
    sequence = sequence_value
    test_results = 0
    halted = False
    if len(final_log) != 5:
        int_code = int_code_original
        position = 0
        test_results = 0

    else:
        int_code = final_log[counter-1]['int code']
        position = final_log[counter-1]['end position']
        test_results = final_log[counter-1]['test results']

        
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
            position += 4
            
        elif opcode == 2:
            int_code[param_values[2]] = param_values[0] * param_values[1]
            position += 4
            
        elif opcode == 3:
            input_value_one = sequence_value
            input_value_two = int(output_value)
            if opcode_three_counter == 0:
                int_code[int_code[position + 1]] = input_value_one
                opcode_three_counter += 1
            elif opcode_three_counter == 1:
                int_code[int_code[position + 1]] = output_value
                opcode_three_counter += 1
            else:
                break
            position += 2
            
        elif opcode == 4:
            test_results = int_code[int_code[position + 1]]
            position += 2
            
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
    
##def generate_list():
##    integer_list = []
##    for a in range(5,10):
##        for b in range(5,10):
##            for c in range(5,10):
##                for d in range(5,10):
##                    for e in range(5,10):
##                        sequence = [a,b,c,d,e]
##                        integer_list.append(sequence)
##                        
##    total_sequences_lists = []
##    for possible_sequence in integer_list:
##        count = Counter(possible_sequence)
##        check_empty = [number for number, repeats in count.items() if repeats > 1]
##        if not check_empty:
##            total_sequences_lists.append(possible_sequence)
##    return total_sequences_lists
##
##sequence_list = generate_list()
        
def initiate_thrusters(int_code_original,sequence, sequence_output, counter, final_log):
    if len(final_log) == 5:
        if final_log[0]['halted'] and final_log[1]['halted'] and final_log[2]['halted'] and final_log[3]['halted'] and final_log[4]['halted']:
            return final_log
    if counter == 5:
        counter = 0
    counter += 1
    log = test_diagnostic_program(int_code_original, sequence[counter-1], sequence_output, final_log, counter)
    final_log.append(log)
    print('------------------------------------------------------------------------')
    print(final_log)
    sequence_output = final_log[counter-1]['test results']
    return initiate_thrusters(int_code, sequence, sequence_output, counter, final_log)

def determine_thruster_signal():
    thruster_signals = []
    sequence = [9,8,7,6,5]
    #for sequence in sequence_list:
    max_thruster_signal = initiate_thrusters(int_code, sequence, 0, 0, thruster_signals)
    thruster_signals.append(max_thruster_signal)
    thruster_signals.pop(-1)
    return thruster_signals


print(determine_thruster_signal()[-1]['test results'])
#print(determine_thruster_signal())


