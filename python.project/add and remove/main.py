a ={1,2,3,4,5,6}
a.add("feqan")
print(a)
print(25*"=")
a.remove(2)
print(a)
print(25*"=")
a.discard(5)
print(25*"=")
#discard hec bir zaman xeta vvermir.....

x ={""}
y ={""}
print(x.difference(y))
print(25*"=")
print(y.difference(x))
print(25*"=")
y.difference_update(x)
print(y)
print(25*"=")
x.difference_update(y)
print(x)
print(25*"=")
print(x.intersection(y))