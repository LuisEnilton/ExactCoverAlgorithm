import Professor
import EstruturaDeHorarios

def contar_bits_1(n):
    # Converte o número para uma representação binária e remove o prefixo '0b'
    binario = bin(n)[2:]
    
    # Conta a quantidade de bits 1
    quantidade_bits_um = binario.count('1')
    
    return quantidade_bits_um

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
    - Essa solução por meio de força bruta é muito ineficiente, pois a complexidade é O(2^m).
    - Ela funciona testando cada subconjunto de F, e verificando se ele é uma solução.
    - Para isso, utilizaremos uma mascara binária para representar cada subconjunto de F.
    - Por exemplo, se F = [[1, 2], [2, 3], [1, 3]], então a mascara 010 representa o subconjunto [2, 3].
    - A mascara 101 representa o subconjunto [1, 3].
    - A mascara 111 representa o subconjunto [1, 2, 3].
    - A mascara 000 representa o subconjunto vazio.
    """
    n = len(X)
    m = len(F)
    #cnt é um inteiro e começa com infinito
    cnt = 100000000000000
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
            qtd = contar_bits_1(mask)
            if(cnt > qtd):
                cnt = qtd
                ret = subset
    return ret
 # Exemplo de uso:
    #Lista de horários possiveis
Professor1 = Professor.Professor('João', 30, 1000, [(1, 1), (1, 2)])
dias = [1]
horarios = (1,5)
eh1 = EstruturaDeHorarios.EstruturaDeHorarios(dias,horarios)
X = eh1.horarios
    #Lista de professores
p1 = Professor.Professor('João', 30, 1000, [(1, 1), (1, 2)])
p2 = Professor.Professor('Maria', 30, 1000, [(1, 3), (1, 4)])
p3 = Professor.Professor('José', 30, 1000, [(1, 5)])
F = [p1,p2,p3]
    
result = exact_cover_bruteforce(X, F)

if result:
    for i,professor in enumerate(result):
        print(f'Professor {professor.name} , o salário é {professor.salary}')
        for classe in professor.classes:
            print(f'Aula  do professor  no dia {classe[0]} no horário {classe[1]}')
else:
    print("Nenhuma solução encontrada.")   