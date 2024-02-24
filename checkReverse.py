def checkReverse(array):
    if array==sorted(array):
        return True
    
if __name__=="__main__":
    arr=[1,12,3,4,5,4,1]
    if checkReverse(arr):
        print('Array is sorted')
    else:
        print('Not Sorted')