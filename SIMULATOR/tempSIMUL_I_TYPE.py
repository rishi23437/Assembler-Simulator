def I_TYPE( line ):
  # line is 32 bits

  imm = line[0:12]
  rs1 = line[12:17]
  funct3 = line[17:20]
  rd = line[20:25]
  opcode = line[25:32]

  #lw
  if opcode == '0000011':
  #rd = mem(rs1 + sext(imm[11:0]))
    register[rd] = memory[register[rs1] + bin_to_dec(imm)]

  #addi
  if opcode == '0010011':
    if funct3 == '000':
      register[rd] = register[rs] + bin_to_dec(imm)

  #sltiu
    elif funct3 == '011':
      #rd = 1. If unsigned(rs) < unsigned(imm)
      if abs(register[rs]) < abs(bin_to_dec(imm)) :
        register[rd] = 1   

  #jalr
  if opcode == '1100111':
    register[rd] = PC + 4
    #And store(link) the return address in (rd).
    PC = register_name['x6'] + bin_to_dec(imm)
    if PC%2==1:
      PC -= 1
    
    
