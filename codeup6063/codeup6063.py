# 모범답안
a, b = input().split()
a = int(a)
b = int(b)
c = a if a>=b else b
print(c)

# 1
a, b = map(int, input().split())
print(a if a >= b else b)