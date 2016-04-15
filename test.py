test=map(int, raw_input().split(' '))
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

def check(tmp):
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


def cal(tmp, num):
    m=12345678912345
    if len(tmp)<=2:
        return 123456789
    elif len(tmp)<=5:
        return check(tmp)

    for i in range(3, 6):
        m=min(m, cal(tmp[:num], i)+cal(tmp[num:], i))

    return m

mmm=12345678
for i in range(3, 6):
    for j in range(3, 6):
        mmm=min(mmm, cal(test[:i], j)+cal(test[i:], j))

print mmm