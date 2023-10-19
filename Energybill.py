#1 Energybill
units =int(input("please enter the number of units:"))
def bill_calculator(units):
if(units<=100):
   return units*3.46;
elif units<=300:
    return((100*3.46)+(units-100)*7.43);
elif units<=500:
    return((100*3.46)+(200*7.43)+(units-300)*10.32);
elif units>=501:
    return((100*3.46)+(200*7.43)+(units-500)*11.71);
bill_calculator(units)    
units = units + (units*1.45)
units = units + 100
units = units + (units*0.16)
if units<=400:
    print("Bill should be 400")
else:
    print(units)


