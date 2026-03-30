def insert_to_sorted(array, key):
    index=place_to_insert(array,key)
    return array[0:index] + [key] +array[index:]


def place_to_insert(array,key):
    index=0
    for i in array:
        if i > key:
            break
        else:
            index +=1
    return index

if __name__ == "__main__":
    #array = [2, 1, 5, 7, 2, 0, 5]   

    stream=[]

    count=0

    while(True):
        i = int(input())
        count +=1

        stream=insert_to_sorted(stream,i)

        if count % 2 ==1:
            print(f"Median of {stream} : {stream[count//2]}")
        else:
            l1=count//2
            l2=count//2 -1 

            print(f"Median of {stream} : {stream[l1] + stream[l2] //2}")
