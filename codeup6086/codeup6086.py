# 모범답안
a=int(input())
s=0
c=0

while True:
    s=s+c
    c=c+1
    if s>=a:
        break
    
print(s)

# 1
n = int(input())
c = 0
s = 0
while True :
  s += c
  c += 1
  if s>=n :
    break
print(s)