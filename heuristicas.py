# heuristics.py — as 4 heurísticas do trabalho

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Posição goal de cada peça: peça N está no índice GOAL.index(N)
GOAL_POS = {v: (i // 3, i % 3) for i, v in enumerate(GOAL) if v != 0}


# ------------------------------------------------------------------
# 1. zero — Custo Uniforme
# h sempre retorna 0: sem heurística, vira Dijkstra/BFS por custo.
# Garante solução ótima mas explora muito mais nodos.
# ------------------------------------------------------------------
def zero(state):
    return 0


# ------------------------------------------------------------------
# 2. inadmissible — heurística NÃO admissível
# Peças fora do lugar × 3.
# Superestima o custo real → pode encontrar caminhos não ótimos,
# mas tende a ser mais rápida porque expande menos nodos.
# ------------------------------------------------------------------
def inadmissible(state):
    return sum(
        3 for i, v in enumerate(state)
        if v != 0 and v != GOAL[i]
    )


# ------------------------------------------------------------------
# 3. misplaced — peças fora do lugar (admissível simples)
# Conta quantas peças estão fora da posição goal.
# É admissível porque cada peça precisa de pelo menos 1 movimento.
# Nunca superestima → garante solução ótima.
# ------------------------------------------------------------------
def misplaced(state):
    return sum(
        1 for i, v in enumerate(state)
        if v != 0 and v != GOAL[i]
    )


# ------------------------------------------------------------------
# 4. manhattan — distância de Manhattan (admissível e mais precisa)
# Para cada peça, soma |linha_atual - linha_goal| + |col_atual - col_goal|.
# É admissível porque cada unidade de distância precisa de 1 movimento.
# Mais precisa que misplaced: sabe o QUANTO cada peça está longe,
# não apenas SE está fora do lugar.
# ------------------------------------------------------------------
def manhattan(state):
    total = 0
    for i, v in enumerate(state):
        if v == 0:
            continue
        row, col = i // 3, i % 3
        goal_row, goal_col = GOAL_POS[v]
        total += abs(row - goal_row) + abs(col - goal_col)
    return total