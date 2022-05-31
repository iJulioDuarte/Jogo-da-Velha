jogadas = 0
linha = 0
coluna = 0
soma = 0
vez = 0
velha = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def exibirtab():  
    global velha
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])


while True:
    exibirtab()
    if vez >=10:
        break
    elif vez % 2 == 0:
        linha, coluna = map(int, input("Digite o valor da linha e da coluna: ").split())
        while velha[linha][coluna] == 'X' or velha[linha][coluna] == 'O':
            print("Está posição ja está ocupada, tente outra:")
            linha, coluna = map(int, input("Digite o valor da linha e da coluna: ").split())
        velha[linha][coluna] = "X"
        vez +=1
        print()

    #verific
    for i in range(3):
        for j in range(3):
            if velha[i][j] == 'X':
                soma += 1
            if soma == 3:
                exibirtab()
                print("X ganhou!")
                vez = 10
        soma = 0
    if vez >=10:
        break
    soma = 0

    for i in range(3):
        soma = 0
        for j in range(3):
            if velha[j][i] == 'X':
                soma += 1
            if soma == 3:
                exibirtab()
                print("X ganhou!")
                vez = 10
        soma = 0
    if vez >=10:
        break
    soma = 0

    for i in range(3):
        if velha[i][i] == 'X':
            soma += 1
        if soma == 3:
            exibirtab()
            print("X ganhou!")
            vez = 10
    soma = 0
    if vez >=10:
        break
    soma = 0
    
    for i in range(3):
        if velha[i][2-i] == 'X':
            soma += 1
        if soma == 3:
            exibirtab()
            print("X ganhou!")
            vez = 10
    soma = 0
    if vez >=10:
        break
    if vez == 9:
        for i in range(3):
            for j in range(3):
                if velha[i][j] == 'X' or velha[i][j] == 'O':
                    vez += 2
        if vez > 16:
            print("DEU VELHA!")
            exibirtab()
            break
    #fimverific
    else:
        exibirtab()
        linha, coluna = map(int, input("Digite o valor da linha e da coluna: ").split())
        while velha[linha][coluna] == 'X' or velha[linha][coluna] == 'O':
            print("Está posição ja está ocupada, tente outra!")
            linha, coluna = map(int, input("Digite o valor da linha e da coluna: ").split())
        velha[linha][coluna] = "O"
        vez+=1
        print()

        for i in range(3):
            for j in range(3):
                if velha[i][j] == 'O':
                    soma += 1
                if soma == 3:
                    exibirtab()
                    print("O ganhou!")
                    vez = 10
            soma = 0
        if vez >= 10:
            break

        for i in range(3):
            for j in range(3):
                if velha[j][i] == 'O':
                    soma += 1
                if soma == 3:
                    exibirtab()
                    print("O ganhou!")
                    vez = 10
            soma = 0
        if vez >=10:
            break
        soma = 0

        for i in range(3):
            if velha[i][i] == 'O':
                soma += 1
            if soma == 3:
                exibirtab()
                print("O ganhou!")
                vez = 10
        soma = 0
        if vez >=10:
            break
        soma = 0
        
        for i in range(3):
            if velha[i][2-i] == 'X':
                soma += 1
            if soma == 3:
                exibirtab()
                print("X ganhou!")
                vez = 10
        soma = 0
        if vez >=10:
            break
        #fimverific
