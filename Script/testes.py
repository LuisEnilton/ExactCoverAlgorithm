from GeradorDeTestes import *
from Heuristica import *
from bruteforce import *
import time
from gerartxt import *
def main():
    numero_de_restricoes = 10
    numero_de_itens = 25
    d = generate_instance(numero_de_restricoes, numero_de_itens)
    for x in d:
        print(x, d[x])
    # Teste Heuristica
    constraint_to_pieces = convert(d)
    
    print("\nSoluções encontradas:")
    #Verificar tempo de execução da heuristica
    start = time.perf_counter_ns()
    s = Heuristica(constraint_to_pieces)
    end = time.perf_counter_ns()
    time_heur = end - start
    for solution in s:
        pass
        print(solution)
    # Teste BruteForce
    print("Instância gerada:")
    for item, constraints in d.items():
        print(f"Item {item}: {constraints}")
    start = time.perf_counter_ns()
    solutions = solve_brute_force(d)
    end = time.perf_counter_ns()
    time_brute = end - start
    print("\nSoluções encontradas:")
    for solution in solutions:
        print(solution)
    escrever_txt(numero_de_restricoes, numero_de_itens, time_heur, time_brute)
    
    
    
if(__name__ == "__main__"):
    main()