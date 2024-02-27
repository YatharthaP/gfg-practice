def maxIndexDiff(self,a, n): 
    ##Your code here
    max=0
    if n==2 and a[0]<a[1]:
        return 1
    else :
        
        for i in range(n):
            for j in range(i+1,n):
                if a[i]<=a[j] and i<=j and j-i>max:
                    max=j-i
                    
    return max

if __name__ == "__main__":
    a=[1,12,3,41,8]
    n=len(a)
    print('')

    # print(list(enumerate(array)))

#This code is not yet complete, and will give problem during execution. 
