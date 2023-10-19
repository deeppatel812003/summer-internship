string = input("Enter the String :")
string = string.lower()
string = list(string)
print(string)

a = 0 ; e = 0 ; i =0 ; o = 0 ; u = 0 

for j in range(0,len(string)):
    if string[j] == "a":
        a = a + 1
    elif string[j] == "e":
        e = e + 1
    elif string[j] == "i":
        i = i + 1
    elif string[j] == "o":
        o = o + 1    
    elif string[j] == "u":
        u = u + 1
print("No. of a :", a)
print("No. of e :", e)
print("No. of i :", i)
print("No. of o :", o)
print("No. of u :", u)
