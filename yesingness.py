def Sort(FileName):
    index = []
    with open(FileName, "r") as file:
        lines = file.readlines()
        for l in lines[1:]:
            split = l.split()
            for i in range(1, len(split)):
                gpa = (split[-1])
                if gpa not in index:
                    index += [gpa]
    hasSwap = True
    tempIndexList = []
    for i in range(len(index)):
        tempIndexList += [i]
    while hasSwap:
        hasSwap = False
        for i in range(len(index)):
            if i == len(index)-1:
                continue
            if index[i] > index[i+1]:
                hasSwap = True
                tempIndexList[i], tempIndexList[i+1] = tempIndexList[i+1], tempIndexList[i]
                index[i], index[i+1] = index[i+1], index[i]
    for i in tempIndexList:
        print(lines[i + 1])
    return tempIndexList

Sort("StudentData.txt")

