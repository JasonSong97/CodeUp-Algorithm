# 모범답안
a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

for i in range(1, n) :
    a = a*r

print(a)

# 1
a, r, n = map(int, input().split())

sum = a
for i in range(2, n + 1):
    sum = sum * r
print(sum)

# 2
a, r, n = map(int, input().split())

s = a
for _ in range(2, n + 1):
    s *= r
print(s)