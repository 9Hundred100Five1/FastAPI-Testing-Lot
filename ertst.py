def fac(i):
    if i == 0 or i == 1:
        return 1
    else:
        return fac(i-1)*i


n = int(input())
print(fac(n))