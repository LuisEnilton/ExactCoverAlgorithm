def solve_brute_force(F):
    X = set.union(*F.values())
    solutions = []

    def is_solution(subset):
        covered_elements = set()
        for subs in subset:
            for element in subs:
                # Verifica se algum elemento já está na cobertura
                if element in covered_elements:
                    return False
                covered_elements.add(element)
        return covered_elements == X

    m = len(F)
    for mask in range(1 << m):
        # Cria um subconjunto de F a partir da máscara
        subset = [F[key] for i, key in enumerate(F) if mask & (1 << i)]
        itens = tuple([key for i, key in enumerate(F) if mask & (1 << i)])
        # Verifica se o subconjunto é uma solução
        if is_solution(subset):
            solutions.append(itens)

    return solutions