test=[]

for i in range(2993):
    test.append(1)
cache=[]
for i in range(len(test)+3):
    cache.append(-1)

def nando1(tmp):
    for i in range(len(tmp)-1):
        if tmp[i]!=tmp[i+1]:
            return 0

    return 1

def nando2_1(tmp):
    for i in range(len(tmp)-1):
        if tmp[i]+1!=tmp[i+1]:
            return 0

    return 1

def nando2_2(tmp):
    for i in range(len(tmp)-1):
        if tmp[i]-1!=tmp[i+1]:
            return 0

    return 1

def nando3(tmp):
    for i in range(len(tmp)-2):
        if tmp[i]!=tmp[i+2]:
            return 0
    return 1

def nando4(tmp):
    diff=tmp[0]-tmp[1]
    for i in range(len(tmp)-1):
        if tmp[i]-tmp[i+1]!=diff:
            return 0

    return 1

def check(start, end):

    tmp=test[start:end]
    ret=123456789
    if nando1(tmp):
        ret=1
    elif nando2_1(tmp):
        ret=2
    elif nando2_2(tmp):
        ret=2
    elif nando3(tmp):
        ret=4
    elif nando4(tmp):
        ret=5
    else:
        ret=10

    return ret

def memorize(begin):
    if begin==len(test):
        return 0

    if(cache[begin]!=-1):
        return cache[begin]
    #print cache[begin]
    cache[begin]=987654321
    for i in range(3, 6):
        if begin+i<=len(test):
            cache[begin]=min(cache[begin], memorize(begin+i)+check(begin, begin+i-1))

    return cache[begin]

print memorize(0)
