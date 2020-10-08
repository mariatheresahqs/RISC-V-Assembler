from registers import*

print("Apenas um teste")
Instruction = "sub"
teste = Register(Instruction)
print(teste)



# leitura do arquivo de entrada
arquivo = open("entrada.asm", "r")
conteudo = arquivo.read()
arquivo.close()
print("Arquivo de entrada:")# print para teste
print(conteudo)

# escrita do conteudo traduzido no arquivo de saida
arquivo = open("saida.asm", "w")
arquivo.write(teste) # retorno esta como teste porque a funcao de retorno ainda nao foi concluida
arquivo.close()

# mostrar conteudo traduzido no terminal - leitura do arquivo de saida e impressao
arquivo = open("saida.asm", "r")
conteudo = arquivo.read()
arquivo.close()
print("Arquivo de saida:")  # print para teste
print(conteudo)
