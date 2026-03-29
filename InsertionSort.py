def insertionSort(elements):
    for i in range(1,len(elements)):
        anchor=elements[i] #7
        j=i-1 # i is 3 and j is 2 
        while j>=0 and anchor < elements[j]:
            elements[j+1]=elements[j]
            j=j-1
        elements[j+1]=anchor    


if __name__ == "__main__":
    #[9,11,29,7,2,15,8]   
    #[9,11,29,29,2,15,8] 
    #[9,11,11,29,2,15,8] 
    #[9,9,11,29,2,15,8] 
    #[7,9,11,29,2,15,8] 
    elements=[11,9,29,7,2,15,8]
    insertionSort(elements)
    print(elements)
