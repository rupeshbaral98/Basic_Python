a,b,c,d,e = "abc",10,20,30,40

print(e)

a = 10,20,30,40
print(a[2])

a= 10
print(type(a))


a=4
b="age"
print(b+str(a))
print(a,b)


if(a > 5):
    if(a < 7):
      print("a is greater",a)
      print("abc")
else:
    print("a is not greater")

a = 10,20,30,40
for i in a:
    print(i)

for i in range(len(a)):
    if a[i] % 2 == 0:
        print(a[i])


print(10 + 4j)

a=[10,20,30,40,50,"abc",2.50,True]
print(a)
print(a[4:7])
print(len(a))
a[3] ="change"
print(a)
