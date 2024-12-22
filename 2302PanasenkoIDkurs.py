import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_grid(size):
    grid = [[0 for _ in range(size)] for _ in range(size)]

    grid[4][4] = 1
    grid[2][4] = 1
    grid[3][4] = 1
    grid[5][4] = 1
    grid[6][4] = 1
    grid[7][4] = 1
    grid[5][5] = 1
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join('█' if cell else ' ' for cell in row))
    print()

def count_neighbors(grid, x, y):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx, ny = (x + i) % len(grid), (y + j) % len(grid[0])
            total += grid[nx][ny]
    return total

def update(grid):
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors = count_neighbors(grid, i, j)

            if grid[i][j] == 1:  
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0  
                else:
                    new_grid[i][j] = 1  
            else: 
                if neighbors == 3:
                    new_grid[i][j] = 1  
    return new_grid

def main():
    size = 10  
    grid = initialize_grid(size)
    previous_states = set()
    
    while True:
        clear_screen()
        print_grid(grid)

        grid_tuple = tuple(tuple(row) for row in grid)

        if grid_tuple in previous_states:
            print("Игра окончена: конфигурация повторилась.")
            break
        
        previous_states.add(grid_tuple)
        
        grid = update(grid)
        time.sleep(0.5)

        if not any(any(cell == 1 for cell in row) for row in grid):
            print("Игра окончена: нет живых клеток.")
            break

        if grid == update(grid):  
            print("Игра окончена: стабильная конфигурация.")
            break

if __name__ == "__main__":
    main()