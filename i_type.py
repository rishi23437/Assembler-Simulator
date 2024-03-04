# addi , sltiu , jalr , l{b|h|w|d}

map_I_TYPE = { "addi" : ["0010011", "000"] , 
              "sltiu" : ["0010011", "011"] , 
              "jalr" : ["1100111", "000"] , 
              "lw" : ["0000011","010"] , 
              "lb" : ["", ""] , 
              "lh" : ["", ""] , 
              "ld" : ["", ""] }

def I_TYPE( I_instruction ):
  imm = I_instruction[3]
  rs = reg_ENCODE(I_instruction[2])
  rd = reg_ENCODE(I_instruction[1])
  
  funct = map_I_TYPE[I_instruction[0]][1]
  opc = map_I_TYPE[I_instruction[0]][0]
  
  encoded = imm + rs + funct + rd + opc
  return encoded

