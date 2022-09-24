
def Cube_Block(n,l):
    condition = 'Yes'
    for j in range(int(n // 2)):
        if max(int(l[j]), int(l[-j - 1])) < min(int(l[j + 1]), int(l[-j - 2])):
            condition = 'No'
    return condition