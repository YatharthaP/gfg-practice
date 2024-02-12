import string

def palindrom(str1,start,end):
    if start>=end:
        return True
    return(str1[start]==str1[end] and palindrom(str1, start+1, end-1))

str1=input()
print(palindrom(str1, 0, len(str1)-1))
