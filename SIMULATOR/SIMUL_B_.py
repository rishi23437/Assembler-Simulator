def B_TYPE( line ):
  # line is 32 bits

  imm = line[0]+line[24]+line[1:7]+line[20:24]+'0'
  rs1 = line[12:17]
  funct3 = line[17:20]
  rs2 = line[7:12]
  opcode = line[25::]

  # #beq
  # if opcode == '0000011':
  # #rd = mem(rs1 + sext(imm[11:0]))
  #   register[rd] = memory[register[rs1] + bin_to_dec(imm)]

  # #addi
  # if opcode == '0010011':
  #   if funct3 == '000':
  #     register[rd] = register[rs] + bin_to_dec(imm)

  # #sltiu
  #   elif funct3 == '011':
  #     #rd = 1. If unsigned(rs) < unsigned(imm)
  #     if abs(register[rs]) < abs(bin_to_dec(imm)) :
  #       register[rd] = 1   

  # #jalr
  # if opcode == '1100111':
  #   register[rd] = PC + 4
  #   #And store(link) the return address in (rd).
  #   PC = register_name['x6'] + bin_to_dec(imm)
  #   if PC%2==1:
  #     PC -= 1
    
    
