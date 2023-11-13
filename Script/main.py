import Professor

def exact_cover_bruteforce(X, F):
    """
    Resolve o problema da cobertura exata usando força bruta.

    Parâmetros:
    - X: Conjunto de elementos a serem cobertos.
    - F: Conjunto de conjuntos, onde cada conjunto é um subconjunto de X.

    Retorna:
    - Uma lista de conjuntos que forma uma cobertura exata, ou None se não houver solução.
    """
    n = len(X)
    m = len(F)

    def is_solution(solution):
        covered_elements = set()
        for subset in solution:
            # Verifica se algum elemento já está na cobertura
            if any(element in covered_elements for element in subset):
                return False
            covered_elements.update(subset)
        return covered_elements == set(X)

    def backtrack(index, current_solution):
        if index == m:
            if is_solution(current_solution):
                return current_solution
            return None

        # Inclui o conjunto atual na solução
        with_current = current_solution + [F[index]]
        result_with_current = backtrack(index + 1, with_current)
        if result_with_current:
            return result_with_current

        # Exclui o conjunto atual da solução
        without_current = current_solution
        result_without_current = backtrack(index + 1, without_current)
        if result_without_current:
            return result_without_current

        return None

    return backtrack(0, [])

# Exemplo de uso:
    #Lista de horários possiveis
X = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),]
    #Lista de professores
F = [[(1, 1), (1, 2)], [(1, 3), (1, 4)], [(1, 5)]]
    
result = exact_cover_bruteforce(X, F)

if result:
    for i,professor in enumerate(result):
        print(f'Professor {i+1}')
        for classe in professor:
            print(f'Aula no dia {classe[0]} no horário {classe[1]}')
else:
    print("Nenhuma solução encontrada.")
