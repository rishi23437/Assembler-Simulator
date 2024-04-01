def U_TYPE( line ):
  #line is 32 bits
  global PC
  
  imm = line[0:19]
  rd = line[20:24]
  opcode =line[25:31]

  if (opcode == "0110111"):
    register[rd] = PC + bin_to_dec(imm)

  elif (opcode == "0010111"):
    register[rd] = bin_to_dec(imm)
