from wrapper import aoc_runner

TEST_DATA = """987654321111111
811111111111119
234234234234278
818181911112111"""

def get_banks(data_str:str):
    battery_banks = data_str.split("\n")
    print(f"there are {len(battery_banks)} battery banks")

def get_biggest_values(battery_bank: str):
    """
    Given a string representation of a battery bank, i.e. "1234", returns the largest joltage possible
    Returns: int """

def part1(input_data: str| None):
    joltages = []
    if input_data == None:
        input_data = TEST_DATA
    bat_banks = get_banks(input_data)
    for bank in bat_banks:



def part2(input_data: str| None):
    if input_data == None:
        input_data = TEST_DATA
    bat_banks = get_banks(input_data)



if __name__ == "__main__":
    aoc_runner(part1, part2)