from bitstring import Bits

# check the excecute which one used in jal ??
# fix assembler errors
# NEW ERROR TYPE: x0 register CANNOT be changed!!
# Bonus instruction - halt: Possilbe simulation: PC += len(simulator)

#Assumption : all syntactical errors have been handled by assembler. So each line in the input file is a valid 32 bit instruction


#################################################################################################################

def display_file(program_ctr, file_reg):
    global output
    number = sext(str(program_ctr), 32)
    line = ''
    line = number
    for reg in file_reg:
        file_reg_value=file_reg[reg]
        line = line + " 0b" + sext(file_reg_value,32)
    output.append(line)

def display_mem(memory_reg):
    inp_f=open("filename.txt", 'a')
    for reg in memory_reg:
        memory_reg_value=memory_reg[reg]
        line ="0x" "0b" + sext(file_reg_value,32)
    

#################################################################################################################

def add_bin(num1, num2):
    #num 1 and num 2 are in binary string

    a = Bits(bin=num1)  
    b = Bits(bin=num2) 
    
    result = a.int + b.int
    return sext(result, 32)
    
#################################################################################################################

instruction_R = {0110011}  #use if else inside the R type function... 

instruction_I = { 0000011 : {010 : 'lw'},  #may not use these values associated with keys. keys is enough.
                 0010011 : {000 : 'addi', 011 : 'sltiu'},
                 1100111 : {000 : 'jalr'} }

instruction_S = { 0100011 : {010 : 'sw'} }

instruction_B = { 1100011 : {000 : 'beq', 001 : 'bne', 100 : 'blt', 101 : 'bge', 110 : 'bltu', 111 : 'bgeu'} }

instruction_U = { 0110111 : 'lui',
                 0010111 : 'auipc' }

instruction_J = { 1101111 : 'jal'}

instruction_BONUS = { }

################################################################################################################

#function for sign extension
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

########################################################################################

def bin_to_dec ( number, sign = 's' ) :
  # number is a STRING
  # length is atleast 1
  # sign : s means signed, u means unsigned
  sign = sign.lower()
  
  dec = 0
  pow = 0

  length = len(number)
  if length == 0:
    return 0
    
  for i in range( length - 1, 0, -1 ):
    dec += (int(number[i]) * (2**pow) )
    pow += 1

  
  if sign == 's':
    dec -= (int(number[0]) * (2**(length-1)) )
  elif sign == 'u':
    dec += (int(number[0]) * (2**(length-1)) )


  return dec

####################################################################################################################

register =  #starting from 0 to 31 in binary 
  { '00000': 0, '00001': 0, '00010': 0, '00011': 0, 
   '00100': 0, '00101': 0, '00110': 0, '00111': 0, 
   '01000': 0, '01001': 0, '01010': 0, '01011': 0, 
   '01100': 0, '01101': 0, '01110': 0, '01111': 0, 
   '10000': 0, '10001': 0, '10010': 0, '10011': 0, 
   '10100': 0, '10101': 0, '10110': 0, '10111': 0, 
   '11000': 0, '11001': 0, '11010': 0, '11011': 0, 
   '11100': 0, '11101': 0, '11110': 0, '11111': 0 }
  
 # to get value stored in register from its binary. value is in DECIMAL

register_name = { } # to decode the register name from its binary

memory = # memory address starting from 65536 , add 4
{  '10000000000000000': 0, '10000000000000100': 0, '10000000000001000': 0, '10000000000001100': 0, 
   '10000000000010000': 0, '10000000000010100': 0, '10000000000011000': 0, '10000000000011100': 0, 
   '10000000000100000': 0, '10000000000100100': 0, '10000000000101000': 0, '10000000000101100': 0, 
   '10000000000110000': 0, '10000000000110100': 0, '10000000000111000': 0, '10000000000111100': 0, 
   '10000000001000000': 0, '10000000001000100': 0, '10000000001001000': 0, '10000000001001100': 0, 
   '10000000001010000': 0, '10000000001010100': 0, '10000000001011000': 0, '10000000001011100': 0, 
   '10000000001100000': 0, '10000000001100100': 0, '10000000001101000': 0, '10000000001101100': 0, 
   '10000000001110000': 0, '10000000001110100': 0, '10000000001111000': 0, '10000000001111100': 0 } 
# to get content of memory from its binary
######################################################################################################

def display(PC, 
        
virtual_halt = "00000000000000000000000001100011"

import sys
with open (sys.argv[1], "r") as pointer:
    binary = pointer.readlines()

PC = 0
output = []

while (PC <  len( binary ) ):
  line = binary[PC/4]
  opcode = line[25:32]

  if opcode in instruction_R:
          R_TYPE(line)

  if opcode in instruction_I:
          I_TYPE(line)
    
  if opcode in instruction_S:
          S_TYPE(line)

  if opcode in instruction_B:
          B_TYPE(line)

  if opcode in instruction_U:
          U_TYPE(line)

  if opcode in instruction_J:
          J_TYPE(line)

  display_reg(PC, register)
  
  


      
      
        
