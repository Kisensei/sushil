lst=[2,3,4,5]
sum=0
sum1=0
for i in range (0,4):
    if lst[i] % 2 == 0:
        sum =sum + lst[i]
    else:
        sum1 = sum1+lst[i]
print(sum)
print(sum1)
