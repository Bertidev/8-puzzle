import random

def trocar_posicoes(lista, pos1, pos2):
    lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
    return lista

def horizontal(mat):
    for i in range(3):
        for j in range(3):
            if mat[i][j] == 0:
                linha = i
                coluna = j
    num = int(input('Qual número deseja mover?'))  
    for k in range(3):
        if matriz[linha][k] == num:
            coluna_num = k
    if (coluna == 0) and (coluna_num == 1):
        trocar_posicoes(mat[linha], coluna, k) 
    elif (coluna == 2) and (coluna_num == 1):
        trocar_posicoes(mat[linha], coluna, k) 
    

def vertical(mat):
    for i in range(3):
        for j in range(3):
            if mat[i][j] == 0:
                linha = i
                coluna = j
    num = int(input('Qual número deseja mover?'))  
    return matriz

matriz_final = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

numeros = list(range(9))
random.shuffle(numeros)
matriz = [numeros[i:i+3] for i in range(0, 9, 3)]

if matriz == matriz_final:
    numeros = list(range(9))
    random.shuffle(numeros)
    matriz = [numeros[i:i+3] for i in range(0, 9, 3)]

print('Inicio')

while matriz != matriz_final:
    for j in range(3):
        print(matriz[j])
    entrada = input('Deseja mover na vertical(v) ou horizontal(h)?')
    if entrada == 'h':
        horizontal(matriz)
    else:
        vertical(matriz)