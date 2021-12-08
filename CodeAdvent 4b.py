def strToIntList(list):
    for x in range(len(list)):
        if list[x][:-1] == "n":
            list[x] = int(list[0:1])
        else:
            list[x] = int(list[x])
    return list

def winColumna(list):
    for x in range(len(list)):
        equals = True
        n = 0
        while equals and n < len(list):
            if list[n][x] != " ":
                equals = False
            n += 1
        if equals == True:
            break
    return equals

def winFila(list):
    for x in range(len(list)):
        equals = True
        n = 0
        while equals and n < len(list):
            if list[x][n] != " ":
                equals = False
            n += 1
        if equals == True:
            break
    return equals

with open("./input4", 'r') as numsInput:
    nums = (numsInput.readline()).split(",")
    strToIntList(nums)
    bingo = []

    for x in range(100):
        if numsInput.readline() == "\n":
            carton = []
            for n in range(5):
                filaList = []
                filaStr = numsInput.readline()

                for k in range(5):
                    filaList.append(filaStr[3*k:2+3*k])
                carton.append(strToIntList(filaList))
            bingo.append(carton)

    win = 0
    a = -1
    while win<=99:
        a += 1
        win = 0
        for x in range(100):
            for n in range(5):
                if nums[a] in bingo[x][n]:
                    bingo[x][n][bingo[x][n].index(nums[a])] = " "
            if (winColumna(bingo[x]) == True) or (winFila(bingo[x]) == True):
                win += 1
            else:
                k = x

res = 0
for x in range(len(bingo[k])):
    for n in range(len(bingo[k][x])):
        if bingo[k][x][n] != " ":
            res += bingo[k][x][n]
print(res * nums[a])


