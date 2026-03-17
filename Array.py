from array import *
import numpy as np

val = array('i',[1,2,3,4,5,6,7,8,9])

print(val)

for i in range(0,len(val)):
    print(val[i] , end = " ")

print('\n')

for x in val:
    print(x, end = ' , ')

print('\n')

print(val.typecode)

val.reverse()

for i in range(0,len(val)):
    print(val[i] , end = " ")

print('\n')

# val.insert(1,50)
# val.append(100)
# val[2] = 200

copyArray = array(val.typecode , (x*2 for x in val))

copyArray.pop(3)
for i in range(0,len(copyArray)):
    print(copyArray[i] , end = " ")


# slicing

# a = val[starting index : ending index]

print('\n')

abc = val[2 : 5]
for i in range(0, len(abc)):
    print(abc[i], end= " ")


print('\n')
# user input array

# arr = array('i', [])

# n = int(input('Enter a number'))

# for i in range (0,n):
#     arr.append(int(input('Enter next input')))


# for x in arr:
#     print(x , end = ' ') 


# searching the index in array 

arr1 = array('i', [12,54,67,87,97,11])

i = arr1.index(54)

print(i)

print('\n')
# Numpy arrays

val = np.array(
    [1,2,3.5, 'a']
) 

for x in val:
    print(x, end = " ")