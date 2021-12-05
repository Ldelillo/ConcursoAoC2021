tasaGamma = 0
tasaEpsilon = 0
with open('./input3', 'r') as numsInput:
    list = (numsInput.read()).split("\n")
    for x in range(12): #12 es la longitud de los numeros binarios recibidos
        bit0 = 0
        bit1 = 0
        for n in range(len(list)):
            if list[n][x] == "0":
                bit0 += 1
            else:
                bit1 += 1
        if bit0 > bit1:
            tasaGamma += pow(2, 11-x)
        else:
            tasaEpsilon += pow(2, 11-x)
print(tasaGamma * tasaEpsilon)