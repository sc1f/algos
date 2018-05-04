def count_islands(grid):
    if not grid:
        return 0

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
        	# find the first 1, and start counting
            if grid[i][j] == 1:
            	# once we return back out of the count, increment and keep going
                dfs(grid, i, j)
                count += 1
    return count

def dfs(grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
        return
    grid[i][j] = '#'
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)

if __name__ == "__main__":
	grid = [
		[1,0,0,1],
		[0,1,1,1],
		[1,1,0,0]
	]
	print(count_islands(grid))

