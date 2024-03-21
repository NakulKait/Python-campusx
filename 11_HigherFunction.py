def return_sum(func , L):
    result = 0
    for i in L :
        if func(i):

            result = result + i
    return result



L = [11,14,21,23,56,78,45,29,28]
a = lambda x : x %2 ==0
b = lambda x : x % 2 !=0
c = lambda x : x%3 == 0

print(return_sum(a,L))
print(return_sum(b,L))
print(return_sum(c,L))