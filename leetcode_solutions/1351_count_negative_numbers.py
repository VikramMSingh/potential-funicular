def countNegatives(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i = len(grid)-1
        j = 0
        count = 0
        while i>=0 and j< len(grid[0]):
            print(i,j)
            if grid[i][j] < 0:
                count +=len(grid[0])-j
                i -= 1
            else:
                j +=1
        return(count)

### Example
arr = [[-1,-2,-3], [-1,-2,-3]]
solution = countNegatives(arr)
print(solution)