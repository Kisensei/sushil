a=int(input('enter the number: '))
factorial=1
if a<0:
    print('sorry it isnt available')
elif a==0:
    print('the factorial og 0 is 1')
else:
    for i in range (1,a+1):
        factorial=factorial*i
    print('the ans is',a)