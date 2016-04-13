#inp=['x', 'b', 'w', 'w', 'b']
#inp=['x', 'b', 'w', 'x', 'w', 'b', 'b', 'w', 'b']
inp=['x', 'x', 'w', 'w', 'w', 'b', 'x', 'w', 'x', 'w', 'b', 'b', 'b', 'w', 'w', 'x', 'x', 'x', 'w', 'w', 'b', 'b', 'b', 'w', 'w', 'w', 'w', 'b', 'b']
#inp=['b']
tmp=[]
str=''

def listing(inp):
    for i in range(len(inp)):
        if inp[i]=='x':
            tmp.append(i)

    tmp.reverse()

def Decompress():
    global inp
    for i in tmp:
        temp=inp[i+1:i+5]
        inp[i:i+5]=[]
        inp.insert(i, temp)

def Reverse(l):
    l[0], l[2]=l[2], l[0]
    l[1], l[3]=l[3], l[1]
    print l
    for i in l:
        try:
            j=i+'1'
        except:
            l[l.index(i)]=Reverse(i)

    return l



def Compress(l):
    global str
    for i in l:
        try:
            str+=i
            #print i
        except:
            str+='x'
            Compress(i)


listing(inp)
Decompress()
#print inp
print Reverse(inp[0])
Compress(list(inp))
print str
