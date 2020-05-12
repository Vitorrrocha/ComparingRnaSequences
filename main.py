import matplotlib.pyplot as plt
import copy
aux = 0
m = 0
human = open("18s_human.fasta").read()
bacteria = open("16s_bacteria.fasta").read()
seq_human = {}
seq_bacteria = {}

while m == 0:
    if aux == 0:
        entrada = human
    else:
        entrada = bacteria
        m = 1

    cont = {}

    for i in ['A' ,'T' ,'C' ,'G']:
        for j in ['A' ,'T' ,'C' ,'G']:
            cont[i + j] = 0

    entrada = entrada.replace('\n','')

    for k in range(len(entrada) - 1):
        cont[entrada[k] + entrada[k + 1]] += 1
        if aux == 0:
            seq_human = copy.deepcopy(cont)
        else:
            seq_bacteria = copy.deepcopy(cont)

    aux += 1


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))

ax1.bar(seq_human.keys(), seq_human.values(), width=0.4, align='edge', label='Human: 18S rRNA gene')
ax1.bar(seq_bacteria.keys(), seq_bacteria.values(), width=-0.4, align='edge', label='Bacteria: Escherichia coli 16S ribosomal')
ax1.set_ylabel('Frequency')
ax1.set_xlabel('Nitrogenous Bases')
ax1.legend()
plt.show()

print(seq_human)
print(seq_bacteria)