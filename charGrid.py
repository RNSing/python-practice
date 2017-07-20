#charGrid.py
#Here is one method that I used to solve the Character Grid problem from
#the book Automate The Boring Stuff with Python

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

n = 0 
while True: #Here I set up an "infinity" loop
    for i in range(0,9):
        print(grid[i][n], end='')
    print('')
    n += 1
    if n == 6: #If statement to end the "infinity" loop
        break
    



    
