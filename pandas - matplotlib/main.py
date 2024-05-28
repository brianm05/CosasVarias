def generarPos(equipo):
    import pandas as pd
    ruta="https://es.wikipedia.org/wiki/Campeonato_de_Primera_Divisi%C3%B3n_2023_(Argentina)"

    tabla=pd.read_html(ruta)

    posiciones=tabla[10]

    dataPos=[]
    for i in range(1,28):
        pos=posiciones.iloc[equipo,i]
        if(len(pos)==4 or len(pos)==3):
            pos = pos[:-2]
        pos=int(pos)
        dataPos.append(pos)
        print(i)
    print(dataPos)
    return dataPos



import matplotlib.pyplot as plt
import numpy as np
import random

#x = range(27)
#y = [1,4,6,4,9]*5

fechas=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

x = generarPos(20)
y = fechas

plt.figure(figsize=(10,6))

colores=("#"+random.choice(["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"])
        +random.choice(["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"])
        +random.choice(["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"])
        )


for i in range(28):
    #print(i)
    i=generarPos(i)
    #print(i)
    plt.plot(y,i,marker="o",
        c=("#"+random.choice(["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"])
            +random.choice(["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"])
            +random.choice(["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]))
        ,linestyle="--")


#plt.plot(y,x,marker="o",c=colores,linestyle="--")

plt.yticks(fechas)
plt.xticks(fechas)

plt.ylim(max(y)+2, min(y)-1)
plt.xlabel("Fecha")
plt.ylabel("Posicion en tabla")

plt.grid(True)

plt.title("Titulo")

plt.show()