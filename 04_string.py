#strings are immutable we can reassign whole string but can't reassign its alphabets

a= "Nakul"
print(a)

#substring from string 

print(a[0])

#slicing

n = "Hello World"

print(n[0:5])
print(n[2:8:3])
print(n[-5:-1])
print(n[::-1])

#Operators on string

#concatenation 

print("Nakul" +" "+ "Kait")

print("*"*50)

print("Mumbai">"Pune")

print("kol">"Kol")

#Logical Operator

#Python consider empty string as False 

print("hello" or "World")

print("hello" and "World")

print("" and "Hello")

print("" or "Hello")