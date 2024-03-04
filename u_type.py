functions_itype = {"lui":"0110111",
                   "auipc":"0010111"
                }

def u_type(item):
    #item = re.split(" |,", instruction)  its already split when giving argument to the function

    imm=sext(int(item[2]),20)
    reg=reg_ENCODE[item[1]]
    op_c=functions_itype[item[0]]
    
    return  imm+reg+op_c
