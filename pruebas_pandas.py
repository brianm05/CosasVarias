import pandas as pd
ruta='https://es.wikipedia.org/wiki/Campeonato_de_Primera_Divisi%C3%B3n_2023_(Argentina)'
tablas = pd.read_html(ruta)
posiciones=tablas[10]

print("Evolucion de posiciones fecha a fecha:")
print(posiciones)

unEquipo=posiciones[0:1]
print("prueba:")
print(unEquipo)
