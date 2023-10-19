with open("sample.txt", "r+") as file:
    file.write("Hello world. I am Python developer.")
file =  open("sample.txt", "r+")
content = file.read()
print(content)
file.close()
file_reverse = open("reverse.txt", "w")
with open("sample.txt", "r+") as myfile:
    data = myfile.read()
    data_2 = data[::-1]
    file_reverse.write(data_2)
    file_reverse.close()
file =  open("reverse.txt", "r+")
content = file.read()
print(content)
file.close()
