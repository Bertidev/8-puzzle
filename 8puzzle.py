import random
import os
from collections import deque
import heapq

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
    linha_num, coluna_num = encontrar_posicao(mat, num)
    linha_zero, coluna_zero = encontrar_posicao(mat, 0)
    
    if linha_num is None or coluna_num is None:
        print('Número não encontrado.')
        return
    
    if (abs(linha_zero - linha_num) == 1 and coluna_zero == coluna_num):  #movimento vertical
        trocar_vertical(mat, linha_num, coluna_num, linha_zero, coluna_zero)
        clear()
    elif (abs(coluna_zero - coluna_num) == 1 and linha_zero == linha_num):  #movimento horizontal
        trocar_horizontal(mat[linha_num], coluna_num, coluna_zero)
        clear()
    else:
        clear()
        print('Movimento não válido.')



def encontrar_zero(matriz):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == 0:
                return i, j
    return None, None

def expande_estado(matriz):
    linha_zero, coluna_zero = encontrar_zero(matriz)
    estados = []

    movimentos = [
        (-1, 0),  # cima
        (1, 0),   # baixo
        (0, -1),  # esquerda
        (0, 1)    # direita
    ]
    
    for mov in movimentos:
        nova_linha = linha_zero + mov[0]
        nova_coluna = coluna_zero + mov[1]

        if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
            nova_matriz = [linha[:] for linha in matriz]
            trocar_vertical(nova_matriz, linha_zero, coluna_zero, nova_linha, nova_coluna)
            estados.append(nova_matriz)
    
    return estados

def estado_final(matriz):
    return matriz == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

def heuristica(matriz):
    distancia = 0
    posicoes_finais = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 0: (2, 2)
    }
    
    for i in range(3):
        for j in range(3):
            numero = matriz[i][j]
            pos_final = posicoes_finais[numero]
            distancia += abs(i - pos_final[0]) + abs(j - pos_final[1])
    
    return distancia

def reconstruir_caminho(estado_final, pais):
    caminho = []
    atual = str(estado_final)
    while atual is not None:
        caminho.append(eval(atual))
        atual = pais[atual]
    caminho.reverse()
    return caminho

def imprimir_caminho(caminho):
    print("\nSolução encontrada! Caminho:")
    for passo, estado in enumerate(caminho):
        print(f"Passo {passo}:")
        for linha in estado:
            print(linha)
        print()

# largura
def largura(inicial):
    fila = deque([(inicial, None)])  
    encontrados = set()
    encontrados.add(str(inicial))
    pais = {str(inicial): None}
    estados_encontrados = 0

    while fila:
        atual, pai = fila.popleft()
        estados_encontrados += 1

        if estado_final(atual):
            caminho = reconstruir_caminho(atual, pais)
            imprimir_caminho(caminho)
            print(f"Solução encontrada em {estados_encontrados} estados encontrados!")
            return atual
        
        for estado in expande_estado(atual):
            if str(estado) not in encontrados:
                fila.append((estado, atual))
                encontrados.add(str(estado))
                pais[str(estado)] = str(atual)

    print("Sem solução.")

# Profundidade
def profundidade(inicial):
    pilha = [(inicial, None)]  
    encontrados = set()
    encontrados.add(str(inicial))
    pais = {str(inicial): None}
    estados_encontrados = 0

    while pilha:
        atual, pai = pilha.pop()
        estados_encontrados += 1

        if estado_final(atual):
            caminho = reconstruir_caminho(atual, pais)
            imprimir_caminho(caminho)
            print(f"Solução encontrada em {estados_encontrados} estados encontrados!")
            return atual
        
        for estado in expande_estado(atual):
            if str(estado) not in encontrados:
                pilha.append((estado, atual))
                encontrados.add(str(estado))
                pais[str(estado)] = str(atual)

    print("Sem solução.")

# A*
def a(inicial):
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (heuristica(inicial), inicial, None))
    encontrados = set()
    encontrados.add(str(inicial))
    pais = {str(inicial): None}
    estados_encontrados = 0

    while fila_prioridade:
        _, atual, pai = heapq.heappop(fila_prioridade)
        estados_encontrados += 1

        if estado_final(atual):
            caminho = reconstruir_caminho(atual, pais)
            imprimir_caminho(caminho)
            print(f"Solução encontrada em {estados_encontrados} estados encontrados!")
            return atual
        
        for estado in expande_estado(atual):
            if str(estado) not in encontrados:
                heapq.heappush(fila_prioridade, (heuristica(estado), estado, atual))
                encontrados.add(str(estado))
                pais[str(estado)] = str(atual)

    print("Sem solução.")
4

def escolha_modo():
    print("Escolha o modo de jogo:")
    print("1 - Jogar manualmente")
    print("2 - Resolver com Busca em Largura")
    print("3 - Resolver com Busca em Profundidade")
    print("4 - Resolver com A*")

    escolha = int(input("Digite o número da sua escolha: "))
    
    if escolha == 1:
        jogar_manual()
    elif escolha == 2:
        largura(matriz)
    elif escolha == 3:
        profundidade(matriz)
    elif escolha == 4:
        a(matriz)
    else:
        print("Escolha inválida!")


def jogar_manual():
    while matriz != [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]:
        for linha in matriz:
            print(linha)
        
        num = int(input('Qual número deseja mover? '))
        mover_numero(matriz, num)

    print('Parabéns! Você resolveu o puzzle.')


matriz = nao_resolvida()
escolha_modo()
