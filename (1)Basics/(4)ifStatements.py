# if statements1
temp = int(input("enter temp:  "))
if temp > 30:
    print("its a hot day")
    print("drint alot of water")
elif temp > 20:
   print("its a nice day")
else:
   print("its cold")
print("done") 



#eg weight converter
weight = float(input("what is your weight? :"))
factor = input("is your weight in kg or lbs ")

if factor.lower() == "kg" :
    converted = weight/0.45
    input("weight in lbs is  " + str(converted) )

elif factor.lower() == "lbs" :
    converted = weight*0.45
    input("weight in kg is " + str(converted) )
else:
    print("plese enter appropriate operator")