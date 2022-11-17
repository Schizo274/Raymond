filename = open("StudentData.txt", "r")
lines = filename.readlines()
filename.close()

def getGPA(list):
    index = []
    for i in range(1, len(lines)):
        line = list[i]
        gpa = float(line[-5:])
        index += [gpa]
    return index

def bubblesort(list):
    hasSwap = True
    tempIndexList = []
    for i in range(len(list)):
        tempIndexList += [i]
    while hasSwap:
        hasSwap = False
        for i in range(len(list)):
            if i == len(list)-1:
                continue
            if list[i] > list[i+1]:
                hasSwap = True
                tempIndexList[i], tempIndexList[i+1] = tempIndexList[i+1], tempIndexList[i]
                list[i], list[i+1] = list[i+1], list[i]
    return tempIndexList

for i in bubblesort(getGPA(lines)):
    print(lines[i+1])