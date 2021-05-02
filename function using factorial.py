def factorial(num):
    a=1
    for i in range(num,1,-1):
        a=a*i
    return a
num=int(input("euta number:"))

ans=factorial(num)
print(ans)