# addi , sltiu , jalr , l{b|h|w|d}

map_I_TYPE = { "addi" : addi , "sltiu" : sltiu , "jalr" : jalr , "lw" : l_type , "lb" : l_type , "lh" : l_type , "ld" : l_type }

def addi( I_instruction ):
  rd = I_instruction[2]
  rs = I_instruction[3]
  imm = 
