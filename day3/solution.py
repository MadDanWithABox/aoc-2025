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

def get_biggest_k_values(battery_bank: str, k: int) -> int:
    """
    Finds the largest number formed by selecting exactly k digits from the battery_bank string.
    """
    jolt_list = [digit for digit in battery_bank] # Keep as strings
    n = len(jolt_list)
    result = []
    
    current_start_index = 0
    
    # We need to select 'k' digits in total
    for num_digits_to_select in range(k, 0, -1):
        
        search_end_index = n - num_digits_to_select
        
        best_digit = '0'
        best_index = -1
        
        # Iterate through the search window (from current_start_index up to search_end_index)
        for i in range(current_start_index, search_end_index + 1):
            digit = jolt_list[i]
            
            # greedy. Pick largest digit and in cases of a ti e pick the one on the left
            # Picking leftmost to get more space for lateer searches
            if digit > best_digit:
                best_digit = digit
                best_index = i
        result.append(best_digit)
        current_start_index = best_index + 1
        
    return int("".join(result))



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
    joltages = []
    for bank in bat_banks:
        joltages.append(get_biggest_k_values(bank, 12))
        
    return sum(joltages)



if __name__ == "__main__":
    aoc_runner(part1, part2)