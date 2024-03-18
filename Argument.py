#Default Argument 

# def power(a=1,b=1):
#     return a**b
# print(power(2))

#Arbitrary Argument

def product(*number):
    a=1
    for i in number:
        a = a*i
    return a
print(product(2,6,7))