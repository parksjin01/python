import itertools

tmp=[]
for i in range(6):
    tmp.append(i)

friend=[[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [3, 5], [4, 5]]

print sorted(friend)

def checking(res):
    for i in res:
        if friend.count(i)==0:
            return 0
    return 1

cnt=0

for p in itertools.permutations(tmp,6):
    p=list(p)
    res=[]
    while p!=[]:
        res.append(p[:2])
        p=p[2:]

    if checking(res):
        print res
        cnt+=1

print cnt/6