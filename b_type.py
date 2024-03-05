map_B_TYPE = { "beq" : ["1100011", "000"] , 
              "bne" : ["1100011", "001"] , 
              "blt" : ["1100011", "100"] , 
              "bge" : ["1100011", "101"] , 
              "bltu" : ["1100011", "110"] , 
              "bgeu" : ["1100011", "111"] }

def B_TYPE( B_instruction ):
  """
  B_instruction is a list of the form [[opcode, funct3], rs1, rs2, immediate value not converted in bits]
  """
  imm = sext(int(B_instruction[3]),13)
  if (imm[0]=='e'):
      return imm
  rs1 = reg_ENCODE.get(B_instruction[1])
  rs2 = reg_ENCODE.get(B_instruction[2])
  
  funct3 = map_B_TYPE[B_instruction[0]][1]
  opc = map_B_TYPE[B_instruction[0]][0]
  
  decoded = imm[0] + imm[2:8] + rs2 + rs1 + funct3 + imm[8:12] + imm[1] + opc
  return decoded
