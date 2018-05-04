def count_countries(grid, n, m):
	count = 0 
	if not grid:
		return count
	for row_num in range(n):
		for col_num in range(m):
			if grid[row_num][col_num] != "#":
				color = grid[row_num][col_num]
				dfs(grid, row_num, col_num, color)
				count += 1
	return count


def dfs(grid, row, col, color):
	if not_valid(grid, row, col, color):
		return
	current_color = grid[row][col]
	grid[row][col] = "#"
	dfs(grid, row + 1, col, current_color)
	dfs(grid, row - 1, col, current_color)
	dfs(grid, row, col + 1, current_color)
	dfs(grid, row, col - 1, current_color)
	
def not_valid(grid, row, col, color):
	return (row < 0) or (row >= len(grid)) or (col < 0) or (col >= (len(grid[0]))) or (grid[row][col] == "#") or (grid[row][col] != color)

if __name__ == "__main__":
	grid = [
		[5,4,4],
		[4,3,4],
		[3,2,4],
		[2,2,2],
		[3,3,4],
		[1,4,4],
		[4,1,1]
	]
	n = len(grid)
	m = len(grid[0])
	print(count_countries(grid, n, m))