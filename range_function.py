"""a=range(5)
print(a[3])
b=range(2,5)
print(b[2])"""
c=range(-2,15,2)#2 5 (start,stop,step) 
"""start>stop if nt true then empty
- Positive step → start < stop*
- Negative step → start > stop
- equal step=stop->empty
"""
for i in c:
   print(i)


for i in range(10,0):
    print(i)
#python always expect start<stop 
#But here start=10 is greater than stop=0. That means the range is empty.

