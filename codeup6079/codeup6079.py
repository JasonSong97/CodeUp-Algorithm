# 모범답안
n = int(input())

s = 0
t = 0
while s<n :
    t = t+1
    s = s+t
  
print(t)

# 1
sum = int(input())
sub_sum = 1
x = 0
while sub_sum <= sum:
    x += 1
    sub_sum = sub_sum + x
print(x)

# 2
n = int(input())

new_num = 0
sum = 0
while sum < n: 
    new_num = new_num + 1
    sum = sum + new_num
    
print(new_num)