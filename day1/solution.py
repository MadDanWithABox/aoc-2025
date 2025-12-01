from wrapper import aoc_runner

TEST_DATA = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]


def establish_new_position(start_pos: int, direction: str, zero_counter: int = 0):
    """
    Inputs: takes a starting position, a stringbased direction for turning a dial, and an optional counter
    Returns: the adjusted position, having applied the direction, and optionally updated counter.
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


def part1(input_data: str | None) -> int:
    """Solve part 1: count how many times we hit position 0."""
    # Use test data if no input file provided
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
    """Solve part 2: (to be implemented)"""
    # Your part 2 solution goes here
    pass


if __name__ == "__main__":
    aoc_runner(part1, part2)