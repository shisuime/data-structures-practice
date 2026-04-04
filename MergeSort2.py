def merge_sorted_arrays(arr1,arr2,arr,key,descending):
    # sorted_list=[]
    len1=len(arr1)
    len2=len(arr2)    

    i = j = k = 0

    while i < len1 and j < len2 :
        if (arr1[i][key] > arr2[j][key]) == descending:
            # sorted_list.append(arr1[i]) 
            arr[k]=arr1[i]
            i +=1

        else:
            # sorted_list.append(arr2[j])
            arr[k]=arr2[j]
            j +=1
        k+=1
    while i < len1:
        # sorted_list.append(arr1[i])
        arr[k]=arr1[i]
        i+=1
        k+=1

    while j < len2:
        # sorted_list.append(arr2[j])
        arr[k]=arr2[j]
        j+=1 
        k+=1             



    # return sorted_list


def merge_sort(array,key,descending=False):
    if len(array) <=1:
        return array
    
    mid=len(array)//2
    left=array[:mid]
    right=array[mid:]

    # left=merge_sort(left)
    
    # right=merge_sort(right)

    merge_sort(left, key, descending)
    merge_sort(right, key, descending)
    
    # return merge_sorted_arrays(left,right)
    merge_sorted_arrays(left,right,array,key,descending)

if __name__ == "__main__":
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    # print(merge_sort(array))
    # merge_sort(elements, key='name', descending=True)
    merge_sort(elements, key='name')
    print(elements)

    

