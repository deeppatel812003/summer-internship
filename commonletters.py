#5 Find common letters
S1 = input("Enter the First String:")
S2 = input("Enter the Second String:")
a = list(set(S1)&set(S2))
print("The Common letters are:")
print(a)