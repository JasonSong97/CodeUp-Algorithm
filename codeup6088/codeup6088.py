# 모범답안
a,d,n=input().split()

a=int(a)
d=int(d)
n=int(n)

s=a
for i in range(2, n+1):
    s+=d

print(s)
   
# 1
a, d, n = map(int, input().split())

sum = a
for i in range(2, n + 1):
    sum = sum + d
print(sum)

# 2
a, d, n = map(int, input().split())

num = a
for _ in range(2, n+1):
    num = num + d
print(num)