def I_TYPE( line ):
  # line is 32 bits
  # STORE 32 bits in 1 register

  global PC

  imm = line[0:12]
  rs1 = line[12:17]
  funct3 = line[17:20]
  rd = line[20:25]
  opcode = line[25:32]

  #lw
  if opcode == '0000011':
  #rd = mem(rs1 + sext(imm[11:0]))
    register[rd] = memory[sext(bin_to_dec(register[rs1])) + bin_to_dec(imm), 17)]

  #addi
  if opcode == '0010011':
    if funct3 == '000':
      register[rd] = sext(bin_to_dec(register[rs]) + bin_to_dec(imm),32)

  #sltiu
    elif funct3 == '011':
      #rd = 1. If unsigned(rs) < unsigned(imm)
      if bin_to_dec(register[rs],'u') < bin_to_dec(bin_to_dec(imm),'u') :
        register[rd] = sext(1,32)   

  #jalr
  
  if opcode == '1100111':
    # register[rd] = PC + 1 //
    # #And store(link) the return address in (rd).
    # PC = register_name['x6'] + bin_to_dec(imm)
    # if PC%2==1:
    #   PC -= 1
    
    
