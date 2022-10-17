# 모범답안
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and b) or (not a and not b))

# 1
a, b = map(int, input().split())
print((bool(a) and bool(b)) or (not bool(a) and not bool(b)))