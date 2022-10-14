# 모범답안
n=int(input())

if n<0:
    if n%2==0:
        print('A')
    else:
        print('B')
else:
    if n%2==0:
        print('C')
    else:
        print('D')

# 1
x = int(input())

if x < 0 and x % 2 == 0: print('A')
elif x < 0 and x % 2 != 0: print('B')
elif x > 0 and x % 2 == 0: print('C')
elif x > 0 and x % 2 != 0: print('D')

# 2
a = int(input())

if a < 0 and a % 2 == 0:
    print('A')
elif a < 0 and a % 2 != 0:
    print('B')
elif a > 0 and a % 2 == 0:
    print('C')
elif a >0 and a % 2 != 0:
    print('D')