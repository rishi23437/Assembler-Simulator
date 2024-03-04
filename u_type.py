functions_itype = {"lui":"0110111",
                   "auipc":"0010111"
                }

def u_type(instruction):
    item = re.split(" |,", instruction)

    imm=sext(string_to_number(item[2]),20)
    reg=reg_ENCODE[item[1]]
    op_c=functions_itype[item[0]]
    
    return  imm+reg+op_c
