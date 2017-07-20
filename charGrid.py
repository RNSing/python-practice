grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#print(grid[0][0], end='')
#print(grid[1][0], end='')
#print(grid[2][0], end='')
#print(grid[3][0], end='')
#print(grid[4][0], end='')
#print(grid[5][0], end='')
#print(grid[6][0], end='')
#print(grid[7][0], end='')
#print(grid[8][0], end='')

n = 0 
while True:
    for i in range(0,9):
        print(grid[i][n], end='')
    print('')
    n += 1
    if n == 6:
        break
    



    
