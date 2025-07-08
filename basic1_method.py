def firstMethod(a):
    
    if(isinstance(a, int)): #to compare type with variable
        a = str(a)
    print(a+" Baral")

firstMethod("Rupesh")
firstMethod("Subhasmita")
firstMethod(10)

a=[10,20,30,40]
b=["ll","kk"]
a.insert(2,"abc") #add value with index
a.append("Rup") # add value at last
a.pop(3) #remove value through index
a.remove("abc") # remove value from list
print(a)
del(a[2])
print(a)
a.extend(b) #to add 2 lists
print(a)

b.clear() #to clear whole list
print(b)

b=(10,20,30,"abc") # ()-> tuple , value is fixed we can't change & duplifate allowed
#b[2]=40 # this will give error because tuple is immutable
print(b[2])
print(b[1:3]) # slicing
print(len(b)) # length of tuple
print(type(b)) # type of variable
b = list(b) # convert tuple to list
b.append("new value") # now we can add value in b because it is converted to list
print(b)
b = tuple(b) # convert list to tuple
print(b)