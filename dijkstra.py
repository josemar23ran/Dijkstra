import heapq
def dijkstra(graph, inicio, destino):
    distancias = {estacion: float('inf') for estacion in graph}
    distancias[inicio] = 0
    estacion_anterior = {estacion: None for estacion in graph}
    cola_prioridad = [(0, inicio)]
    while cola_prioridad:
        distancia_actual, estacion_actual = heapq.heappop(cola_prioridad)

        if estacion_actual == destino:
            # Se ha llegado al punto de destino, construir el camino y terminar
            ruta = []
            while estacion_actual is not None:
                ruta.insert(0, estacion_actual)
                estacion_actual = estacion_anterior[estacion_actual]
            return ruta

        if distancia_actual > distancias[estacion_actual]:
            continue

        for vecino, peso in graph[estacion_actual].items():
            distancia = distancia_actual + peso

            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                estacion_anterior[vecino] = estacion_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return None