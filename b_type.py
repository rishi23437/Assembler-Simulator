
map_I_TYPE = {"addi" :   ["0010011", "000"] , 
              "sltiu" :  ["0010011", "011"] , 
              "jalr" :   ["1100111", "000"] , 
              "lw" :     ["0000011","010"] } 

def I_TYPE( I_instruction ):
  '''argument : list type, instruction
  returns : string of encoded binary
  '''
  rd = reg_ENCODE.get(I_instruction[1])
  
  if ((I_instruction[0] != "lw"):
      imm = sext(int(I_instruction[3]),12)
      rs = reg_ENCODE.get(I_instruction[2])    

  else:
      imm = sext(int(I_instruction[2]),12)
      rs = reg_ENCODE.get(I_instruction[3]) 
                           
  if (imm == "e1"):
      return imm
    
  if (rs == None) or (rd == None):
      return "e3"
      
  funct = map_I_TYPE[I_instruction[0]][1]
  opc = map_I_TYPE[I_instruction[0]][0]
  
  encoded = imm + rs + funct + rd + opc   
  return encoded
