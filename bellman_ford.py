# Simulação do algoritmo de Bellman-Ford 
# Aplicação em uma rede de computadores com 5 roteadores. 
 
# Identificação dos roteadores 
roteadores = ["A", "B", "C", "D", "E"] 
 
# Enlaces da rede e seus respectivos custos. 
# Cada conexão é bidirecional, por isso são criadas 
# duas arestas: uma de ida e outra de volta. 
 
conexoes = [ 
    ("A", "B", 2), 
    ("A", "C", 5), 
    ("A", "E", 10), 
    ("B", "C", 1), 
    ("B", "D", 4), 
    ("C", "D", 2), 
    ("C", "E", 5), 
    ("D", "E", 1) 
] 
 
# Criação da lista de arestas direcionadas 
arestas = [] 
 
for origem, destino, custo in conexoes: 
    arestas.append((origem, destino, custo)) 
    arestas.append((destino, origem, custo)) 
 
 
# Algoritmo de Bellman-Ford 
def bellman_ford(origem): 
 
    # Inicialmente, todos os destinos têm custo infinito 
    distancia = {r: float("inf") for r in roteadores} 
 
    # O custo para chegar ao próprio roteador é zero 
    distancia[origem] = 0 
 
    # Guarda o próximo salto para cada destino 
    proximo_salto = {r: None for r in roteadores} 
 
    # Executa V-1 iterações de relaxamento 
    for i in range(len(roteadores) - 1): 
 
        alterou = False 
 
        # Analisa todas as conexões da rede 
        for u, v, custo in arestas: 
 
            # Verifica se existe um caminho mais barato 
            if distancia[u] != float("inf"): 
 
                novo_custo = distancia[u] + custo 
 
                if novo_custo < distancia[v]: 
 
                    distancia[v] = novo_custo 
 
                    # Registra o primeiro roteador 
                    # utilizado para alcançar o destino 
                    if u == origem: 
                        proximo_salto[v] = v 
                    else: 
                        proximo_salto[v] = proximo_salto[u] 
 
                    alterou = True 
 
        # Interrompe se nenhuma rota foi modificada 
        if not alterou: 
            break 
 
    # Verifica a existência de ciclos negativos 
    for u, v, custo in arestas: 
        if distancia[u] != float("inf"): 
            if distancia[u] + custo < distancia[v]: 
                raise ValueError("Ciclo de custo negativo encontrado!") 
 
    return distancia, proximo_salto 
 
 
# Exibe os resultados para todos os roteadores 
print("=" * 60) 
print("SIMULACAO DE ROTEAMENTO - BELLMAN-FORD") 
print("=" * 60) 
 
for origem in roteadores: 
 
    distancia, proximo_salto = bellman_ford(origem) 
 
    print(f"\nTABELA DE ROTEAMENTO DO ROTEADOR {origem}") 
    print("-" * 45) 
    print("Destino | Custo | Proximo salto") 
    print("-" * 45) 
 
    for destino in roteadores: 
 
        custo = distancia[destino] 
        salto = proximo_salto[destino] 
 
        if custo == float("inf"): 
            custo_texto = "Infinito" 
        else: 
            custo_texto = str(custo) 
 
        if origem == destino: 
            salto_texto = "-" 
        elif salto is None: 
            salto_texto = "Indisponivel" 
        else: 
            salto_texto = salto 
 
        print(f"   {destino}    | {custo_texto:7} | {salto_texto}") 
 
print("\nSimulacao finalizada com sucesso!")