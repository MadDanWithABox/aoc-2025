from wrapper import aoc_runner
from typing import List
from functools import reduce

import operator


TEST_DATA = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """

def parse(data_str):
    "splits input data string into a 2D vector of rolls and gaps"
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


if __name__ == "__main__":
    aoc_runner(part1, part2)