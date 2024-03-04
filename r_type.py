import re

functions_r = {"add": ["0000000", "000"],                #opcode: [funct7, funct3]
             "sub": ["0100000", "000"], 
             "sll": ["0000000", "001"], 
             "slt": ["0000000", "010"], 
             "sltu": ["0000000", "011"], 
             "xor": ["0000000", "100"], 
             "srl": ["0000000", "101"], 
             "or": ["0000000", "110"],
             "and": ["0000000", "111"]
             }

def r_type(instruction):
    items = re.split(' |,', instruction)
   
    operation = items[0]
    reg1, reg2, reg3 = reg_ENCODE[items[1]], reg_ENCODE[items[2]], reg_ENCODE[items[3]]
    
    output = functions_r[operation][0] + reg3 + reg2 + functions_r[operation][1] + reg1 + "0110011"

    return output 