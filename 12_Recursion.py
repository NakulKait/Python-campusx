# def multiply(a,b):
#     result = 0
#     for i in range(b):
#         result = result + a
#     print(result)

# multiply(3,4)

#Recursion

# def multiply(a,b):
#     if b==1:
#         return a
#     else :
#         return a + multiply(a,b-1)
    
# print(multiply(3,4))

#factorial

# def factorial(a):
#     if a==1:
#         return a
#     else:
#         return a * factorial(a-1)
    
# print(factorial(5))

#Palindrome

# def Palindrome(s):
#     if(len(s)<=1):
#         print("It is pallindrome")
#     else:
#         if s[0]==s[-1]:
#             Palindrome(s[1 :-1])
#         else:
#             print("It is not pallindrome")
# Palindrome("madam")
# Palindrome("nakul")

#Rabbit Problem / Fibonacci Series

def count(month):

    if month == 1 or month==0:
        return 1
    else:
        return count(month-1)+ count(month-2)
    
print(count(12))





