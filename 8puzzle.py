import random

def trocar_posicoes(lista, pos1, pos2):
    lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
    return lista

def is_solvable(puzzle):
    def count_inversions(puzzle):
        one_d_puzzle = [num for row in puzzle for num in row if num != 0]
        inversions = 0
        for i in range(len(one_d_puzzle)):
            for j in range(i + 1, len(one_d_puzzle)):
                if one_d_puzzle[i] > one_d_puzzle[j]:
                    inversions += 1
        return inversions

    inversions = count_inversions(puzzle)
    return inversions % 2 == 0

def gera_matriz_aleatoria():
    numeros = list(range(9))
    random.shuffle(numeros)
    matriz = [numeros[i:i+3] for i in range(0, 9, 3)]
    return matriz

def verifica():
    matriz_final = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    matriz = gera_matriz_aleatoria()
    
    while not is_solvable(matriz):
        matriz = gera_matriz_aleatoria()

    return matriz

def horizontal(mat):
    for i in range(3):
        for j in range(3):
            if mat[i][j] == 0:
                linha = i
                coluna = j
    num = int(input('Qual número deseja mover?'))  
    coluna_num = -1            
    for k in range(3):
        if mat[linha][k] == num:
            coluna_num = k
    
    if coluna_num == -1:
        print('Número não encontrado na mesma linha.')
        return
    
    if abs(coluna - coluna_num) == 1:
        trocar_posicoes(mat[linha], coluna, coluna_num)
    else:
        print('Movimento horizontal não válido.')

def vertical(mat):
    for i in range(3):
        for j in range(3):
            if mat[i][j] == 0:
                linha = i
                coluna = j
    num = int(input('Qual número deseja mover?'))  
    linha_num = -1
    for k in range(3):
        if mat[k][coluna] == num:
            linha_num = k
    
    if linha_num == -1:
        print('Número não encontrado na mesma coluna.')
        return
    
    if abs(linha - linha_num) == 1:
        mat[linha][coluna], mat[linha_num][coluna] = mat[linha_num][coluna], mat[linha][coluna]
    else:
        print('Movimento vertical não válido.')

# Inicialização
matriz = verifica()

print('Início')

while matriz != [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]:
    for linha in matriz:
        print(linha)
    
    entrada = input('Deseja mover na vertical(v) ou horizontal(h)? ')
    if entrada == 'h':
        horizontal(matriz)
    elif entrada == 'v':
        vertical(matriz)
    else:
        print('Entrada inválida. Por favor, escolha "v" ou "h".')

print('Parabéns! Você resolveu o puzzle.')
