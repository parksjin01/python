import copy

moveX=[[-1, 0, 0], [0, 0, 1], [-1, 0, 0], [0, 0, 1], [-1, 0, 0], [0, 1, 1], [0, 0, 1], [0, -1, -1],[0, 1, 1], [-1, 0, 0], [0, -1, -1], [0, 0, 1]]
moveY=[[0, 0, 1], [1, 0, 0], [0, 0, -1], [-1, 0, 0], [-1, -1, 0], [0, 0, 1], [0, -1, -1], [0, 0, 1], [0, 0, -1], [1, 1, 0], [0, 0, -1], [0, 1, 1]]

def isCovered(map):
    for i in map:
        for j in i:
            if j=='.':
                return 0

    return 1

def isStar(map):
    y=0
    x=0
    for i in map:
        for j in i:
            if j=='.':
                return y, x
            x+=1
        y+=1
        x=0

def boardCover(x1, y1, x2, y2, x3, y3, map):
    cnt=0
    tmp=map[:]
    if(x1<0 or x1>len(tmp[0])):
        return 0

    if(x2<0 or x2>len(tmp[0])):
        return 0

    if(x3<0 or x3>len(tmp[0])):
        return 0

    if(y1<0 or y1>len(tmp)):
        return 0

    if(y2<0 or y2>len(tmp)):
        return 0

    if(y3<0 or y3>len(tmp)):
        return 0

    if(tmp[y1][x1]=='#' or tmp[y2][x2]=='#' or tmp[y3][x3]=='#'):
        return 0

    tmp[y1][x1]='#'
    tmp[y2][x2]='#'
    tmp[y3][x3]='#'
    try:
        y1, x1=isStar(tmp)
        for i in range(len(moveX)):
            cnt+=boardCover(x1+moveX[i][0], y1+moveY[i][0], x1+moveX[i][1], y1+moveY[i][1], x1+moveX[i][2], y1+moveY[i][2], copy.deepcopy(tmp))
    except:
        if(1 == isCovered(tmp)):
           return 1
    return cnt

map=[]
map.append('# # # # # # # # # #'.split(' '))
map.append('# . . . . . . . . #'.split(' '))
map.append('# . . . . . . . . #'.split(' '))
map.append('# . . . . . . . . #'.split(' '))
map.append('# . . . . . . . . #'.split(' '))
map.append('# . . . . . . . . #'.split(' '))
map.append('# . . . . . . . . #'.split(' '))
map.append('# # # # # # # # # #'.split(' '))

res=0
ttt=[]
for i in range(len(moveX)):
        print ttt, map
        y, x=isStar(copy.deepcopy(map))
        ttt.append(boardCover(x+moveX[i][0], y+moveY[i][0], x+moveX[i][1], y+moveY[i][1], x+moveX[i][2], y+moveY[i][2], copy.deepcopy(map)))

print sum(ttt)