Goal = (1,2,3,4,5,6,7,8,0)

def get_vizinhos(state):
    i = state.index(0)
    row, col = i // 3, i% 3
    vizinhos = []

    for delta_row, delta_col, move in [(-1,0,'cima'),(1,0,'baixo'),(0,-1,'esq'),(0,1,'dir')]:
        new_row, new_col = row