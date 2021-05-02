def mul(n):
    if n==1:
        return 3
    else:
        return 3+mul(n-1)
print(mul(99))