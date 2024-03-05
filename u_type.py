functions_itype = {"lui":"0110111",
                   "auipc":"0010111"}

def u_type(U_instruction):
  
    ''' 
    U_instruction is a list of string in format :
    [(Name of u_type function),(destination register),(value of the immediate)]

    returns : Above provided U_instrution into 32 bit binary format in a string
    '''
  
    imm = sext(int(U_instruction[2]),20)
    reg = reg_ENCODE[U_instruction[1]]
    op_c= functions_itype[U_instruction[0]]
    
    return  imm+reg+op_c
