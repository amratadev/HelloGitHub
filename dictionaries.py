phone_no={
    'Ram':1234,
    'Shyam':3456,
    'Mohan':8976,
    'Ram':666
}
print(phone_no['Ram'])
"""phone_no=dict({
    'Ram':1234,
    'Shyam':3456,  
    'Mohan':8976,
    'Ram':666
})"""

phone_no['Mohan']={1111,2222.3333}
print(phone_no['Mohan'])
phone_no['Shyam']={'Shyam_home':9152,'Shyam_work':5233}
print(phone_no['Shyam']['Shyam_work']) 
del phone_no['Ram']
print(phone_no)
#print(phone_no.pop('Shyam'))particular item delete
print(phone_no.popitem())#random delete
print(phone_no)
print(phone_no.keys())
print(phone_no.values())
print(phone_no.items())
for i in phone_no.items():
    print(i)
phone_no2=phone_no.copy()
print(phone_no2)
    