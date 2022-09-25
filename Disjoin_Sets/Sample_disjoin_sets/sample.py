# Enter your code here. Read input from STDIN. Print output to STDOUT
def disj(l,A,B):
    a=set(A)
    b=set(B)
    count=0
    for i in l:
        if i in a:
            count=count+1
        if i in b:
            count=count-1
    return count