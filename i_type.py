# addi , sltiu , jalr , l{b|h|w|d}

map_I_TYPE = {"addi" :   ["0010011", "000"] , 
              "sltiu" :  ["0010011", "011"] , 
              "jalr" :   ["1100111", "000"] , 
              "lw" :     ["0000011","010"] , 
              "lb" :     ["0000011","000"] ,  #using https://msyksphinz-self.github.io/riscv-isadoc/html/rvi.html#lb
              "lh" :     ["0000011","001"] , 
              "ld" :     ["0000011","XXX"]} # insufficient information!!!!!

def I_TYPE( I_instruction ):
  '''argument : list type, instruction
  returns : string of encoded binary
  '''
  imm = sext(int(I_instruction[3]),12)
  rs = reg_ENCODE.get(I_instruction[2])
  rd = reg_ENCODE.get(I_instruction[1])

  if (imm == "e1"):
    return imm

  if (rs == None) or (rd == None):
    return "e3"
  
  funct = map_I_TYPE[I_instruction[0]][1]
  opc = map_I_TYPE[I_instruction[0]][0]
  
  encoded = imm + rs + funct + rd + opc
  return encoded

