import heapq
import time
import json
from puzzle import get_vizinhos, is_goal

def astar(start, heuristic):
    start_time = time.time()
 
    # (f, g, estado)
    open_list = [(heuristic(start), 0, start)]
 
    came_from = {start: None}       # estado → (pai, movimento)
    g_score   = {start: 0}          # estado → custo acumulado
 
    visited = {}                    # estados expandidos (fechados)
    max_frontier = 0                # maior tamanho da fronteira
 
    while open_list:
        max_frontier = max(max_frontier, len(open_list))
 
        f, g, state = heapq.heappop(open_list)
 
        # Ignora se já encontramos um caminho melhor para este estado
        if state in visited and g_score.get(state, float('inf')) < g:
            continue
 
        visited[state] = g
 
        if is_goal(state):
            elapsed = time.time() - start_time
            path = reconstruct_path(came_from, state)
 
            # Salva fronteira e visitados em arquivo
            save_output(open_list, visited)
 
            return {
                'path':         path,
                'path_length':  len(path),
                'visited':      len(visited),
                'time':         round(elapsed, 4),
                'max_frontier': max_frontier,
            }
 
        # Expande os vizinhos
        for neighbor, move in get_vizinhos(state):
            new_g = g + 1
            if new_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor]   = new_g
                came_from[neighbor] = (state, move)
                new_f = new_g + heuristic(neighbor)
                heapq.heappush(open_list, (new_f, new_g, neighbor))
 
    return None  # sem solução

def save_output(open_list, visited):
    data = {
        'frontier': [list(item) for item in open_list],
        'visited':  [list(s) for s in visited.keys()],
    }
    with open('output.json', 'w') as f:
        json.dump(data, f, indent=2)

# ------------------------------------------------------------------
# print_result
# Exibe as métricas do enunciado no terminal.
# ------------------------------------------------------------------
def print_result(result, algorithm_name):
    if result is None:
        print("Sem solução.")
        return
    print(f"\n=== {algorithm_name} ===")
    print(f"Caminho:          {' → '.join(result['path'])}")
    print(f"Tamanho caminho:  {result['path_length']}")
    print(f"Nodos visitados:  {result['visited']}")
    print(f"Tempo:            {result['time']}s")
    print(f"Maior fronteira:  {result['max_frontier']}")

def reconstruct_path(came_from, goal_state):
    path = []
    state = goal_state
    while came_from[state] is not None:
        parent, move = came_from[state]
        path.append(move)
        state = parent
    path.reverse()
    return path