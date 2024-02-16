# We are given length of rope(N). We have to find max number of pieces which we can get by cutting the rope in length exactly mathcing wither a, b, or c.
# Eg. n=5, a=2,b=5, c=1. Answer = 5. 

def maxCuts(n,a,b,c):
    if (n==0):
        return 0
    if (n<0):
        return -1
    result=max(maxCuts(n-a,a,b,c),max(maxCuts(n-b,a,b,c),maxCuts(n-c,a,b,c)))
    if result == -1:
        return -1
    return result

n=23
a=11
b=9
c=12
print(maxCuts(n,a,b,c))
