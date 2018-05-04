def mergesort(nums):
	if len(nums) <= 1:
		# already sorted
		return

	# split into 2
	mid = len(nums) // 2
	left = nums[:mid]
	right = nums[mid:]

	# recursively split
	mergesort(left)
	mergesort(right)

	# start merging
	merge(left, right, nums)

	return nums

def merge(left, right, nums):
	index = 0
	while left and right:
		# sort
		if right[0] < left[0]:
			nums[index] = right.pop(0)
		else:
			nums[index] = left.pop(0)
		index += 1

	# clear lists that are left
	while left:
		nums[index] = left.pop(0)
		index += 1

	while right:
		nums[index] = right.pop(0)
		index += 1

print(mergesort([1,44,5,2,1,3]))