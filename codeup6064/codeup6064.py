# 모범답안
a, b, c = input().split()
a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = int(c)

d = a if a<b else b
e = d if d<c else c

print(e)

# 1
a, b, c = map(int, input().split())
print((b if a > b else a) if ((b if a > b else a) < c) else c)
