from wrapper import aoc_runner

TEST_DATA = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def parse(data_str):
    "splits input data string into a 2D vector of rolls and gaps"
    rows = data_str.split("\n")
    cells = [list(r) for r in rows]
    return cells


def count_at_neighbors(grid, row, col):
    """
    Counts the number of '@' characters in the 8-directional Moore neighborhood
    of the cell at (row, col).

    Args:
        grid (list[list[str]]): The 2D grid .
        row (int): The row index of the central cell.
        col (int): The column index of the central cell.

    Returns:
        int: The total count of '@' neighbors.
    """
    
    # Define the 8 relative offsets (Delta_r, Delta_c) for the Moore neighborhood
    offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    at_count = 0
    num_rows = len(grid)    # Should be 10
    num_cols = len(grid[0]) # Should be 10

    for dr, dc in offsets:
        # Calculate the coordinates of the potential neighbor
        neighbor_r = row + dr
        neighbor_c = col + dc

        # ensure the neighbor's row index is within the grid bounds (0 to num_rows-1)
        # Ensure the neighbors col index is within the grid bounds (0 to num_cols-1)
        is_valid_r = 0 <= neighbor_r < num_rows
        is_valid_c = 0 <= neighbor_c < num_cols

        if is_valid_r and is_valid_c:
            if grid[neighbor_r][neighbor_c] == '@':
                at_count += 1

    return at_count

def process_roll_rack(input_grid, threshold=8):
    num_rows = len(input_grid)
    if num_rows == 0:
        return []
    low_count_positions = 0
    num_cols = len(input_grid[0])
    result_grid = [[0] * num_cols for _ in range(num_rows)]

    for row in range(num_rows):
        for col in range(num_cols):
            if input_grid[row][col] == '@':
                count = count_at_neighbors(input_grid, row, col)
                result_grid[row][col] = count
                if count < threshold:
                    low_count_positions += 1
    return result_grid, low_count_positions


def iterate_roll_rack(current_grid, threshold=4):
    """
    Performs a single simulation pass over the grid.

    It calculates the state of the next grid based entirely on the current grid
    and returns the new grid and the number of changes made.
    """
    num_rows = len(current_grid)
    if num_rows == 0:
        return current_grid, 0
    num_cols = len(current_grid[0])
    
    # Initialize the next grid as a copy of the current grid.
    next_grid = [row[:] for row in current_grid] # Deep copy the grid
    rolls_removed = 0

    for r in range(num_rows):
        for c in range(num_cols):
            
            current_cell_value = current_grid[r][c]

            if current_cell_value == '@':
                neighbor_count = count_at_neighbors(current_grid, r, c)
                
                if neighbor_count < threshold:
                    next_grid[r][c] = '.'
                    rolls_removed += 1
                    
    return next_grid, rolls_removed

def get_elves_moving_rolls(current_grid, threshold=4):
    """
    Runs the full simulation until the grid stabilizes (0 changes in a pass).
    
    Returns the final stable grid and the total number of iterations.
    """
    
    iteration = 0
    total_changes = 0
    
    while True:
        iteration += 1
        
        new_grid, changes_in_pass = iterate_roll_rack(current_grid, threshold)
        
        print(f"--- Iteration {iteration} ---")
        print(f"Changes this pass: {changes_in_pass}")
        
        if changes_in_pass == 0:
            # If no changes were made, the grid is stable.
            print("\nGrid stabilized.")
            break
        
        # Update the grid for the next iteration
        current_grid = new_grid
        total_changes += changes_in_pass
        
    return current_grid, iteration, total_changes



def part1(input_data: str| None):
    if input_data == None:
        input_data = TEST_DATA

    input_grid = parse(input_data)
    roll_neighbour_count, accessible_rolls = process_roll_rack(input_grid, threshold=4)
    return accessible_rolls



        
def part2(input_data: str| None):
    if input_data == None:
        input_data = TEST_DATA
    input_grid = parse(input_data)
    result, iteration, total_changes = get_elves_moving_rolls(input_grid)
    return total_changes
        



if __name__ == "__main__":
    aoc_runner(part1, part2)