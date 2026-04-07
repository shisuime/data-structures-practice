def shell_sort(arr):
    size=len(arr) #9
    gap=size //2 #4
    
    while gap > 0:
        for i in range(gap,size): #i=8
            anchor=arr[i] #9
            j=i #8
            while j >= gap and arr[j-gap] > anchor: #21 > 9
                arr[j]=arr[j-gap] #arr[8]=21 ==> [21,38,11,17,21,38,29,32,9]
                j-=gap #j=6-4 ==>2

            arr[j]=anchor  #arr[2]=11 ==>[4,38,11,17,21,38,29,32,9]
        gap=gap //2

if __name__ == "__main__":
    elements=[21,38,29,17,17,4,25,11,11,32,9]
    shell_sort(elements)
    print(elements)

