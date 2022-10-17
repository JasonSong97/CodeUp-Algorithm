# 모범답안
a, b = input().split()
c= bool(int(a))
d= bool(int(b))

print( not (c or d) )

# 1
a , b = map(int, input().split())
x = bool(a)
y = bool(b)
print(not(x) and not(y))

# 2
a, b = map(int, input().split())
print(not(bool(a) or bool(b)))