import matplotlib.pyplot as plt
import copy
aux = 0
m = 0
human = open("18s_human.fasta").read()
bacteria = open("16s_bacteria.fasta").read()
seq_human = {}
seq_bacteria = {}

while m == 0:   #Necessario para fazer a leitura dos dois arquivos em uma execução e popular assim os dicionarios.
    if aux == 0:    #Foi utilizado para que seja possivel a leitura da bacteria e do humano em momentos diferentes.
        entrada = human
    else:
        entrada = bacteria
        m = 1   #mudança feita para sair do loop e poder executar os codigos de plotagem do grafico.

    cont = {}  #Dicionario que ira receber as bases nitrogenadas.

    for i in ['A' ,'T' ,'C' ,'G']:
        for j in ['A' ,'T' ,'C' ,'G']:
            cont[i + j] = 0            #Populando o dicionario com cada combinação de bases nitrogenas com valor zero.

    entrada = entrada.replace('\n','')      #substituição necessaria para que o arquivo continue sendo lido.

    for k in range(len(entrada) - 1):       #O arquivo será lido completamente em pares, menos 1 pois seria o fim do arquivo não contendo mais pares para sererm lidos.
        cont[entrada[k] + entrada[k + 1]] += 1  #Toda vez que um caracter (base nitrogenada) mais o proximo for lido ex: "AC", será somado mais um a aquele par no dicionario.
        
        if aux == 0: 
            seq_human = copy.deepcopy(cont)  #variavel que recebe a copia do dicionario atual.
        else:
            seq_bacteria = copy.deepcopy(cont)  #variavel que recebe a copia do dicionario atual.

    aux += 1

#   Montagem do grafico em barras utilizando dois dicionarios
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))

ax1.bar(seq_human.keys(), seq_human.values(), width=0.4, align='edge', label='Human: 18S rRNA gene')
ax1.bar(seq_bacteria.keys(), seq_bacteria.values(), width=-0.4, align='edge', label='Bacteria: Escherichia coli 16S ribosomal')
ax1.set_ylabel('Frequency')
ax1.set_xlabel('Nitrogenous Bases')
ax1.legend()
plt.show()

print(seq_human)
print(seq_bacteria)
