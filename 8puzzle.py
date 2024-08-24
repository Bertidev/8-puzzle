import random
import os


move_count = 0
def clear():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def trocar_horizontal(lista, pos1, pos2):
    lista[pos1], lista[pos2] = lista[pos2], lista[pos1]

def trocar_vertical(mat, linha1, coluna1, linha2, coluna2):
    mat[linha1][coluna1], mat[linha2][coluna2] = mat[linha2][coluna2], mat[linha1][coluna1]

def resolvivel(puzzle):
    def conta_inversoes(puzzle):
        lista_total = [num for row in puzzle for num in row if num != 0]
        inversoes = 0
        for i in range(len(lista_total)):
            for j in range(i + 1, len(lista_total)):
                if lista_total[i] > lista_total[j]:
                    inversoes += 1
        return inversoes

    inversoes = conta_inversoes(puzzle)
    return inversoes % 2 == 0

def gera_matriz_aleatoria():
    numeros = list(range(9))
    random.shuffle(numeros)
    matriz = [numeros[i:i+3] for i in range(0, 9, 3)]
    return matriz

def nao_resolvida():
    matriz_final = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    matriz = gera_matriz_aleatoria()
    
    while not resolvivel(matriz):
        matriz = gera_matriz_aleatoria()

    return matriz

def encontrar_posicao(mat, num):
    for i in range(3):
        for j in range(3):
            if mat[i][j] == num:
                return i, j
    return None, None

def mover_numero(mat, num):
    global move_count
    linha_num, coluna_num = encontrar_posicao(mat, num)
    linha_zero, coluna_zero = encontrar_posicao(mat, 0)
    
    if linha_num is None or coluna_num is None:
        print('Número não encontrado.')
        return
    
    if (abs(linha_zero - linha_num) == 1 and coluna_zero == coluna_num):  #movimento vertical
        trocar_vertical(mat, linha_num, coluna_num, linha_zero, coluna_zero)
        move_count += 1
        clear()
    elif (abs(coluna_zero - coluna_num) == 1 and linha_zero == linha_num):  #movimento horizontal
        trocar_horizontal(mat[linha_num], coluna_num, coluna_zero)
        move_count += 1
        clear()
    else:
        clear()
        print('Movimento não válido.') #remover so ta aqui pra debug
        

#inicializacao
matriz = nao_resolvida()

print('Início')
clear()
while matriz != [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]:
    for linha in matriz:
        print(linha)
    
    num = int(input('Qual número deseja mover? '))
    mover_numero(matriz, num)
    print(f"Total de movimentos: {move_count}\n")


print('Parabéns! Você resolveu o puzzle.')
