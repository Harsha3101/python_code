
def Word_order(k,j):
    n = {}
    l=[]
    for i in range(k):
        count=1
        if j[i] in n:
            n[j[i]] += 1
        else:
            n[j[i]]=1

    for a in n:
        l.append(n[a])

    return l