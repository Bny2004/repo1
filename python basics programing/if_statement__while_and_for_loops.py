#if statements
#temp = int(input("enter temp:  "))
#if temp > 30:
#     print("its a hot day")
#     print("drint alot of water")
#elif temp > 20:
#    print("its a nice day")
#else:
#    print("its cold")
#print("done") 


#while  loops
i=1
while  i<=10:
    print(i*'*')
    i += 1

#lists
name = [ "jhon", "bob", "mosh","sam","mary"]
print(name)
print(name[0])
print(name[1])
print(name[-1])
name[0]="jon"
print(print(name[0:3]))

#list methods
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
numbers.insert(0, "t")
print(numbers)
print(len(numbers))
print(5 in numbers)
numbers.remove(3)
print(numbers)
numbers.clear()
print(numbers)

#for loops
num = [1, 2, 3, 4, 5]
for item in num :
    print(item)

#range function
obj = range(5 , 10 , 2)
for ob in obj :
    print(ob)

#tuples
itm = (1, 2, 3)