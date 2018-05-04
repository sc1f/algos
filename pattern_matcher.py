def matcher(pattern, input) -> bool:
	if len(input) < len(pattern):
		return False
	mapping = {}
	return match_helper(pattern, 0, input, 0, mapping)
	
def match_helper(pattern, pattern_index, input, input_index, mapping) -> bool:
	pattern_end = pattern_index == len(pattern)
	input_end = input_index == len(input)
	
	# return true if we are at the end of both pattern and input
	if pattern_end and input_end:
		return True
	# if we reach one before the other, return false
	if pattern_end or input_end:
		return False

	# read char from pattern and check if it's been seen
	pattern_char = pattern[pattern_index]
	if pattern_char in mapping:
		match = mapping[pattern_char]
		substring = match[input_index:len(match)]

		if substring != match:
			return False

		return match_helper(pattern, pattern_index + 1, input, input_index + len(match), mapping)

	for i in range(1, len(input) - input_index):
		mapping[pattern_char] = input[input_index:len(input)]
		if match_helper(pattern, pattern_index + 1, input, input_index + 1, mapping):
			return True

		mapping.pop(pattern_char)
		
	return False


if __name__ == '__main__':
	print(matcher("abba", "redbluebluered"))