# -*- coding: utf-8 -*-
from registers import*

# leitura do arquivo de entrada
arquivo = open("entrada.asm", 'r')
# abre arquivo de saida para escrita
saida = open('saida.asm', 'w')
# leitura de todas as linhas do arquivo
linhas = arquivo.readlines()
for i in linhas:
    entradaFormatada = i.strip("\n")
    instrucao = entradaFormatada.split()[0]
    print(entradaFormatada) # APENAS PARA TESTES!!!
    rd = entradaFormatada.split(" ")[1]
    rd = rd.replace(',','') 
    rs1 = entradaFormatada.split(",")[1]
    rs1 = rs1.replace(' ', '')
    rs2 = entradaFormatada.split(", ")[2]
    binario = TipoR(instrucao, rd, rs1, rs2) # TEM DE TROCAR PELA FUNCAO TRADUTOR QUANDO A FUNCAO IMEDIATA FICAR PRONTA!!!
    # escrita do conteudo traduzido no arquivo de saida
    saida.writelines(binario+"\n")
arquivo.close()
saida.close()

# mostrar conteudo traduzido no terminal - leitura do arquivo de saida e impressao
arquivo = open("saida.asm", "r")
saida = arquivo.read()
arquivo.close()
print("Arquivo de saida:")  # print para teste
print(saida)
