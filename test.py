#inp=['x', 'b', 'w', 'w', 'b']
#inp=['x', 'b', 'w', 'x', 'w', 'b', 'b', 'w', 'b']
#inp=['x', 'x', 'w', 'w', 'w', 'b', 'x', 'w', 'x', 'w', 'b', 'b', 'b', 'w', 'w', 'x', 'x', 'x', 'w', 'w', 'b', 'b', 'b', 'w', 'w', 'w', 'w', 'b', 'b']
inp=['b']
tmp=[]

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
    inp=inp[0]

listing(inp)
Decompress()
print inp
