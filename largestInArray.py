def largest_element(array):
    max_element=max(array)
    return max_element

def second_largest(array):
    sorted_array= sorted(array,reverse=True)
    return sorted_array[1]
 

if __name__ == "__main__":
    array=[1,12,3,41,8]
    print('Largest Element',largest_element(array))
    print('Second Largest Array', second_largest(array))
    # print(list(enumerate(array)))
    

