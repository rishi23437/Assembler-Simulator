import re

reg_ENCODE  = {'zero': '00000',   'ra': '00001',     'sp': '00010',     'gp': '00011', 
               'tp': '00100',     't0': '00101',     't1': '00110',     't2': '00111', 
               's0': '01000',     'fp': '01000',     's1': '01001',     'a0': '01010',     'a1': '01011', 
               'a2': '01100',     'a3': '01101',     'a4': '01110',     'a5': '01111', 
               'a6': '10000',     'a7': '10001',     's2': '10010',     's3': '10011', 
               's4': '10100',     's5': '10101',     's6': '10110',     's7': '10111', 
               's8': '11000',     's9': '11001',     's10': '11010',    's11': '11011', 
               't3': '11100',     't4': '11101',     't5': '11110',     't6': '11111'}

instruction_mapping = {"r_type": {"add", "sub", "sll", 
                                  "slt", "sltu", "xor", 
                                  "srl", "or", "and"}, 
                       "i_type": {"lw", "lb", "lh", "ld", 
                                   "addi", "sltiu", 'jalr'}, 
                       "s_type": {"sw", "sb", "sh", "sd"}, 
                       "b_type": {"beq", "bne", "blt", 
                                   "bge", "bltu", "bgeu"}, 
                       "u_type": {"lui", "auiPC"}, 
                       "j_type": {"jal"}
                       }

virtual_halt = "00000000000000000000000001100011"


with open(r"", 'r') as pointer:
    assembly = pointer.readlines()
    #print(assembly)

PC = 0
output_list = []

vh_flag = False
vh_num = -1

while ( PC < (len(assembly) ) ):
    instruction = (assembly[PC]).lower()
  
    if (instruction == ""):                                      #for Empty lines
        PC += 1
        continue

    if (vh_flag == True):
        output_list.clear()
        output_list.append( errorGEN("e7", vh_num) )
        break
      
    instruction_elements = re.split(' |,|(|)', instruction)
    type = instruction_elements[0]

  
    if type in instruction_mapping["r_type"]:
        output = R_TYPE(instruction_elements)
        output_list.append(output)
  
    elif type in instruction_mapping["i_type"]:
        output = I_TYPE(instruction_elements)
        output_list.append(output)  

    elif type in instruction_mapping["s_type"]:
        output = S_TYPE(instruction_elements)
        output_list.append(output)

    elif type in instruction_mapping["b_type"]:
        output = B_TYPE(instruction_elements)
        
        if (output == "e1"):
            output_list.clear()
            output_list.append( errorGEN("e1", PC) )
            break

        if (output == virtual_halt):
          vh_flag = True
          vh_num = PC
          
        output_list.append(output)

    elif type in list(instruction_mapping["u_type"]):
        output = U_TYPE(instruction_elements)
        output_list.append(output)

    elif type in list(instruction_mapping["j_type"]):
        output = J_TYPE(instruction_elements)
        output_list.append(output)

   # code for LABEL
  
    else:
        # opcode not from the mentioned mnemonics
        output_list.clear()
        output_list.append( errorGEN("e2", PC) )
        break

    if (output_list[-1] == virtual_halt):
      if ( PC != (len(assembly)-1) ):
        
    PC += 1

else:
  # this CODE will not be execute if while has been exited due to a BREAK statement
  if (vh_flag == False):
    output_list.clear()
    output_list.append( errorGEN("e6", PC-1) )

# CODE FOR OUTPUT FILE
  




def sext(number, bits):
  # ONLY USE IT TO SIGN EXTEND AN IMMEDIATE VALUE
    """
    This function first converts the number into binary
    and then extends its bits to the required amount
    """
    number = int(number)
    if ( ( number < -(2**(bits-1)) ) or ( number > (2**(bits-1))-1 ) ):
        return "e1"
      
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




errorMAPPING = {"e1": "Error: overflow detected in immediate value" ,
                "e2": "Error: invalid opcode",
                "e3": "Error: invalid register name",
                "e4": "Error: maximum(1000) loop calls reached",
                "e5": "Error: invalid label name",
                "e6": "Error: Virtual Halt missing after last instruction",
                "e7": "Error: Virtual Halt encountered before remaining instructions"}                
              
def errorGEN ( errorNUM, lineNUM ):
  errorMSG = errorMAPPNIG[errorNUM] + " at Line " + (lineNUM + 1)  # 0 PC implies line 1 !!!
  return errorMSG
  




