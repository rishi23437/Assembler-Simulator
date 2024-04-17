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

def mul_bin(num1, num2):
    #num 1 and num 2 are in binary string
    a = bin_to_dec(num1)
    b = bin_to_dec(num2)
    result = sext( (a*b), 32)
    return result


# HALT
# opcode 0000110
#let all other bits be filler 0
halt = '00000000000000000000000000000110'

# simply have to write in while loop, if line == halt, break. No need for function

#############################################################

# rvrs_opcode = '0000111'
def rvrs( line ):
  global PC
  global memory
  global register
  
  # syntax : '000000000000' + rs1 + '000' + rd + '0000111'
  rs1 = line[12:17]
  rd = [20:25]
  register[rd] = register[rs1][::-1]
  
  PC += 4
####################################################

def mul(line):
    '''
    Input format: Filler bits(10 zeroes) + rd + rs1 + rs2 + opcode(0000100)
    '''
    global PC, register

    rd = line[10:15]
    rs1 = line[15:20]
    rs2 = line[20:25]

    register[rd] = mul_bin(register[rs1], register[rs2])

    PC += 4

def rst():
    '''
    No input for reset, just check in while loop if opcode matches with 0000101
    '''
    global PC, register
    for key in register:
        if key == '00010':
            register[key] = '00000000000000000000000100000000'
            continue
        else:
            register[key] = '00000000000000000000000000000000'

    PC += 4




  
  

