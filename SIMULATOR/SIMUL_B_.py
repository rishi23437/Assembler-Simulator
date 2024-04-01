def B_TYPE( line ):
  # line is 32 bits
  #imm==0?

  imm = line[0]+line[24]+line[1:7]+line[20:24]+'0'
  rs1 = line[12:17]
  funct3 = line[17:20]
  rs2 = line[7:12]

  global PC

  #beq
  if funct3 == '000':
    if (rs1==rs2):
      PC+=bin_to_dec(imm)
    else:
      PC+=1

  #bne
  elif funct3 == '001':
    if (rs1!=rs2):
      PC+=bin_to_dec(imm)
    else:
      PC+=1

  #bge
  elif funct3 == '101':
    if (bin_to_dec(rs1)>=bin_to_dec(rs2)):
      PC+=bin_to_dec(imm)
    else:
      PC+=1

  #bgeu
  elif funct3 == '111':
    if (bin_to_dec(rs1, 'U')>=bin_to_dec(rs2, 'U')):
      PC+=bin_to_dec(imm)
    else:
      PC+=1

  #blt
  elif funct3 == '100':
    if (bin_to_dec(rs1)<bin_to_dec(rs2)):
      PC+=bin_to_dec(imm)
    else:
      PC+=1

  #bltu
  elif funct3 == '110':
    if (bin_to_dec(rs1, 'U')<bin_to_dec(rs2, 'U')):
      PC+=bin_to_dec(imm)
    else:
      PC+=1

  else:
    #error
