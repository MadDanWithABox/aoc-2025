from wrapper import aoc_runner

TEST_DATA="11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
def parse(data_string:str):
    data_ranges = data_string.split(",")
    return data_ranges

def process_range(range_str: str):
    """
    A range string like so '11-22'
    """
    numbers = []
    split = range_str.split('-')
    start = int(split[0])
    end = int(split[1])
    numbers.extend(num for num in range(start, end + 1))
    return numbers

def check_num_for_two_repeats(num: int) -> bool:
    s_num = str(num)
    length = len(s_num)
    
    #can't be mirror number if length is odd
    if length % 2 != 0:
        return False
        
    midpoint = length // 2
    # compare for equality
    return s_num[:midpoint] == s_num[midpoint:]


def check_num_for_repeats(num: int) -> bool:
    s_num = str(num)
    length = len(s_num)
    # patern length can be at most half the total length 
    for i in range(1, (length // 2) + 1):
        
        # total len must be divisible by the pattern len
        if length % i == 0:
            pattern = s_num[:i]
            multiplier = length // i
            
            # 2. Check if the pattern repeated 'multiplier' equals the original string
            if pattern * multiplier == s_num:
                return True
                
    return False

def part1(input_data: str| None):
    if input_data == None:
        input_data = TEST_DATA
    mirror_numbers=[]
    parsed = parse(input_data)
    print("running part 1")
    for r in parsed:
        numbers_list = process_range(r)
        for num in numbers_list:
            if check_num_for_two_repeats(num):
                mirror_numbers.append(num)
    return(sum(mirror_numbers))


def part2(input_data:str|None):
    if input_data == None:
        input_data = TEST_DATA
    perfect_repeats = []
    parsed = parse(input_data)
    for r in parsed:
        numbers_list = process_range(r)
        for num in numbers_list:
            if check_num_for_repeats(num):
                perfect_repeats.append(num)
    return(sum(perfect_repeats))


    print("running part 2")

if __name__ == "__main__":
    aoc_runner(part1, part2)