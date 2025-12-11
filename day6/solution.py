from wrapper import aoc_runner
from typing import List
from functools import reduce
from itertools import zip_longest

import operator


TEST_DATA = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """

def parse(data_str):
    rows = data_str.split("\n")
    grid = []
    for row_str in rows:
        elements = [element for element in row_str.split() if element]
        grid.append(elements)

    return grid

def construct_sums(grid_of_strs):
    # assume all grids are the same length
    sums = []
    num_of_sums_to_construct = len(grid_of_strs[0])
    num_of_terms = len(grid_of_strs)
    for i in range(num_of_sums_to_construct):
        calc = []
        for j in range(num_of_terms):
            calc.append(grid_of_strs[j][i])
        sums.append(calc)
    return sums


def apply_operator_to_list(operator_symbol, data_list):
    """
    Selects an operation based on a string symbol and applies it across a list of integers."""
    operation_map = {
        '*': operator.mul, 
        '+': operator.add,  
        '-': operator.sub,
        '/': operator.truediv,
    }
    operation_func = operation_map.get(operator_symbol)

    if operation_func is None:
        raise ValueError(f"Unsupported operator symbol: {operator_symbol}")
    try:
        result = reduce(operation_func, data_list)
    except Exception as e:
        print(e)

    return result

def compute_calc(calc: List[str]):
    str_list = calc[:-1]
    operation = calc[-1]

    data_list = []
    for i in str_list:
        data_list.append(int(i))


    return apply_operator_to_list(operation, data_list)

def compute_cephalopod_calc(calc: List[str]):
    """
    Given a column of numbers and an operator as strings:
    ['123', '45', '6', '*']
    extracts the operator
    parses the numbers columnwise
    returns the calculation
    
    Process:
    We need to reverse the numbers, because cephalopod math reads from the RHS.
    123 -> 321. 45 -> 54. 6 -> 6

    Now we need to construct based on character position (these are still strings)
    based on zeroth character, we take "321"[0] == 3, then "54"[0] == 5 then "6"[0] == "356"
    then the first character, so "321"[1]=="2", "54"[1] == "4", "6"[1] is out of range, so we ignore that. == "24"
    Then the second character, the only num_str which has a value is "321"[1] == "1"
    So we should return [356, 24, 1], ["*"]
    
    """
    operator_symbol = calc[-1]
    number_strings = calc[:-1]
    max_len = max(len(s) for s in number_strings)
    padded_slices = [s.ljust(max_len, ' ') for s in number_strings]
    reversed_slices = [s[::-1] for s in padded_slices]

    # 3. Transpose (read columnwise) to reconstruct the new numbers
    new_number_components = []
    
    # zip_longest(321, 54, 6) will produce:
    # ('3', '5', '6') -> The digits for the first new number (356)
    # ('2', '4', ' ') -> The digits for the second new number (24)
    # ('1', ' ', ' ') -> The digits for the third new number (1)
    for digits in zip_longest(*reversed_strings, fillvalue=' '):
        # Concatenate the digits, ignoring padding spaces
        new_number_str = "".join(d.strip() for d in digits if d.strip())

        if new_number_str:
            new_number_components.append(new_number_str)
    data_list = []
    for i in new_number_components:
        data_list.append(int(i))
    print(calc)
    print(data_list)
    print(operator_symbol)
    return apply_operator_to_list(operator_symbol, data_list)

def part1(input_data: str | None) -> int:
    if input_data is None:
        input_data = TEST_DATA
    grid = parse(input_data)
    calcs = construct_sums(grid)
    results = []
    for calc in calcs:
        results.append(compute_calc(calc))
    return sum(results)




def part2(input_data: str | None) -> int:
    if input_data is None:
        input_data = TEST_DATA
    grid = parse(input_data)
    columns = construct_sums(grid)
    results = []
    for calc in columns:
        results.append(compute_cephalopod_calc(calc))
    return sum(results)


if __name__ == "__main__":
    aoc_runner(part1, part2)