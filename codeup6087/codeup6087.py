# 모범답안
n=int(input())

for i in range(1, n+1) : 
    if i%3==0 : 
        continue            #다음 반복 단계로 넘어간다.
    print(i, end=' ') 

# 1
x = int(input())

for i in range(1, x+1):
    if i % 3 ==0:continue
    print(i, end = ' ')