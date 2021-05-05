def selection(nums):
    for i in range(len(nums)-1):
        min=i
        for j in range(i,len(nums)):
            if nums[j]<nums[min]:
                min=j
        temp=nums[i]
        nums[i]=nums[min]
        nums[min]=temp
n=[1,5,78,2,9,57,93,90]
selection(n)
print(n)