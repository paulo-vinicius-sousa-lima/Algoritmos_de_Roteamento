# ================================================== 
# SIMULACAO DE REDE DE COMPUTADORES 
# ALGORITMO DE DIJKSTRA 
# ================================================== 
 
import heapq 
 
# Identificacao dos roteadores 
roteadores = ["A", "B", "C", "D", "E"] 
 
# Criacao da topologia da rede 
# Cada enlace possui um custo de transmissao. 
# As conexoes sao bidirecionais. 
 
rede = { 
    "A": {"B": 2, "C": 5, "E": 10}, 
    "B": {"A": 2, "C": 1, "D": 4}, 
    "C": {"A": 5, "B": 1, "D": 2, "E": 5}, 
    "D": {"B": 4, "C": 2, "E": 1}, 
    "E": {"A": 10, "C": 5, "D": 1} 
} 
 
 
# Funcao que executa o algoritmo de Dijkstra 
def dijkstra(origem): 
 
    # Inicializa todas as distancias com infinito 
    distancia = { 
        roteador: float("inf") 
        for roteador in roteadores 
    } 
 
    # O custo para chegar a origem e zero 
    distancia[origem] = 0 
 
    # Guarda o proximo salto de cada destino 
    proximo_salto = { 
        roteador: None 
        for roteador in roteadores 
    } 
 
    # Fila de prioridade: (custo, roteador) 
    fila = [(0, origem)] 
 
    # Enquanto existirem roteadores para analisar 
    while fila: 
 
        # Retira o roteador de menor custo 
        custo_atual, atual = heapq.heappop(fila) 
 
        # Ignora caminhos que ja foram superados 
        if custo_atual > distancia[atual]: 
            continue 
 
        # Percorre os vizinhos do roteador atual 
        for vizinho, custo_enlace in rede[atual].items(): 
 
            # Calcula o custo total do novo caminho 
            novo_custo = custo_atual + custo_enlace 
 
            # Verifica se o novo caminho e mais barato 
            if novo_custo < distancia[vizinho]: 
 
                # Atualiza a distancia minima 
                distancia[vizinho] = novo_custo 
 
                # Se estiver saindo da origem, o primeiro 
                # salto sera o proprio vizinho. 
                # Caso contrario, conserva o primeiro salto. 
                if atual == origem: 
                    proximo_salto[vizinho] = vizinho 
                else: 
                    proximo_salto[vizinho] = proximo_salto[atual] 
 
                # Insere o novo caminho na fila 
                heapq.heappush( 
                    fila, 
                    (novo_custo, vizinho) 
                ) 
 
    return distancia, proximo_salto 
 
 
# ================================================== 
# EXECUCAO PARA TODOS OS ROTEADORES 
# ================================================== 
 
print("=" * 55) 
print(" SIMULACAO DE ROTEAMENTO - ALGORITMO DE DIJKSTRA") 
print("=" * 55) 
 
# Calcula as rotas de cada roteador 
for origem in roteadores: 
 
    distancia, proximo_salto = dijkstra(origem) 
 
    print(f"\nTABELA DE ROTEAMENTO - ROTEADOR {origem}") 
    print("-" * 45) 
    print("Destino | Custo | Proximo Salto") 
    print("-" * 45) 
 
    for destino in roteadores: 
 
        custo = distancia[destino] 
        salto = proximo_salto[destino] 
 
        # Formata o custo para exibicao 
        if custo == float("inf"): 
            custo_texto = "Infinito" 
        else: 
            custo_texto = str(custo) 
 
        # A origem nao precisa de proximo salto 
        if origem == destino: 
            salto_texto = "-" 
        elif salto is None: 
            salto_texto = "Indisponivel" 
        else: 
            salto_texto = salto 
 
        print( 
            f"   {destino}    | " 
            f"{custo_texto:7} | " 
            f"{salto_texto}" 
        ) 
 
print("\nSimulacao finalizada com sucesso!")