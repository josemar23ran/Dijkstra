import json
from dijkstra import dijkstra
with open ("metro_graph.json" , "r") as archivo:
    metro_graph=json.load(archivo)
#print (metro_graph)  #Verifica que se cargo correctamente

inicio= 'La Paz'
destino = 'Tasqueña'
ruta_mas_corta = dijkstra(metro_graph, inicio, destino)

if ruta_mas_corta:
    print("Ruta más corta desde ",inicio, " hasta ",destino," : ")
    for i in ruta_mas_corta:
      print(i)
else:
    print(f'No hay una ruta válida desde {inicio} hasta {destino}') #es probable que haya un error en el nombre, resiva en el JSON como se encuentra escrito