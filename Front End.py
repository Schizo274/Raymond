filename = open("StudentData.txt", "r")
lines = filename.readlines()

def bubblesort(list):
    # Swap the elements to arrange in order
    for iter_num in range(len(list) - 1, 0, -1):
        for idx in range(iter_num):
            if list[idx][-5:-1] > list[idx + 1][-5:1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp


for i in range(len(lines) -1):
    print(lines[i][-5:-1])