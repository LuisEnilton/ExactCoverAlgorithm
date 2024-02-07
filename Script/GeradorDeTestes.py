from Heuristica import *
from bruteforce import *
import random

def generate_instance(num_constraints, num_items):
    instance = {}
    for item in range(1, num_items + 1):
        constraints = set(random.sample(range(1, num_constraints + 1), random.randint(1, num_constraints)))
        instance[item] = constraints
    
    return instance

def main():
    num_constraints = 100
    num_items = 300
    instance = generate_instance(num_constraints, num_items)
    for x in instance:
        print(x, instance[x])
    # Teste Heuristica
    
    constraint_to_pieces = convert(instance)
    #print(constraint_to_pieces)
    print("\nSoluções encontradas:")
    for solution in Heuristica(constraint_to_pieces):
        pass
        print(solution)
    # Teste BruteForce

    print("Instância gerada:")
    for item, constraints in instance.items():
        print(f"Item {item}: {constraints}")

    solutions = solve_brute_force(instance)

    print("\nSoluções encontradas:")
    for solution in solutions:
        print(solution)
        
if __name__ == "__main__":
    main()




