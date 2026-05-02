# main.py — entrada do usuário e orquestração dos algoritmos

from puzzle import is_solvable, print_tabuleiro
from search import astar, print_result
from heuristicas import zero, inadmissible, misplaced, manhattan


# ------------------------------------------------------------------
# read_board
# Lê o tabuleiro digitado pelo usuário.
# O usuário digita 9 números separados por espaço, ex: 1 2 3 4 0 6 7 5 8
# O 0 representa o espaço vazio.
# ------------------------------------------------------------------
def read_board():
    print("Digite os 9 números do tabuleiro separados por espaço.")
    print("Use 0 para o espaço vazio. Ex: 1 2 3 4 0 6 7 5 8\n")

    while True:
        try:
            nums = list(map(int, input("Tabuleiro: ").split()))

            if len(nums) != 9:
                print("  ✗ Digite exatamente 9 números.\n")
                continue

            if sorted(nums) != list(range(9)):
                print("  ✗ Use os números de 0 a 8, sem repetição.\n")
                continue

            return tuple(nums)

        except ValueError:
            print("  ✗ Digite apenas números inteiros.\n")


# ------------------------------------------------------------------
# choose_algorithm
# Menu simples para o usuário escolher qual algoritmo rodar.
# ------------------------------------------------------------------
def choose_algorithm():
    print("\nEscolha o algoritmo:")
    print("  1 - Custo Uniforme (sem heurística)")
    print("  2 - A* heurística NÃO admissível (misplaced × 3)")
    print("  3 - A* heurística admissível simples (misplaced)")
    print("  4 - A* heurística admissível precisa (Manhattan)")
    print("  5 - Rodar TODOS e comparar")

    while True:
        choice = input("\nOpção: ").strip()
        if choice in ('1','2','3','4','5'):
            return choice
        print("  ✗ Digite um número de 1 a 5.")

 
# ------------------------------------------------------------------
# run
# Junta tudo: lê o tabuleiro, valida, escolhe algoritmo e exibe resultado.
# ------------------------------------------------------------------
def run():
    print("=" * 45)
    print("         8-PUZZLE — Busca A*")
    print("=" * 45)

    state = read_board()

    print("\nTabuleiro lido:")
    print_tabuleiro(state)

    if not is_solvable(state):
        print("✗ Este tabuleiro NÃO tem solução (número de inversões ímpar).")
        return

    print("✓ Tabuleiro solucionável!\n")

    algorithms = {
        '1': (zero,         "Custo Uniforme"),
        '2': (inadmissible, "A* NÃO admissível"),
        '3': (misplaced,    "A* admissível simples (misplaced)"),
        '4': (manhattan,    "A* admissível precisa (Manhattan)"),
    }

    choice = choose_algorithm()

    if choice == '5':
        for key in ('1','2','3','4'):
            heuristic, name = algorithms[key]
            result = astar(state, heuristic)
            print_result(result, name)
    else:
        heuristic, name = algorithms[choice]
        result = astar(state, heuristic)
        print_result(result, name)

    print("\nArquivo output.json gerado com fronteira e visitados.")


if __name__ == '__main__':
    run()