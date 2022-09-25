import re
def fun(s):
    pattern="^[a-zA-Z0-9\-\_]+@[A-Za-z0-9]+[\.][a-zA-Z]{1,3}$"
    return re.search(pattern,s)!=None
def filter_mail(emails):
    return list(filter(fun, emails))
