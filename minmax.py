def min_value(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min
num = [10,32,24,16,22]
print(min_value(num))

