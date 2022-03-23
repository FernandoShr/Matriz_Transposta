matriz = []

linhas = int(input("Digite o número de linhas  da matriz M: "))
colunas = int(input("Digite o número de colunas da matriz M: "))

for n_linhas in range (linhas):
    linha = []
    for n_colunas in range (colunas):
        linha.append (int(input("Digite o elemento {0} {1} da matriz: ".format (n_linhas+1,n_colunas+1) )))
    matriz.append(linha)

print("MATRIZ")
for n_linhas in range (linhas):
    for n_colunas in range (colunas):
        print("{0}.0 ".format (matriz[n_linhas][n_colunas]), end="")
    print("")

print("\nMATRIZ TRANSPOSTA:")
for n_colunas in range (colunas):
    for n_linhas in range (linhas):
        print("{0}.0 ".format (matriz[n_linhas][n_colunas]), end="")
    print("")