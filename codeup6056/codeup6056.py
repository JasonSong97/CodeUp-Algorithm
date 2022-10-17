# 모범답안
a, b=input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

# 1
a, b = map(int, input().split())
print((bool(a) and not bool(b)) or (not bool(a) and bool(b)))