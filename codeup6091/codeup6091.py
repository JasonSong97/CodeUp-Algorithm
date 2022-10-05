# 모범답안
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
    d += 1

print(d)

# 1
a, b, c = map(int, input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
    d += 1
print(d)

# 2
a, b, c = map(int, input().split())

day = 1
while day%a != 0 or day%b != 0 or day%c != 0:
    day += 1
print(day)