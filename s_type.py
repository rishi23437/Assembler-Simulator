# s{b|h|w|d}

map_S_TYPE = {"sw" :     ["0100011","010"] , 
              "sb" :     ["0100011","010"] ,  #assumption - sw, sb, sh, sd are equivalent --> REVISIT this line
              "sh" :     ["0100011","010"] , 
              "sd" :     ["0100011","010"]}

def S_TYPE( S_instruction ):
  '''argument : list type, instruction
  returns : string of encoded binary
  '''
  imm = sext(string_to_number(S_instruction[2]),12)
  rt = reg_ENCODE[S_instruction[3]]
  rd = reg_ENCODE[S_instruction[1]]
  
  funct = map_S_TYPE[S_instruction[0]][1]
  opc = map_S_TYPE[S_instruction[0]][0]
  
  encoded = imm[0:7] + rd + rt + imm[7:] + opc
  return encoded
