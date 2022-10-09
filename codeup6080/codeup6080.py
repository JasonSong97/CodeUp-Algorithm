# 모범답안
n,m=input().split()

n=int(n)
m=int(m)

for i in range(1, n+1) :
    for j in range(1, m+1) :
        print(i, j)

# 1
a, b = map(int, input().split())
for i in range(1, a + 1):
    for j in range(1, b + 1):
        print(i, j)