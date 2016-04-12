input=[7, 1, 5, 9, 6, 7, 3]

def fence(left, right):
    if left==right:
        return input[left]
    mid=left+right
    mid=mid/2
    ret=max(fence(left, mid), fence(mid+1, right))
    height=min(input[mid], input[mid+1])
    ret=max(ret, height*2)
    lo=mid
    hi=mid+1
    while(left<lo or hi<right):
        if hi<right and (lo==left or input[lo-1]<input[hi+1]):
            hi+=1
            height=min(height, input[hi])
        else:
            lo-=1
            height=min(height, input[lo])
        ret=max(ret, (hi-lo+1)*height)
    return ret


print fence(0, len(input)-1)
