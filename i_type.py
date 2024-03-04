# addi , sltiu , jalr , l{b|h|w|d}

map_I_TYPE = { "addi" : {opcode: "0010011", funct3: "000"} , 
              "sltiu" : {opcode: "0010011", funct3: "011"} , 
              "jalr" : {opcode: "1100111", funct3: "000"} , 
              "lw" : {opcode: "0000011", funct3: "010"} , 
              "lb" : {opcode: "", funct3: ""} , 
              "lh" : {opcode: "", funct3: ""} , 
              "ld" : {opcode: "", funct3: ""} }

def I_TYPE( I_instruction ):
  imm = I_instruction[4]
  rs = reg_ENCODE(I_instruction[3])
  rd = reg_ENCODE(I_instruction[2])
  
  funct = map_I_TYPE[I_instruction[0]][funct3]
  opc = map_I_TYPE[I_instruction[0]][opcode]
  
  encoded = imm + rs + funct + rd + opc
  return encoded

