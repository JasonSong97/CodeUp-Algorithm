# 모범답안
a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)

for i in range(1, n) :
   a = a*m+d

print(a)

# 1
a, m, d, n = map(int, input().split())
new = a
for _ in range(1, n):
    new = (new * m) + d 
print(new)

# 2
a, m, d, n = map(int, input().split())
x = a
for _ in range(2, n + 1):
    x = (x * m) + d
print(x)