import re

reg_ENCODE  = {'zero': '00000',   'ra': '00001',     'sp': '00010',     'gp': '00011', 
               'tp': '00100',     't0': '00101',     't1': '00110',     't2': '00111', 
               's0': '01000',     'fp': '01000',     's1': '01001',     'a0': '01010',     'a1': '01011', 
               'a2': '01100',     'a3': '01101',     'a4': '01110',     'a5': '01111', 
               'a6': '10000',     'a7': '10001',     's2': '10010',     's3': '10011', 
               's4': '10100',     's5': '10101',     's6': '10110',     's7': '10111', 
               's8': '11000',     's9': '11001',     's10': '11010',    's11': '11011', 
               't3': '11100',     't4': '11101',     't5': '11110',     't6': '11111'}




with open(r"", 'r') as pointer:
    assembly = pointer.readlines()
    print(assembly)

pc = 0

# while (pc<(len(assembly))):
  
  #Split the instruction on ' ' and ',' using regex(re) module. items = re.split(' |,', instruction)




def sext(number, bits):
    """
    This function first converts the number into binary
    and then extends its bits to the required amount
    """
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


    
