

with open(r"", 'r') as pointer:
    assembly = pointer.readlines()
    print(assembly)

pc = 0

# while (pc<(len(assembly))):

def sign_EXT( length , sign , value ):
    num = length - len(value)
    final = sign*num + value
    return final

def reg_ENCODE( reg_NAME ):
    reg_NUM = int(reg_NAME[1:])
    bin_EQ = bin(reg_NUM)[2:]
    bin_EQ = sign_EXT( 5 , 0 , bin_EQ )
    return bin_EQ



    
