#representação do estado e movimentos

goal = (1,2,3,4,5,6,7,8,0)

# ------------------------------------------------------------------
# get_vizinhos
# Dado um estado, retorna todos os estados alcançáveis em 1 movimento.
# Cada vizinho é uma tupla (novo_estado, direção_do_movimento).
#
# Lógica:
#   1. new_col Encontra o índice do vazio (0) na tupla
#   2. Converte índice → (linha, coluna)
#   3. Para cada direção (cima/baixo/esq/dir), calcula a célula vizinha
#   4. Se a célula existe no tabuleiro, troca vazio com ela
# ------------------------------------------------------------------

def get_vizinhos(state):
    i = state.index(0)
    row, col = i // 3, i% 3

    direcoes = [
        (-1,  0, 'cima'),
        ( 1,  0, 'baixo'),
        ( 0, -1, 'esquerda'),
        ( 0,  1, 'direita'),
    ]

    vizinhos = []

    for delta_row, delta_col, move in direcoes:
        new_row, new_col = row + delta_row , col + delta_col
        
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            j = new_row*3 + new_col
            # Troca vazio com peça vizinha
            new_state = list(state)
            new_state[i], new_state[j] = new_state[j], new_state[i]
            vizinhos.append((tuple(new_state), move))
    
    return vizinhos

# ------------------------------------------------------------------
# is_goal
# Verifica se o estado atual é a solução.
# Simples comparação de tuplas — O(n).
# ------------------------------------------------------------------

def is_goal(state):
    return state == goal

# ------------------------------------------------------------------
# is_solvable
# Nem todo tabuleiro embaralhado tem solução.
# A regra: conta o número de inversões (par de peças fora de ordem).
# Se o total for PAR → tem solução. Ímpar → não tem.
#
# Exemplo de inversão: 3 antes do 1 = 1 inversão (3 > 1).
# ------------------------------------------------------------------
def is_solvable(state):
    tiles = [x for x in state if x != 0]  # ignora o vazio
    inversions = sum(
        1 for i in range(len(tiles))
          for j in range(i + 1, len(tiles))
          if tiles[i] > tiles[j]
    )
    return inversions % 2 == 0


# ------------------------------------------------------------------
# print_board
# Exibe o tabuleiro formatado no terminal. Apenas para debug.
# ------------------------------------------------------------------
def print_board(state):
    for i in range(9):
        val = state[i] if state[i] != 0 else '_'
        end = '\n' if (i + 1) % 3 == 0 else ' '
        print(val, end=end)
    print()

