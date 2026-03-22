def BinarySearch(list,number_to_find):
    left_index=0
    right_index=len(list) - 1
    mid_index= 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number=list[mid_index]

        if mid_number == number_to_find:
            return mid_index
        
        if mid_number < number_to_find:
            left_index= mid_index + 1

        else:
            right_index = mid_index - 1

    return -1   

def BinarySearchRecursive(list,number_to_find,left_index,right_index):
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    mid_number=list[mid_index]

    if mid_number == number_to_find:
        return mid_index
    
    if mid_number < number_to_find:
        left_index= mid_index +1
    else:
        right_index = mid_index -1

    return BinarySearchRecursive(list,number_to_find,left_index,right_index)        


def findOccurances(list,number_to_find):
    index=BinarySearch(list,number_to_find)
    indices=[index]

    i=index-1

    while i >=0:
        if list[i] == number_to_find:
            indices.append(i)
            break
        i= i - 1

    i=index + 1

    while i < len(list):
        if list[i] == number_to_find:
            indices.append(i)
            break

        i = i + 1    

    return sorted(indices)     



if __name__ == "__main__":


    # numberList=[12,15,16,19,21,24,45,67]
    # numberList=[1,4,6,9,10,5,7]
    numberList=[1,4,6,9,11,15,15,15,17,21,34,34,56]

    # index=BinarySearch(numberList,67)
    # index=BinarySearchRecursive(numberList,5,0,len(numberList)-1)

    # print(f"number found at {index} using binary search")
    result= findOccurances(numberList,15)
    print("result",result)




