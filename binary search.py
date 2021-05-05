pos=0
def search(p,n):
    l=0
    u=len(p)
    while l<=u:
        mid=(l+u)//2
        if p[mid]==n:
            globals()['pos']=mid
            print('the number',n,'found at position',pos+1 )
            break
        else:
            if p[mid]<n:
                l=mid
            else:
                u=mid

nums=[1,2,3,4,5,6,7,8,9,10,12,34,47,48,48,49,56,57,59,67,68,69,78,79,81,85,87,90,100]
n=48
a=search(nums,n)

