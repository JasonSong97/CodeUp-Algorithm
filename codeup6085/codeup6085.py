# 모범답안
w,h,b = input().split()
res=int(w)*int(h)*int(b)/1024/1024/8

print('%.2f'%res,"MB")

# 1
w, h, b = map(int, input().split())

x = w * h * b / 8 / 1024 / 1024

print(format(x, '.2f') + ' MB')
