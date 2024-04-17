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




  
  

