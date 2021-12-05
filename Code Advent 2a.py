import os
profundidad = 0
horizontal = 0
with open('C:/Users/ldeli/Desktop/CodeAdvent/datosProblema2.txt', 'r') as coordsInput:
    list = (coordsInput.read()).split("\n")
    for x in range(len(list)):
        coordenada = list[x]
        #Como todos los numeros son de una cifra uso -1
        if coordenada[0:2] == "up":
            profundidad -= int(coordenada[-1])
        if coordenada[0:4] == "down":
            profundidad += int(coordenada[-1])
        if coordenada[0:7] == "forward":
            horizontal += int(coordenada[-1])
print(profundidad * horizontal)