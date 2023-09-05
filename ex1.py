# Abra o arquivo em modo de leitura
uniao = "U"
inter = "I"
diff = "D"
carte = "C"

with open('teste1.txt', 'r') as arquivo:
    # Use um loop para iterar pelas linhas do arquivo
    linhas = arquivo.readlines()  # le as linhas do arquivo
    for i, linha in enumerate(linhas):
        vetor = linha.split
        if uniao == linha[0]:
            if i + 1 < len(linhas):
                l1 = linhas[i+1].strip().split(', ')  # strip para eliminar os espaços entre linhas e o split para dividir entre as vírgulas
                u1 = {str(elementos) for elementos in l1}

                l2 = linhas[i+2].strip().split(', ')
                u2 = {str(elemento) for elemento in l2}  # transforma os elementos do vetor em int

                u3 = u1.union(u2)  # função do set para juntar
                print(u3)
        elif inter == linha[0]:
             if i + 1 < len(linhas):
                l1 = linhas[i+1].strip().split(', ')
                i1 = {str(elementos) for elementos in l1}

                l2 = linhas[i+2].strip().split(', ')
                i2 = {str(elemento) for elemento in l2}
                i3 = i1 & i2
                print(i3)
        elif diff == linha[0]:
             if i + 1 < len(linhas):
                l1 = linhas[i+1].strip().split(', ')
                d1 = {str(elementos) for elementos in l1}

                l2 = linhas[i+2].strip().split(', ')
                d2 = {str(elemento) for elemento in l2}
                d3 = d1.difference(d2)
                print(d3)
        elif carte == linha[0]:
            if i + 1 < len(linhas):
                l1 = linhas[i+1].strip().split(', ')
                c1 = {str(elementos) for elementos in l1}

                l2 = linhas[i+2].strip().split(', ')
                c2 = {str(elemento) for elemento in l2}
                c3 = []

                for n in c1:
                    for num in c2:
                        c3.append((n,num)) 
                print(set(c3))
print("União: conjunto1 {}, conjunto 2 {}. Resultado: {}".format(u1, u2, u3))
print("Interseção: conjunto1 {}, conjunto 2 {}. Resultado: {}".format(i1, i2, i3))
print("Diferença: conjunto1 {}, conjunto 2 {}. Resultado: {}".format(d1, d2, d3))
print("Produto Cartesiano: conjunto1 {}, conjunto 2 {}. Resultado: {}".format(c1, c2, set(c3)))
