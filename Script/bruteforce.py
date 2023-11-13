import Professor
import EstruturaDeHorarios


def exact_cover_bruteforce(X, F):
    ret = []
    """
    Resolve o problema da cobertura exata usando força bruta.

    Parâmetros:
    - X: Conjunto de elementos a serem cobertos.
    - F: Conjunto de conjuntos, onde cada conjunto é um subconjunto de X.

    Retorna:
    - Uma lista de conjuntos que forma uma cobertura exata, ou None se não houver solução.
    
    Especificação:
    - Essa solução por meio de força bruta é muito ineficiente, pois a complexidade é O(2^n).
    - Ela funciona testando cada subconjunto de F, e verificando se ele é uma solução.
    - Para isso, utilizaremos uma mascara binária para representar cada subconjunto de F.
    - Por exemplo, se F = [[1, 2], [2, 3], [1, 3]], então a mascara 010 representa o subconjunto [2, 3].
    - A mascara 101 representa o subconjunto [1, 3].
    - A mascara 111 representa o subconjunto [1, 2, 3].
    - A mascara 000 representa o subconjunto vazio.
    """
    n = len(F)
    m = len(X)
    def is_solution(subset):
        covered_elements = set()
        for subset in subset:
            # Verifica se algum elemento já está na cobertura
            if any(element in covered_elements for element in subset.classes):
                return False
            covered_elements.update(subset.classes)
        return covered_elements == set(X)
    
    
    for mask in range(1 << m):
        # Cria um subconjunto de F a partir da mascara
        subset = [F[i] for i in range(m) if mask & (1 << i)]
        # Verifica se o subconjunto é uma solução
        if is_solution(subset):
            return subset
    return None
    
def main():
        X = []
        F = []

        while True:
            print("\nEscolha uma opção:")
            print("1. Criar estrutura de horários")
            print("2. Inserir professor")
            print("3. Mostrar solução")
            print("4. Sair")

            opcao = input("Digite o número da opção desejada: ")

            if opcao == "1":
                dias = input("Digite os dias da semana (ex: 1,2,3): ")
                dias = [int(dia) for dia in dias.split(',')]
                horarios = input("Digite os horários disponíveis no formato (inicio,final): ").split(',')
                horarios = tuple(map(int, horarios))
                print(horarios)
                eh1 = EstruturaDeHorarios.EstruturaDeHorarios(dias, horarios)
                X = eh1.horarios
                print("Estrutura de horários criada com sucesso!")

            elif opcao == "2":
                nome = input("Digite o nome do professor: ")
                disponibilidade = input("Digite a disponibilidade do professor (dia,horário): ")
                disponibilidade = [tuple(map(int, intervalo.split(','))) for intervalo in disponibilidade.split()]
                professor = Professor.Professor(nome, disponibilidade)
                F.append(professor)
                print(f"Professor {nome} inserido com sucesso!")

            elif opcao == "3":
                result = exact_cover_bruteforce(X, F)
                if result:
                    for i, professor in enumerate(result):
                        print(f'\nProfessor {professor.name}, o salário é {professor.salary}')
                        for classe in professor.classes:
                            print(f'Aula do professor no dia {classe[0]} no horário {classe[1]}')
                else:
                    print("Nenhuma solução encontrada.")

            elif opcao == "4":
                print("Saindo...")
                break

            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()