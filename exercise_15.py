number_list=[]
numbers=input("Enter number seperated by space:")
number_list=numbers.split()
count=0
for number in number_list:
  count+=1
print(count)
for i in range(count):
  number_list[i]=int(number_list[i])
print(number_list)

maximum_number=number_list[0]
for number in number_list:
  if number>maximum_number:
    maximum_number=number
print(f"The maximum number is {maximum_number}.")
   
