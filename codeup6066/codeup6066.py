# 모범답안
a,b,c=input().split()

a=int(a)
b=int(b)
c=int(c)

if a%2==0:
    print("even")
else:
    print("odd") 

if b%2==0:
    print("even")
else:
    print("odd") 

if c%2==0:
    print("even")
else:
    print("odd")

# 1
a, b, c = map(int, input().split())
print('even') if a % 2 == 0 else print('odd')
print('even') if b % 2 == 0 else print('odd')
print('even') if c % 2 == 0 else print('odd')

# 2
a, b, c = map(int, input().split())

if a % 2 == 0:
    print('even')
else:
    print('odd')
if b % 2 == 0:
    print('even')
else:
    print('odd')
if c % 2 == 0:
    print('even')
else:
    print('odd')