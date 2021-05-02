def  armstrong(num):
    sum=0
    temp=num
    while num>0:
        rem=num%10
        cube=rem **3
        sum+=cube
        num//=10
    if (sum==temp):
        print("yes")
    else:
        print("no")
a=int(input('enter the num: '))
armstrong(a)