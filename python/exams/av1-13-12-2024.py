# 1) Faça um algoritmo que peça uma string ao usuário e mostre quantas vogais existem na string. Por
# exemplo, para a string “alo mundo” deve ser exibida a saída “a=1, o=2, u=1”. Para construir a lógica
# de contagem, considere a string como sendo um vetor de caracteres.

palavra = input("Digite uma palavra: ")
lista_de_letras = list(palavra)
a, e, i, o, u = 0, 0, 0, 0, 0 

for letra in lista_de_letras:
    if letra == "a":
        a += 1
    if letra == "e":
        e += 1
    if letra == "i":
        i += 1
    if letra == "o":
        o += 1
    if letra == "u":
        u += 1
    else:
        print("")

print("a =", a," | e =", e," | i =", i," | o =", o," | u =", u)

# 2) Considere o algoritmo a seguir:

# pede um número (a)
# pede outro número (b)
# calcula x1 = a + b
# pede outro número (c)
# calcula x2 = x1 * c
# pede outro número (d)
# calcula x3 = x2 + d
# pede outro número (e)
# calcula x4 = x3 * e
# pede outro número (f)
# calcula x5 = x4 + f
# mostra a soma dos cálculos (x1+x2+x3+x4+x5)

# Nesta lógica há trechos de código repetidos. Além
# disso, o programa fica maior à medida em que
# mais números são necessários (imagine essa lógica
# com 50 números!). Proponha uma solução para
# reduzir o tamanho desse algoritmo, mantendo a
# mesma funcionalidade.

listOne, listTwo, listThree, listFour, listFive = [], [], [], [], []

for i in range(5):
    if i == 0:
        numberACE = int(input("Digite um número: "))
        numberBDF = int(input("Digite um número: "))
        listOne.append(numberACE, numberBDF, numberACE + numberBDF)
    elif i == 1:
        numberACE = int(input("Digite um número: "))
        listTwo.append(numberACE, listOne[2] * numberACE)
    elif i == 2:
        numberBDF = int(input("Digite um número: "))
        listThree.append(numberBDF, listTwo[1] + numberBDF)
    elif i == 3:
        numberACE = int(input("Digite um número: "))
        listFour.append(numberACE, listThree[1] * numberACE)
    else:
        numberBDF = int(input("Digite um número: "))
        finalSum = listFour[1] + numberBDF
        print("Soma dos cálculos: ", finalSum)