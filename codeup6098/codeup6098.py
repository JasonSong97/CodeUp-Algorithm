# 모범답안
m=[]
for i in range(12) :
    m.append([])
    for j in range(12) :
        m[i].append(0)

for i in range(10) :
    a=input().split()
    for j in range(10) :
        m[i+1][j+1]=int(a[j])

x = 2
y = 2
while True :
    if m[x][y] == 0 :
        m[x][y] = 9
    elif m[x][y] == 2 :
        m[x][y] = 9
        break

    if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9) :
        break

    if m[x][y+1] != 1 :
        y += 1
    elif m[x+1][y] != 1 :
        x += 1
    

for i in range(1, 11) :
    for j in range(1, 11) :
        print(m[i][j], end=' ')
    print()

# 1
d = []
for i in range(11):
    d.append([])
    for j in range(11):
        d[i].append(0)

for i in range(10):
    a = input().split()
    for j in range(10):
        d[i+1][j+1] = int(a[j])
        
x = 2
y = 2

while True:
    if d[x][y] == 0:
        d[x][y] = 9
    elif d[x][y] == 2:
        d[x][y] = 9
        break
    
    if (d[x+1][y] == 1 and d[x][y + 1] == 1 ) or (x == 9 and y == 9):
        break

    if d[x][y+1] != 1:
        y += 1
    elif d[x+1][y] != 1:
        x += 1
        
for i in range(1, 11):
    for j in range(1, 11):
        print(d[i][j], end = ' ')
    print()