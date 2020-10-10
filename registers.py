# -*- coding: utf-8 -*-

# REGISTRADOR - configuracao em bits
# funct7    rs2     rs1     funct3      rd      opcode
# 0000000                   abaixo              0110011
# 0100000


# FUNCAO QUE CONVERTE O CODIGO DA FUNCAO DE SETE BITS EM BINARIO
def Funct7(instrucao):
    if(instrucao == "sub") or (instrucao == "subw") or (instrucao == "sra") or (instrucao == "sraw"):
        return "0100000"
    else:
        return "0000000"


# FUNCAO QUE CONVERTE O CODIGO DE OPERACAO EM BINARIO
def Funct3(instrucao):
    operacoes = {
        "add": "000",
        "sub": "000",
        "sll": "001",
        "slt": "010",
        "sltu": "011",
        "xor": "100",
        "srl": "101",
        "sra": "101",
        "or": "110",
        "and": "111",
        "addw": "000",
        "subw": "000",
        "sllw": "001",
        "srlw": "101",
        "sraw": "101",
    }
    if operacoes[instrucao] == None:
        print("Operação não encontrada.")
        return "-1"
    return operacoes[instrucao]


# FUNCAO DE CONVERTE O TIPO REGISTRO EM CODIGO BINARIO
def Registrador(registrador):
    reg = {
        'x0': '00000',
        'x1': '00001',
        'x2': '00010',
        'x3': '00011',
        'x4': '00100',
        'x5': '00101',
        'x6': '00110',
        'x7': '00111',
        'x8': '01000',
        'x9': '01001',
        'x10': '01010',
        'x11': '01011',
        'x12': '01100',
        'x13': '01101',
        'x14': '01110',
        'x15': '01111',
        'x16': '10000',
        'x17': '10001',
        'x18': '10010',
        'x19': '10011',
        'x20': '10100',
        'x21': '10101',
        'x22': '10110',
        'x23': '10111',
        'x24': '11000',
        'x25': '11001',
        'x26': '11010',
        'x27': '11011',
        'x28': '11100',
        'x29': '11101',
        'x30': '11110',
        'x31': '11111'
    }

    if reg[registrador] == None:
        print("Registrador não encontrado.")
        return "-1"
    return reg[registrador]


# FUNCAO RESPONSAVEL POR MONTAR AS OPERACOES NOS REGISTRADORES EM BINARIO
def TipoR(instrucao, rd, rs1, rs2):
    funct7 = Funct7(instrucao)
    funct3 = Funct3(instrucao)
    rd = Registrador(rd)
    rs1 = Registrador(rs1)
    rs2 = Registrador(rs2)
    Optcode = '0110011'
    return funct7+rs2+rs1+funct3+rd+Optcode


# def Tradutor(instrucao, rd, rs1, rs2):
#     if (instrucao == TipoR):
#         TipoR(instrucao, rd, rs1, rs2)
#     # else:
#         # TipoI(instrucao, rd, rs1, rs2)
