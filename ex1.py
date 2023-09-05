# Abra o arquivo em modo de leitura
uniao = "U"
inter = "I"
diff = "D"
carte = "C"
with open('D:/RAPHA/Documents/ex.txt', 'r') as arquivo:
    # Use um loop para iterar pelas linhas do arquivo
    linhas = arquivo.readlines()#le as linhas do arquivo
    for i,linha in enumerate(linhas):
        vetor = linha.split
        if uniao in linha:
            if i + 1 < len(linhas):
                l1 = linhas[i+1].strip().split(', ')#strip para eliminar os espaços entre linhas e o split para dividir entre as virgulas
                u1 = {str(elementos) for elementos in l1}
                
                l2 = linhas[i+2].strip().split(', ')
                u2 = {str(elemento) for elemento in l2}#transforma os elementos do vetor em int
                
                u1.update(u2)#função do set para juntar
                print(u1)        
        elif inter in linha:
             if i + 1 < len(linhas):
                l1 = linhas[i+1].strip().split(', ')
                i1 = {(elementos) for elementos in l1}
                
                l2 = linhas[i+2].strip().split(', ')
                i2 = {(elemento) for elemento in l2}
                i3 = []
                
                for n in i1:
                    for num in i2:
                        if n == num:
                            i3.append(n)
                print(i3)
        elif diff in linha:
             if i + 1 < len(linhas):
                l1 = linhas[i+1].strip().split(', ')
                d1 = {(elementos) for elementos in l1}
                
                l2 = linhas[i+2].strip().split(', ')
                d2 = {(elemento) for elemento in l2}
                d3 = d1.difference(d2)
                print(d3)
                            
            
                
        # Leia cada linha e faça o que desejar com ela
         # Uc1 = {linhas[i+1]}
              #  c2 = {linhas[i+2]}
               # c1.update(c2)
               # print(c1)
       



