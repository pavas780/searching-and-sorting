def insertionsort(list):
    for i in range(1,len(list)):
        anchor=list[i]
        j=i-1
        sum=0
        while j>=0 and anchor<list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=anchor


if __name__=='__main__':
    list=[2, 1, 5, 7, 2, 0, 5]

    insertionsort(list)
    print(list)