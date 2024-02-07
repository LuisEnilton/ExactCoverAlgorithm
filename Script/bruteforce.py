import Professor
import EstruturaDeHorarios


def exact_cover_bruteforce(X, F):
    ret = []
    """
    Resolve o problema da cobertura exata usando força bruta.

    Parâmetros:
    - X: Conjunto de elementos a serem cobertos (Estrutura de Horários).
    - F: Conjunto de conjuntos, onde cada conjunto é um subconjunto de X 
        (Cada subconjunto são os horários de um respectivo professor).
    Retorna:
    - Uma lista de conjuntos(Horários de Professores) que forma uma cobertura exata, ou None se não houver solução.
    Especificação:
        -O algoritmo testa todas as combinações possíveis de subconjuntos de F, e verifica se alguma delas é uma solução.
        -A quantidade de combinações possíveis é 2^n, onde n é a quantidade de subconjuntos de F.
    """
    n = len(F)
    m = len(X)
    def is_solution(subset):
        covered_elements = set()
        for subs in subset:
            # Verifica se algum elemento já está na cobertura
            if any(element in covered_elements for element in subs):
                return False
            covered_elements.update(subs)
        return covered_elements == set(X)
    
    
    for mask in range(1 << m):
        # Cria um subconjunto de F a partir da mascara
        subset = [F[i] for i in range(m) if mask & (1 << i)]
        # Verifica se o subconjunto é uma solução
        if is_solution(subset):
            return subset
    return None
    
def main():
    a = [x for x in range(1, 40)]
    c = [[x for x in range(1, 40)], [x for x in range(21, 40)],[x for x in range(1,21)]]
    b = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18],
        [19, 20],
        [1, 4, 7, 10, 13, 16, 19],
        [2, 5, 8, 11, 14, 17, 20],
        [3, 6, 9, 12, 15, 18, 19],
        [3, 6, 9, 12, 15, 17, 20],
        [1, 4, 7, 10, 13, 16, 18],
        [2, 5, 8, 11, 14, 16, 19],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        [19, 20],
        [1, 4, 7, 10, 13, 16, 18, 19],
        [2, 5, 8, 11, 14, 17, 20, 19],
        [3, 6, 9, 12, 15, 18, 20, 19],
        [21, 22, 23],
        [24, 25, 26],
        [27, 28, 29],
        [30, 31, 32],
        [33, 34, 35],
        [36, 37, 38],
        [39, 40],
        [21, 24, 27, 30, 33, 36, 39],
        [22, 25, 28, 31, 34, 37, 40],
        [23, 26, 29, 32, 35, 38, 39],
        [23, 26, 29, 32, 35, 37, 40],
        [21, 24, 27, 30, 33, 36, 38],
        [22, 25, 28, 31, 34, 36, 39],
        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
        [39, 40],
        [21, 24, 27, 30, 33, 36, 38, 39],
        [22, 25, 28, 31, 34, 36, 37, 40],
        [21, 24, 27, 30, 33, 36, 37, 38],
        [22, 25, 28, 31, 34, 36, 37, 38],
        [39, 40],
        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]]
    ans =exact_cover_bruteforce(a, c)
    print(ans)
             

if __name__ == "__main__":
    main()