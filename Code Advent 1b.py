
with open('./input1', 'r') as numsInput:
    list = (numsInput.read()).split("\n")
    res = 0
    sum = int(list[0]) + int(list[1]) + int(list[2])
    for x in range(3, len(list)):
        newSum = int(list[x]) + int(list[x-1]) + int(list[x-2])
        if newSum > sum:
            res += 1
        sum = newSum
print(res)
