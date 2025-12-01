with open("input.txt", "r+", encoding="utf-8") as f:
    input_file = f.readlines()

processed = [direction.strip("\n") for direction in input_file]
position= 50
test_data= ["L68", "L30", "R48","L5","R60","L55","L1","L99","R14","L82"]



def establish_new_position(start_pos: int, direction: str, zero_counter: int=0):
    """
    Inputs: takes a starting position, a stringbased direction for turning a dial, and an optional counter
    Returns: the adjusted position, having applied the direction, and optionally updated counter.
    """
    if direction[0] == "L":
        negative_increment = int(direction[1:])
        new_pos = (start_pos - negative_increment) % 100
    elif direction[0] =="R":
        positive_increment = int(direction[1:])
        new_pos = (start_pos + positive_increment) % 100
    else:
        print("Can't go that way!!")
    if new_pos == 0:
        print("BACK AT ZERO!")
        zero_counter+=1

    return new_pos, zero_counter


zero_counter = 0
for turn in processed:
    position, zero_counter = establish_new_position(position, turn, zero_counter)
print(zero_counter)
    
