def S_TYPE( line ):
  # line is 32 bits

  imm = line[0:7] + line[20:25]
  rs2 = line[7:12]
  rs1 = line[12:17]
  funct3 = line[17:20]
  opcode = line[25:32]

  memory[register[rs1] + bin_to_dec(imm)] = register[rs2]
    
