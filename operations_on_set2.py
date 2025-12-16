set1={'Ram','Shyam','Jenny'}
set2={'Jeeny','Jiya','Aakash'}
set3={'Ankur','Pradeep'}

print(set1.difference(set2,set3))#returns elements of the first set (set1) that are not present in any of the other sets (set2 and set3).
print(set1-set2-set3)

print(set1.difference((set2)))
print(set1.difference(['Mohan','Shiva']))
print(set1-set(('Mohan','Shiva')))
print(set1-set(['Ram','Shyam','Jenny','Mohan','Shiva']))

print(set1.difference_update((set2)))
print(set1)

print(set1.symmetric_difference(set2,set3))
print(set1^set2^set3)

print(set2.symmetric_difference_update(set1))
print(set2)
