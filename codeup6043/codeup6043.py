# 모범답안
a,b=input().split()
a=float(a)
b=float(b)
c=a/b
print('%.3f'%c)

# 1
a,b=input().split()
a=float(a)
b=float(b)
c=a/b
print(format(c,".3f"))

# 2
a, b = map(float, input().split())
print(format(a/b, '.3f'))