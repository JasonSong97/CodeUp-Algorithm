# 모범답안
r, g, b = input().split()

r = int(r)
g = int(g)
b = int(b)

for i in range(0, r) :
    for j in range(0, g) :
        for k in range(0, b) :
            print(i, j, k)

print(r*g*b)

# 1
r, g, b = map(int, input().split())
count = 0
for i in range(r):
    for j in range(g):
        for h in range(b):
            count += 1
            print(i, j, h)
print(count)

# 2
r, g, b = map(int, input().split())
count = 0
for i in range(r):
    for j in range(g):
        for h in range(b):
            count += 1
            print(i, j, h)
print(count)