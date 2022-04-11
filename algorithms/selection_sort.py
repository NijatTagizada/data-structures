data = [64, 63, 1, 25, 2, 12, 22, 11]


def selection_sort():
    for i in range(len(data)):

        min_index = i
        for j in range(i + 1, len(data)):
            if data[min_index] > data[j]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]
        print(data)


selection_sort()
print('Answer: ', data)
