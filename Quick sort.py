def swap(a,b,arr):
    if a!=b:
        arr[a],arr[b]=arr[b],arr[a]
def quicksort(elements, start, end):
    if start < end:
        pi = parition(elements, start, end)
        quicksort(elements, start, pi-1)
        quicksort(elements, pi+1, end)

def parition(list,start,end):
    piviot=start
    pivot=list[piviot]
    while start<end:
        while start<len(list) and list[start]<=pivot:
            start+=1
        while list[end]>pivot:
            end-=1
        if start<end:
            swap(start,end,list)
    swap(piviot,end,list)
    return end

if __name__ == '__main__':
   tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
   for elements in tests:
       quicksort(elements, 0, len(elements)-1)
       print(f'sorted array: {elements}')
