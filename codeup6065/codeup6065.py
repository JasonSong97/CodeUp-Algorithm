# 모범답안
a, b, c = input().split()

a=int(a)
b=int(b)
c=int(c)

if a%2==0:
    print(a)
    
if b%2==0:
    print(b)
    
if c%2==0:
    print(c)

# 1
a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)