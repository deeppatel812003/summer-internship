#3
list=[43,23,14,19,22,34,12,27]
max_num = list[0]
i=0
while(i<len(list)):
   if list[i]>max_num:
      max_num = list[i]
   i+=1
   print("maximum number is",max_num)

min_num = list[0]
i=0
while(i<len(list)):
   if list[i]<min_num:
      min_num = list[i]
   i+=1
   print("minimum number is",min_num)
