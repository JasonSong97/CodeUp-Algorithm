# 모범답안
h, b, c, s = input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

print(round(h*b*c*s/8/1024/1024, 1), "MB")

# 1
h, b, c, s = map(int, input().split())

num = h * b* c * s / 8 /1024/ 1024
print(f'{round(num, 1)}' + ' MB')