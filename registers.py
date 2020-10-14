import ctypes
# -*- coding: utf-8 -*-

#####################
# REGISTRADOR - configuracao em bits
# funct7    rs2     rs1     funct3      rd      opcode
# 0000000                   abaixo              0110011
# 0100000
#####################
# IMEDIATOS - configuracao em bits
# imm       rs1     funct3      rd      opcode
# 12bits    5bits   3bits       5bits   7bits

# FUNCAO QUE DEFINE O TIPO DE OPERACAO
def tipoOpercao(instrucao):
    operacoes = {
        # Operacoes de registradores
        "add": "TipoR",
        "sub": "TipoR",
        "sll": "TipoR",
        "slt": "TipoR",
        "sltu": "TipoR",
        "xor": "TipoR",
        "srl": "TipoR",
        "sra": "TipoR",
        "or": "TipoR",
        "and": "TipoR",
        "addw": "TipoR",
        "subw": "TipoR",
        "sllw": "TipoR",
        "srlw": "TipoR",
        "sraw": "TipoR",
        #Operacoes de imediatos
        "addi": "TipoI",
        "slti": "TipoI",
        "sltiu": "TipoI",
        "xori": "TipoI",
        "ori": "TipoI",
        "andi": "TipoI",
        "slli": "TipoI",
    }
    value = operacoes.get(instrucao)
    if value == None:
        print("Operação não encontrada.")
        return
    return operacoes[instrucao]


# FUNCAO QUE CONVERTE O CODIGO DA FUNCAO DE SETE BITS EM BINARIO
def Funct7(instrucao):
    if(instrucao == "sub") or (instrucao == "subw") or (instrucao == "sra") or (instrucao == "sraw"):
        return "0100000"
    else:
        return "0000000"


# FUNCAO QUE CONVERTE O CODIGO DE OPERACAO EM BINARIO
def Funct3(instrucao):
    operacoes = {
        # Operacoes de registradores
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
        #Operacoes de imediatos
        "addi": "000",
        "slti": "010",
        "sltiu": "011",
        "xori": "100",
        "ori": "110",
        "andi": "111",
        "slli": "001",
    }
    value = operacoes.get(instrucao)
    if value == None:
        print("Operação não encontrada.")
        return
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

    value = reg.get(registrador)
    if value == None:
        print("Operação não encontrada.")
        return
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


# FUNCAO RESPONSAVEL POR CONVERTER O VALOR DESTINADO AO IMEDIATO EM BINARIO
def Imm(numero, bits=12):
    numero = int(numero)
    if(numero >= 0):
        # Converte o valor do numero em binario
        strImm = bin(int(numero))
        # Retira a parte de descricao binaria (0b) da string
        strImm = strImm.replace("0b", "")
        # Preenche apenas o numero dado e convertido em binario com os bits 0 necessarios a esquerda
        while len(strImm) != bits:
            # Se o valor convertido em bits ja possui o valor maximo de bits ja da o retorno
            if len(strImm) == bits:
                return strImm
            # Se o valor convertido em bits for maior que o valor maximo de bits
            if len(strImm) > bits:
                print("Valor decimal maior que o permitido em 1 bit!\n")
                return strImm
            # Caso o valor convertido em bits seja menor que o valor maximo, adicina bits 0 a esquerda
            strImm = "0"+strImm
        return strImm
    # Caso o valor convertido em bits seja negativo
    else:
        # Converte o valor inteiro negativo para para seu complemento de dois
        strImm = bin(ctypes.c_ushort(numero).value)
        strImm = strImm.replace("0b", "")
        # Retorno apenas dos 12 ultimos bits convertidos
        return strImm[4:16]

# FUNCAO RESPONSAVEL POR MONTAR AS OPERACOES DE IMEDIATOS EM BINARIO
def TipoI(instrucao, rd, rs1, imm):
    imm = Imm(imm)
    rs1 = Registrador(rs1)
    funct3 = Funct3(instrucao)
    rd = Registrador(rd)
    Optcode = '0010011'
    return imm+rs1+funct3+rd+Optcode

# FUNCAO QUE CONVERTE A OPERACAO POR TIPO 
def Tradutor(instrucao, rd, rs1, rs2):
    tipo = tipoOpercao(instrucao)
    if (tipo == "TipoR"):
        return TipoR(instrucao, rd, rs1, rs2)
    else:
        return TipoI(instrucao, rd, rs1, rs2)
