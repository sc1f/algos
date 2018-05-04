def binary_search(nums, target):
	lo, hi = 0, len(nums) - 1
	while lo < hi:
		mid = (hi + lo) // 2
		if nums[mid] == target:
			return True
		elif nums[mid] < target:
			lo = mid + 1
		else:
			hi = mid - 1
	return False

def rbs(nums, target):
	low, high = -1, len(nums)
	return bs(nums, target, low, high)

def bs(nums, target, low, high):
	if low + 1 == high:
		return 
	mid = (high + low) // 2
	if nums[mid] == target:
		return mid
	elif nums[mid] > target:
		return bs(nums, target, low, mid)
	else:
		return bs(nums, target, mid, high)

print(rbs([1,2,3,4,5], 2))