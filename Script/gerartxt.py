# Formato do txt
# Em cada linha
# Numero de restrições,numero de itens,tempo de execução da heuristica,tempo de execução do brute force
def escrever_txt(numero_de_restricoes, numero_de_itens, tempo_de_execucao_heuristica, tempo_de_execucao_brute_force):
    with open("resultados.txt", "a") as file:
        file.write(f"{numero_de_restricoes},{numero_de_itens},{tempo_de_execucao_heuristica},{tempo_de_execucao_brute_force}\n")
    return