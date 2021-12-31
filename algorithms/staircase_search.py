def staircasesearch(grid, x):
    i = 0 
    j = len(grid[0]) - 1 

    while i < len(grid[0]) - 1 and j >= 0:
        print(i,j)
        if grid[i][j] == x:
            return i, j

        if grid[i][j] > x :
            j -= 1

        else:
            i += 1
    return "Not Found "

mat = [[-1,-2,-3], [-1,-2,-3]]
target = -4
solution = staircasesearch(mat, target)
print(solution)