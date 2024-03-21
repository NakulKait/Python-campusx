l =[1,6,2,5,9,2,3,2]
l1 = [i*2 for i in l]
print(l1)

l2 = [i**2 for i in range(1,11)]
print(l2)

l3 = [i**2 for i in range(1,11) if i%2 == 0]
print(l3)

fruits = ['apple' , 'oranges' , 'papaya' , 'guava']
l4 = [fruit for fruit in fruits if fruit[0] =='o']
print(l4)