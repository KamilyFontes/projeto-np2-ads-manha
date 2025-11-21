graph = {"Clara": ["Carlos", "Daniela"], 
         "Carlos": ["Daniela","Clara", "Mauro"], 
         "Daniela": ["Clara", "Carlos", "Mauro"], "Mauro": ["Carlos", "Daniela"]}

def connected(graph, a, b): # 'a' = nó/vértice onde começa, 'b' = nó/vértice que queremos *alcançar*
    

    if a not in graph:
        raise ValueError(f"{a} não existe no grafo.") # "raise" = para o código

    if b not in graph:
        raise ValueError(f"{b} não existe no grafo.")
    
    if a == b:
        return True # se são os mesmos valores, é desnecessário contiuar
    
    if b in graph[a]: # se b está na lista de amigos de a
        return True
    
    else:
        print(f"{a} e {b} não estão ligados diretamente.")
    
    # bfs (Busca em Largura); conecta a todos e verifica liga de forma DIRETA OU INDIRETA
    fila_visitas = [a]
    descobertos = [a]

    while fila_visitas:
        u = fila_visitas.pop(0)

        if u == b:
            return True
        
        for v in graph[u]:
            if v not in descobertos:
                descobertos.append(v) 
                fila_visitas.append(v)
    return False