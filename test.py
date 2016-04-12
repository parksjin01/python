input=[7, 1, 5, 9, 6, 7, 3]
max=0

def checker(tmp, value):
    for i in tmp:
        if i<value:
            return 0

    return len(tmp)*value

for v in input:
    for i in range(len(input)):
        for j in range(i, len(input)):
            tmp=checker(input[i:j], v)

            if max<tmp:
                max=tmp

print max