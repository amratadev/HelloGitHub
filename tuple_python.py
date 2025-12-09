tuple1=(12,6,-8,'jenny',True)
print(tuple1)

print(tuple1[1]) #indexing

print(tuple1[-1]) # negative indexing possible

#print(tuple1[-6])->index out of range

tuple2=(45,)
print(type(tuple2))

#tuple1[0]=13 Tuple is immutable → ekda create kela ki tyat directly element change karu shakat nahi.
#print(tuple1)

tuple3=(10,20,10)#duplicates allowed in tuple.
print(tuple3)

print(tuple3[3:])#[start index:end index]
"""- start → not given → suru hoतो index 0 (first element)
- end → not given → jato last element paryant
- step = 2 → every 2nd element gheतो (skip 1 element each time
"""
print(tuple3[::2])

print(len(tuple3))

tuple4=(tuple1,tuple3)#nesting of tuple
print(tuple4)

print(tuple4[0][2])#tuple4[tuple1][tuple1 2nd index]

tuple5=tuple1+tuple3
print(tuple5)#Concatenation
print(tuple5[0])

print(min(tuple3))#we can compare int & str
print(max(tuple3))

print(tuple3.count(10))

print(tuple3.index(10))#first coming match index

list1=[1,2,3,5]
print(tuple(list1))#convert list into tuple

tuple6=(10,)*5
print(tuple6)

