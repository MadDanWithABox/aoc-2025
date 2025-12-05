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

def part1(input_data: str| None):
    if input_data == None:
        input_data = TEST_DATA
        print(parse(input_data))

        
def part2(input_data: str| None):
    if input_data == None:
        input_data = TEST_DATA
        



if __name__ == "__main__":
    aoc_runner(part1, part2)