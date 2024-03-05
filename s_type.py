# s{b|h|w|d}

map_S_TYPE = {"sw" :     ["0100011","010"] , 
              "sb" :     ["0100011","000"] ,  # using https://msyksphinz-self.github.io/riscv-isadoc/html/rvi.html#lb
              "sh" :     ["0100011","001"] , 
              "sd" :     ["0100011","XXX"]}   # INSUFFICIENT INFORMATION !!!

def S_TYPE( S_instruction ):
  '''argument : list type, instruction
  returns : string of encoded binary
  '''
  imm = sext(int(S_instruction[2]),12)
  rt = reg_ENCODE.get(S_instruction[3])
  rd = reg_ENCODE.get(S_instruction[1])

  if (rt == None) or (rd == None):
    return "e3"
    
  funct = map_S_TYPE[S_instruction[0]][1]
  opc = map_S_TYPE[S_instruction[0]][0]
  
  encoded = imm[0:7] + rd + rt + funct + imm[7:] + opc
  return encoded
