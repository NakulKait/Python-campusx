D = {"Name" : "Nakul" , "Gender" : "Male" , "Age" : 18}
D1 = {key : value for key,value in D.items() if len(key)>3}
print(D1)

L = {1,2,3,4,5,6,7,8}

d2 = {item : item **2 for item in L}
print(d2)