#4 Prime number or not
num = 59
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")   
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

