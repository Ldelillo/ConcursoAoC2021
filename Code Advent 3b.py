with open('./input3', 'r') as numsInput:
    list = (numsInput.read()).split("\n")
    list2 = list
    n = 0
    while len(list) > 1:
        nums0 = 0
        nums1 = 0
        copiaList = []
        for x in range(len(list)):
            if list[x][n] == "0":
                nums0 += 1
            else:
                nums1 += 1
        for k in range(len(list)):
            if nums0 > nums1:
                if list[k][n] == "0":
                    copiaList.append(list[k])
            else:
                if list[k][n] == "1":
                    copiaList.append(list[k])
        list = copiaList
        n += 1
    O2 = list[0]
    n = 0
    while len(list2) > 1:
        nums0 = 0
        nums1 = 0
        copiaList = []
        for x in range(len(list2)):
            if list2[x][n] == "0":
                nums0 += 1
            else:
                nums1 += 1
        for k in range(len(list2)):
            if nums0 > nums1:
                if list2[k][n] == "1":
                    copiaList.append(list2[k])
            else:
                if list2[k][n] == "0":
                    copiaList.append(list2[k])
        list2 = copiaList
        n += 1
    CO2 = list2[0]
numO2 = 0
numCO2 = 0

for x in range(12):
    numCO2 += int(CO2[x]) * pow(2, 11-x)
    numO2 += int(O2[x]) * pow(2, 11-x)

print(numCO2 * numO2)