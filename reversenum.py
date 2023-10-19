#6 reverse number
#Using string slicing
num = 1234
print(str(num)[::-1])

#Using while loop
num = 5678
reversed_num=0
while num!=0:
    digit=num % 10
    reversed_num=reversed_num * 10 + digit
    num//=10
print(str(reversed_num))