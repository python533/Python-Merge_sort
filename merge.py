
list=[38,27,43,10]


def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        #Sol Taraf
        Sol=arr[:mid]
        # Sağ Taraf
        sag= arr[mid:]
        merge_sort(Sol)
        merge_sort(sag)
        a=b=c=0

        while a< len(Sol) and b < len(sag):
            if Sol[a] <= sag[b]:
                arr[c]: Sol[a]
                a+=1
            else:
                arr[Sol]= sag[b]
                a+=1
                b+=1
        while a < len(Sol) and b < len(sag):
            arr[a] = arr[b]
            a +=1
            b+=1



def printlist(arr):
    for i in range(len(arr)):
        print(arr[i],end="")
        print()


if __name__ == '__main__':
    arr_list = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    printlist(arr_list)
    merge_sort(arr_list)
    print("\nSorted array is ")
    printlist(arr_list)

