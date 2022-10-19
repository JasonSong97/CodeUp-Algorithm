# 모범답안
a, b, c = input().split()
a=int(a)
b=int(b)
c=int(c)
hap=a+b+c
avg=hap/3
print(hap, format(avg, ".2f"))

# 1
a, b, c = map(int, input().split())
sum = a + b + c
print(sum, format(sum/3, '.2f'))

# 2
a, b, c = map(int, input().split())
d = a+b+c
print(d, format(d/3, '.2f'), sep = ' ')