string = "Hey there! This, is, random string.# SS#$#(_XXysfsd"
print("original string is :", string)
special_Symbol = [";", ":", "!", "*", "#", "$", "(", ")", "_"]
for i in special_Symbol:
    string = string.replace(i,"")
print("Final String is :",string)
