l=input()
m=[]
for i in range(l):
    m.append(map(int, raw_input().split(' ')))

def isOk(i, j, limit):
    if(i<0 or i>=limit):
        return False
    elif(j<0 or j>=limit):
        return False

    elif(m[i][j]==0):
        return True

    value=m[i][j]
    return isOk(i+value, j, limit) or isOk(i, j+value, limit)

print m
print isOk(0, 0, l)