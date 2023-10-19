#move all zeros to end
def move_zeros_to_end(arr):
    non_zero_elements = [num for num in arr if num != 0]
    zero_count = len(arr) - len(non_zero_elements)
    return non_zero_elements + [0] * zero_count
array1 = [0, 1, 0, 3, 12]
array2 =[1,7,0,0,8,0,10,12,0,4]
result1 = move_zeros_to_end(array1)
result2 = move_zeros_to_end(array2)
print(result1)
print(result2)