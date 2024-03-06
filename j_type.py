functions_jtype={"jal":"0010111"}

def J_TYPE(J_instruction):
  '''
  J_instruction is a string in format
  {(function name),(destination register),(label)}

  returns : 32 bit binary sequence
  '''
  
  imm=sext(int(J_instruction[2],20))
  reg=reg_ENCODE.get(J_instruction[1])
  op_code=functions_jtype[J_instruction[0]]
  imm=imm[0]+imm[10:20]+imm[9]+[1:9]

  if (imm == "e1"):
      return imm
    
  if (reg == None):
      return "e3"
         
  return imm+reg+op_code
