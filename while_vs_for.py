"""number=int(input("Enter a number(-1 to quit):"))
#sentinal value
while number !=-1:
    print(number)
    number=int(input("Enter a number(-1 to quit):"))
    if number==3:
        break
else:
    print("in else block")
print("out from block")"""


"""count=0
while True:
    print(count)
    count+=1
    if count==5:
        break
else:
    print("in else block")
print("out from block")"""

total=0
number=int(input("enter a number(0 to quit):"))
#sentinal value
while number!=0:
    total=total+number
    number=int(input("enter a number(0 to quit):"))
print("total is",total)