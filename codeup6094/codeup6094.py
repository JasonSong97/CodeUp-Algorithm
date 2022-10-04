# 모범답안
n = int(input())
a = input().split()

for i in range(n) :
    a[i] = int(a[i])

min = a[0]
for i in range(0, n) :
    if a[i] < min :
        min = a[i]

print(min)

# 1
n = int(input()) 
a = map(int, input().split())
a = list(a)
test = a[0]

for i in range(1, n):
    if test > a[i]:  test = a[i]

print(test)