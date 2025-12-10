from wrapper import aoc_runner

TEST_DATA = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

def parse(data_str):
    "splits input data string into a 2D vector of rolls and gaps"
    rows = data_str.split("\n")
    fresh_ranges = []
    ingredients = []
    for element in rows:
        if "-" in element:
            range_start = int(element.split("-")[0])
            range_end = int(element.split("-")[1])
            fresh_ranges.append((range_start, range_end))
        elif element == "":
            pass
        else:
            ingredients.append(int(element))
    
    return fresh_ranges, ingredients

def merge_overlapping_ranges(ranges):
    """
    Merges a list of inclusive, potentially overlapping ranges into a minimal
    set of non-overlapping ranges.

    Args:
        ranges (list of tuples): A list of (start, end) inclusive ranges.

    Returns:
        list of tuples: A minimal list of non-overlapping (start, end) ranges.
    """
    if not ranges:
        return []

    # Step 1: Sort the intervals by their start point.
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    merged_list = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        last_merged_start, last_merged_end = merged_list[-1]

        # Overlap occurs if the current range's start is less than or equal to the last end
        if current_start <= last_merged_end:

            # The new end is the maximum of the two original end points.
            new_end = max(last_merged_end, current_end)
            
            # Replace the last element in the merged_list with the new, combined interval
            merged_list[-1] = (last_merged_start, new_end)
        else:
            # No overlap
            merged_list.append((current_start, current_end))

    return merged_list

def is_ingredient_fresh(ingredient_id, freshness_ranges):
    """
    Checks if a given number is contained within any of the ranges in a 
    list of non-overlapping, inclusive ranges.

    Args:
        number (int/float): The value to check.
        merged_ranges (list of tuples): A list of (start, end) ranges, 
                                        expected to be non-overlapping and sorted.

    Returns:
        bool: True if the number is in any range, False otherwise.
    """
    
    # Iterate through the (start, end) tuple for each merged range
    for start, end in freshness_ranges:
        
        if ingredient_id < start:
            return False

        if start <= ingredient_id <= end:
            return True              
    # If the loop completes without finding a match
    return False

def calculate_cumulative_range_lengths(merged_ranges):
    """requires the merged ranges from part1. simply calculates inclusive length and returns cumulative result"""
    total_length = 0
    
    for start, end in merged_ranges:
        # Length of an inclusive range (start, end) is end - start + 1
        length = end - start + 1
        total_length += length
        
    return total_length

def part1(input_data: str | None) -> int:
    if input_data is None:
        input_data = TEST_DATA

    fresh_ingredients = []
    fresh_ranges, ingredient_ids = parse(input_data)
    fresh_ranges = merge_overlapping_ranges(fresh_ranges)
    for ingredient in ingredient_ids:
        if is_ingredient_fresh(ingredient, fresh_ranges):
            fresh_ingredients.append(ingredient)
    return len(fresh_ingredients)

        



def part2(input_data: str | None) -> int:
    if input_data is None:
        input_data = TEST_DATA
    fresh_ranges, _ = parse(input_data)
    fresh_ranges = merge_overlapping_ranges(fresh_ranges)
    return calculate_cumulative_range_lengths(fresh_ranges)


if __name__ == "__main__":
    aoc_runner(part1, part2)