def selection_sort(a, size):
    for i in range(size):
        minimum = i

        for j in range(i + 1, size):
            if a[j] < a[minimum]:
                min_index = j
        (a[i], a[minimum]) = (a[minimum], a[i])


points = [1,1.5,2,3.5,2.5,4,3]
size = len(points )
selection_sort(points , size)
print(points)

