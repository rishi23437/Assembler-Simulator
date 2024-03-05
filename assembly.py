import re

reg_ENCODE  = {'zero': '00000',   'ra': '00001',     'sp': '00010',     'gp': '00011', 
               'tp': '00100',     't0': '00101',     't1': '00110',     't2': '00111', 
               's0': '01000',     'fp': '01000',     's1': '01001',     'a0': '01010',     'a1': '01011', 
               'a2': '01100',     'a3': '01101',     'a4': '01110',     'a5': '01111', 
               'a6': '10000',     'a7': '10001',     's2': '10010',     's3': '10011', 
               's4': '10100',     's5': '10101',     's6': '10110',     's7': '10111', 
               's8': '11000',     's9': '11001',     's10': '11010',    's11': '11011', 
               't3': '11100',     't4': '11101',     't5': '11110',     't6': '11111'}

instruction_mapping = {"r_type": ["add", "sub", "sll", #we can make each element as set also instead of list->faster search
                                  "slt", "sltu", "xor", 
                                  "srl", "or", "and"], 
                       "i_type": ["lw", "lb", "lh", "ld", 
                                   "addi", "sltiu", 'jalr'], 
                       "s_type": ["sw", "sb", "sh", "sd"], 
                       "b_type": ["beq", "bne", "blt", 
                                   "bge", "bltu", "bgeu"], 
                       "u_type": ["lui", "auipc"], 
                       "j_type": ["jal"]
                       }


with open(r"", 'r') as pointer:
    assembly = pointer.readlines()
    print(assembly)

pc = 0
output_list = []
while (pc<(len(assembly))):
    instruction = assembly[pc]
    if instruction == "":                                      #for Empty lines
        pc += 1
        continue
      
    for index in range(len(instruction)):
        instruction[index] = instruction[index].lower()
    
    instruction_elements = re.split(' |,|(|)', instruction)
    type = instruction_elements[0]

  
    if type in list(instruction_mapping["r_type"]):
        output = r_type(instruction_elements)
        output_list.append(output)
  
    elif type in list(instruction_mapping["i_type"]):
        output = I_TYPE(instruction_elements)
        output_list.append(output)  

    elif type in list(instruction_mapping["s_type"]):
        output = S_TYPE(instruction_elements)
        output_list.append(output)

    elif type in list(instruction_mapping["b_type"]):
        output = B_TYPE(instruction_elements)
        # if (output[0]=='e'):
        #     output_list = []
        #     output_list.append(output)
        #     break
        output_list.append(output)

    elif type in list(instruction_mapping["u_type"]):
        output = u_type(instruction_elements)
        output_list.append(output)

    elif type in list(instruction_mapping["j_type"]):
        output = J_TYPE(instruction_elements)
        output_list.append(output)

    else:
        error = "Operation not valid"
        output_list = []
        output_list.append(error)
        break


  
  




def sext(number, bits):
    """
    This function first converts the number into binary
    and then extends its bits to the required amount
    """
    number = int(number)
    if (number<-(2**(bits-1)) or number>(2**(bits-1))-1):
        return "error: overflow detected"
    if (number<0):
        sign = -1
        number = -number
    else:
        sign = 1
    binary = ""
    while (number>0):
        binary += f"{number%2}"
        number = number//2
    binary = binary[::-1]
    binary = ('0'*(bits-len(binary)))+binary
    if (sign == -1):
        flag=False
        twosComplement = ""
        for i in range(len(binary)-1, -1, -1):
            if (flag):
                if binary[i]=='1':
                    twosComplement+='0'
                else:
                    twosComplement+='1'
                continue
            twosComplement+=binary[i]
            if (binary[i]=='1'):
                flag = True 
        binary = twosComplement[::-1]
    return binary




