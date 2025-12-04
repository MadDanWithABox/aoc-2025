from wrapper import aoc_runner

TEST_DATA = """987654321111111
811111111111119
234234234234278
818181911112111"""

def get_banks(data_str:str):
    battery_banks = data_str.split("\n")
    print(f"there are {len(battery_banks)} battery banks")
    return battery_banks

def get_biggest_values(battery_bank: str):
    """
    Given a string representation of a battery bank, i.e. "1234", returns the largest joltage possible
    Returns: int """
    jolt_list = [int(digit) for digit in battery_bank]

    biggest_joltage = max(jolt_list[:-1])
    prim_index = jolt_list.index(biggest_joltage)
    sec_joltage = None
    sec_index = None
    for i, joltage in enumerate(jolt_list):
        if sec_joltage is None or joltage >= sec_joltage:
            if i > prim_index:
                sec_joltage = joltage
                sec_index = i
    return int(f"{biggest_joltage}{sec_joltage}")

def part1(input_data: str| None):
    joltages = []
    if input_data == None:
        input_data = TEST_DATA
    bat_banks = get_banks(input_data)
    for bank in bat_banks:
        joltages.append(get_biggest_values(bank))
    return sum(joltages)
        




def part2(input_data: str| None):
    if input_data == None:
        input_data = TEST_DATA
    bat_banks = get_banks(input_data)



if __name__ == "__main__":
    aoc_runner(part1, part2)