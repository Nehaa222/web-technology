nums=[1, 2, 3, 4, 5, 6, 7, 8, 9]
nums_copy = nums
nums.append("z")
del nums[5]
nums.remove("z")
print(len(nums))
print(nums_copy)
for i in nums:
    print (i)
list1=[1,2,3,[3.1,3.2,3.3],4,5]
print(list1[3][2])
L=['a',['bb',['ccc','ddd'],'ee','ff'],'g','h']
print(L[1][3] )

nums=[1, 2, 3, 4, 5, 6, 7, 8, 9]
sum=0
for i in nums:
    sum=sum+i
print(sum) 

a=(10,)
print(type(a))

nums=[2,4,6]
nums_sqr=[]
for i in nums:
    nums_sqr.append(i**2)
print(nums_sqr)

print([i**2 for i in nums])
numbers=[1,2,3,4,5]
even_numbers=[x for x in numbers if x%2==0]
print(even_numbers)






