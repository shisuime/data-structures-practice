def merge_sorted_arrays(arr1,arr2):
    sorted_list=[]
    len1=len(arr1)
    len2=len(arr2)    

    i = j = 0

    while i < len1 and j < len2 :
        if arr1[i] < arr2[j]:
            sorted_list.append(arr1[i]) 
            i +=1

        else:
            sorted_list.append(arr2[j])
            j +=1

    while i < len1:
        sorted_list.append(arr1[i])
        i+=1

    while j < len2:
        sorted_list.append(arr2[j])
        j+=1              



    return sorted_list


def merge_sort(array):
    if len(array) <=1:
        return array
    
    mid=len(array)//2
    left=array[:mid]
    right=array[mid:]

    left=merge_sort(left)
    print("left",left)
    right=merge_sort(right)
    print("right",right)
    return merge_sorted_arrays(left,right)

if __name__ == "__main__":
    # elements1=[5,8,12,56]
    # elements2=[7,9,45,51]

    # print(merge_sorted_arrays(elements1,elements2)) 

    array=[10,3,15,7,8,23,98,29]

    print(merge_sort(array))

    

