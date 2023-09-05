'''ENUNCIADO
Página | 2 de 3
Andrey Cabral Meira
Avaliação em grupo 01
Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
operações que serão realizadas entre dois conjuntos de dados.
O programa que você desenvolverá irá receber como entrada do usuário vários conjuntos de
dados e várias operações. Estas operações e dados estarão representadas em um arquivo de textos
contendo apenas os dados referentes as operações que devem ser realizadas segundo a seguinte regra
fixa: a primeira linha do arquivo de texto de entrada conterá o número de operações que estão
descritas no arquivo, este número de operações será um inteiro; as linhas seguintes seguirão sempre o
mesmo padrão de três linhas: a primeira linha apresenta o código da operação (U para união, I para
interseção, D para diferença e C produto cartesiano), a segunda e terceira linhas conterão os elementos
dos conjuntos separados por virgulas. A seguir está um exemplo entradas que podem existir em um
teste para o programa que você irá desenvolver:
U
3, 5, 67, 7
1, 2, 3, 4
I
1, 2, 3, 4, 5
4, 5
D
1, A, C, 34
A, C, D, 23
C
3, 4, 5, 5, A, B, R
1, B, C, D, 1
Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
{𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
a informação e a formatação mostrada a seguir:
União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
contendo um número diferente de operações, operações com dados diferentes, e operações em ordem
diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no
ambiente repl.it quanto no ambiente Github.
Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com,
no mínimo um arquivo de testes criado pelo próprio professor'''

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
        if uniao == linha[0] and linha[1] == '\n':
            if i + 1 < len(linhas):
                l1 = linhas[i+1].strip().split(', ')  # strip para eliminar os espaços entre linhas e o split para dividir entre as vírgulas
                u1 = {str(elementos) for elementos in l1}

                l2 = linhas[i+2].strip().split(', ')
                u2 = {str(elemento) for elemento in l2}  # transforma os elementos do vetor em int

                u3 = u1.union(u2)  # função do set para juntar
                print(u3)
        elif inter == linha[0] and linha[1] == '\n':
             if i + 1 < len(linhas):
                l1 = linhas[i+1].strip().split(', ')
                i1 = {str(elementos) for elementos in l1}

                l2 = linhas[i+2].strip().split(', ')
                i2 = {str(elemento) for elemento in l2}
                i3 = i1 & i2
                print(i3)
        elif diff == linha[0] and linha[1] == '\n':
             if i + 1 < len(linhas):
                l1 = linhas[i+1].strip().split(', ')
                d1 = {str(elementos) for elementos in l1}

                l2 = linhas[i+2].strip().split(', ')
                d2 = {str(elemento) for elemento in l2}
                d3 = d1.difference(d2)
                print(d3)
        elif carte == linha[0] and linha[1] == '\n':
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
