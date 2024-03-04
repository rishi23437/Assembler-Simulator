

with open(r"", 'r') as pointer:
    assembly = pointer.readlines()
    print(assembly)

pc = 0

# while (pc<(len(assembly))):

def string_EXT( length , filler , value ):
    num = length - len(value)
    final = filler*num + value
    return final

def reg_ENCODE( reg_NAME ):
    reg_NUM = int(reg_NAME[1:])
    bin_EQ = bin(reg_NUM)[2:]
    bin_EQ = string_EXT( 5 , "0" , bin_EQ )
    return bin_EQ

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


    
