from wrapper import aoc_runner
import math

# Test data including the canonical example from the problem description
# and the user's specific edge cases.
CANONICAL_TEST = [
    "L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"
]

USER_TEST_1 = ["L150", "L50"] # Expected: 2
USER_TEST_2 = ["R150", "R50"] # Expected: 2
USER_TEST_3 = ["R150", "L50"] # Expected: 2
USER_TEST_4 = ["L150", "R50"] # Expected: 2

# We will default to the canonical test for demonstration purposes if no input is provided
TEST_DATA = CANONICAL_TEST


def establish_new_position(start_pos: int, direction: str, zero_counter: int = 0):
    """
    Part 1: Calculates the final position and counts if the final position is 0.
    """
    if direction[0] == "L":
        negative_increment = int(direction[1:])
        new_pos = (start_pos - negative_increment) % 100
    elif direction[0] == "R":
        positive_increment = int(direction[1:])
        new_pos = (start_pos + positive_increment) % 100
    else:
        raise ValueError(f"Invalid direction: {direction}")

    if new_pos == 0:
        zero_counter += 1

    return new_pos, zero_counter


def establish_new_position_2(start_pos: int, direction: str, zero_counter: int = 0):
    """
    Part 2: Calculates the final position and counts *every click* that lands on 0.
    This requires counting how many multiples of 100 are crossed during the rotation.
    """
    D = int(direction[1:])  # The distance (clicks) for this rotation
    passed_zero = 0

    print(f"\n--- Turn {direction}: Start at {start_pos} ---")

    if direction[0] == "L":
        # Left Rotation Logic (L)
        # Hits 0 when total distance D covers: start_pos, start_pos+100, start_pos+200, ...

        if start_pos == 0:
            # If starting at 0, the first hit is at 100 clicks, 
            # so we only count full 100-click circuits.
            passed_zero = D // 100
        elif D <= start_pos:
            # If distance is less than or equal to distance to 0, no full wrap occurs.
            passed_zero = 0
        else:
            # D > start_pos: At least one pass is guaranteed when passing 0.
            # 1. Count the first pass at click 'start_pos' (which lands on 0).
            passed_zero = 1
            
            # 2. Calculate remaining distance after hitting 0 once.
            remaining_dist = D - start_pos
            
            # 3. Add any subsequent full 100-click circuits.
            passed_zero += remaining_dist // 100

        raw_pos = start_pos - D
        new_pos = raw_pos % 100
        
        print(f"L Logic: D={D}, start={start_pos}. Calculated hits: {passed_zero}")

    elif direction[0] == "R":
        # Right Rotation Logic (R)
        # Hits 0 when total distance D covers: 100 - start_pos, 200 - start_pos, 300 - start_pos, ...
        # This simplifies to counting how many multiples of 100 the raw position reaches.
        
        raw_pos = start_pos + D
        new_pos = raw_pos % 100
        
        # This calculation counts every time the raw position hits 100, 200, 300, etc., 
        # including the final position if it's 0.
        passed_zero = raw_pos // 100
        
        print(f"R Logic: D={D}, start={start_pos}. Raw pos: {raw_pos}. Calculated hits: {passed_zero}")
    
    else:
        raise ValueError(f"Invalid direction: {direction}")
    
    zero_counter += passed_zero
    
    print(f"Dial moves to {new_pos}. Hits added: {passed_zero}. Total count: {zero_counter}")
    
    return new_pos, zero_counter


def part1(input_data: str | None) -> int:
    """Solve part 1: count how many times we hit position 0 *at the end of a rotation*."""
    if input_data is None:
        processed = TEST_DATA
    else:
        processed = [direction.strip() for direction in input_data.split('\n') if direction.strip()]
    
    position = 50
    zero_counter = 0
    for turn in processed:
        position, zero_counter = establish_new_position(position, turn, zero_counter)
    
    return zero_counter


def part2(input_data: str | None) -> int:
    """Solve part 2: count how many times we *click* position 0 (during or at end of rotation)."""
    if input_data is None:
        # Use user-defined tests if no file is provided, for demonstration
        processed = TEST_DATA
        print(f"--- Running Part 2 with User Test Case: {processed} ---")
    else:
        processed = [direction.strip() for direction in input_data.split('\n') if direction.strip()]
        print("\n--- Running Part 2 (Every Click on 0) ---")
    
    position = 50
    zero_counter = 0
    
    for turn in processed:
        position, zero_counter = establish_new_position_2(position, turn, zero_counter)
    
    return zero_counter

if __name__ == "__main__":

    
    
    #manual test cases:
    
    print("--- Verifying Specific Test Cases (Expected Result: 2 for all) ---")
    
    # Test 1: [L150, L50] -> Expected 2
    pos = 50
    count = 0
    for turn in USER_TEST_1:
        pos, count = establish_new_position_2(pos, turn, count)
    print(f"Result for {USER_TEST_1}: {count}\n")
    
    # Test 2: [R150, R50] -> Expected 2
    pos = 50
    count = 0
    for turn in USER_TEST_2:
        pos, count = establish_new_position_2(pos, turn, count)
    print(f"Result for {USER_TEST_2}: {count}\n")

    # Test 3: [R150, L50] -> Expected 2
    pos = 50
    count = 0
    for turn in USER_TEST_3:
        pos, count = establish_new_position_2(pos, turn, count)
    print(f"Result for {USER_TEST_3}: {count}\n")

    # Test 4: [L150, R50] -> Expected 2
    pos = 50
    count = 0
    for turn in USER_TEST_4:
        pos, count = establish_new_position_2(pos, turn, count)
    print(f"Result for {USER_TEST_4}: {count}\n")
    
    #aoc_runner(part1, part2)