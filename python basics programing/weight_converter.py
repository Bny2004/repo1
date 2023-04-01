weight = float(input("what is your weight? :"))
foactor = input("is your weight in kg or lbs ")

if foactor.lower() == "kg" :
    converted = weight/0.45
    input("weight in lbs is  " + str(converted) )

elif foactor.lower() == "lbs" :
    converted = weight*0.45
    input("weight in kg is " + str(converted) )
else:
    print("plese enter appropriate operator")