# -*- coding: utf-8 -*-

def RegConverter(Instruction):
    # R instructions 0110011
    if(Instruction == "add"):
        return "000"
    if(Instruction == "sub"):
        return "000"
    if(Instruction == "sll"):
        return "001"
    if(Instruction == "slt"):
        return "010"
    if(Instruction == "sltu"):
        return "011"
    if(Instruction == "xor"):
        return "100"
    if(Instruction == "srl"):
        return "101"
    if(Instruction == "sra"):
        return "101"
    if(Instruction == "or"):
        return "110"
    if(Instruction == "and"):
        return "111"
    if(Instruction == "addw"):
        return "000"
    if(Instruction == "subw"):
        return "000"
    if(Instruction == "sllw"):
        return "001"
    if(Instruction == "srlw"):
        return "101"
    if(Instruction == "sraw"):
        return "101"
    else:
        print("Instrução não encontrada")

    # fun7    rs2 rs1 fun3  rd  opcode
    # 0000000         acima     0110011
    # 0100000

    # 0100000 sub sra subw sraw
    # add 00000000000000000000000000110011


def Funct7(Instruction):
    if(Instruction == "sub") or (Instruction == "subw") or (Instruction == "sra") or (Instruction == "sraw"):
        return "0000000"
    else:
        return "0100000"


def Register(Instruction):
    funct7 = Funct7(Instruction)
    # funct7 = "0000"
    rs2 = "00000"
    rs1 = "00000"
    rd = "00000"
    funct3 = RegConverter(Instruction)
    # funct3 = "0000"
    opCode = "0110011"
    codeInstruction = funct7+rs2+rs1+funct3+rd+opCode+"\n"
    return codeInstruction
