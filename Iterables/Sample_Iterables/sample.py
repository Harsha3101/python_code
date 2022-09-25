# Enter your code here. Read input from STDIN. Print output to STDOUTimport math
import math

def Iterables(size,input,K):
    Cnt = len(list(filter(lambda x: x == "a",input)))
    total = math.comb(size,K)
    withoutA = math.comb(size - Cnt, K)
    result = 1 - withoutA/total
    return "{0:.3f}".format(result)