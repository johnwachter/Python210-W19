#Dictionaires1
mydict = {'Name': 'Chris', 'City': 'Seattle', 'Cake':'Chocolate'}
print(mydict)
del mydict['Cake']
print(mydict)
mydict['Fruit'] = 'Mango'
print(mydict)
print(mydict.keys())
print(mydict.values())
print(mydict.get('Cake', 'Cake not in dictionary'))
if 'Mango' in mydict.values():
    print('Mango is in the dictionary')
else: print('Mango not in dictionary')

#Dictionaries2 - What???

#Sets1
s2 = range(0,21)
s3 = range(0,21)
s4 = range(0,21)

holds2 = list(s2)
holds3 = list(s3)
holds4 = list(s4)

l2 = []
l3 = []
l4 = []

for i in holds2:
   if i%2 ==0:
        l2.append(i)
for i in holds3:
    if i%3 == 0:
        l3.append(i)
for i in holds4:
    if i%4 == 0:
        l4.append(i)
    
s2 = set(l2)
s3 = set(l3)
s4 = set(l4)
print(s2, s3, s4)
print(s3 < s2)
print(s4 <s2)

#Sets2

pyset = {'p', 'y', 't', 'h', 'o', 'n'}
pyset.add('i')
print(pyset)

marathonset = frozenset = {'m','a','r','a','t','h','o','n'}
print(marathonset)

union = pyset | marathonset
print(union)

intersection = pyset & marathonset
print(intersection)
