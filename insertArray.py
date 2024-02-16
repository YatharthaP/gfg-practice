# The goal is to insert an element in an array. Will try to use different ways rather then the in-built functions. 

#method one // using insert method
# def insert_element(array,index,element):
#     array.insert(index,element)
#     return array

#method two
def insert_element(array, index, element):
    for i in range(index,len(array)):
        array[i] = array[i-1]

    array[index] = element


if __name__=='__main__':
    array=[1,2,3,4,5]
    index=3
    element= 7
    insert_element(array,index,element)
    print("Array after insertion",array)