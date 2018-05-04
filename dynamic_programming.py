def find_partition(nums):
	s = sum(nums)
	# if the sum is odd, then we can't partition it into 2
	if s % 2 != 0:
		return False

	return find_subset_sum(nums, len(nums), s // 2)

def find_subset_sum(nums, n, sum):
	if sum == 0:
		return True
	if n == 0 and sum != 0:
		return False

	if nums[n - 1] > sum:
		return find_subset_sum(nums, n-1, sum)
	# consider without last element and with last element
	return find_subset_sum(nums, n-1, sum) or find_subset_sum(nums, n-1, sum-nums[n-1])
	

print(find_partition([15, 5, 20, 10, 35, 25, 10]))