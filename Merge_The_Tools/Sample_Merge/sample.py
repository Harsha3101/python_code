def merge_the_tools(string, k):
    l=[]
    for i in range(0, len(string), k):
        t = string[i:i + k]
        result = str(t[0])
        for j in range(k):
            if t[j] not in result:
                result += t[j]
        l.append(result)
    return l