'''
Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
'''
def twoSum( nums, target):
	'''
	L=nums.copy() #先排序，缩小范围再找
	nums.sort()
	for i in nums:
		if i>target:
			index=nums.index(i)
			break
		else:
			index=len(nums)
	print('index:',index)
	'''
	count1=1 #暴力破解法
	for m in nums:
		count2=count1
		for n in nums[count1:]:
			if target==(m+n):
				return(count1-1,count2)
			count2+=1
		count1+=1

nums = [0,3,3,2,7,11,1,15]
target =7
print(twoSum(nums,target))


def twoSum_dict(nums, target):
    nums_dict = {}
    for index1, number1 in enumerate(nums):
        print(index1,number1)
        number2 = target - number1
        if number2 in nums_dict:
            return nums_dict[number2] + 1, index1 + 1
        nums_dict[number1] = index1
        print(nums_dict)