def part_one():
    with open("data.txt", "r") as file:
        fully_contained_pairs = 0
        for line in file.read().split("\n"):
            if len(line) > 0:
                assignments = line.split(",")
                first_elf = assignments[0].split("-")
                second_elf = assignments[1].split("-")
                if full_range_overlap(
                    int(first_elf[0]),
                    int(first_elf[1]),
                    int(second_elf[0]),
                    int(second_elf[1])
                ): fully_contained_pairs += 1
        
        print(f"PART ONE: {fully_contained_pairs}")
        
def part_two():
    with open("data.txt", "r") as file:
        contained_pairs = 0
        for line in file.read().split("\n"):
            if len(line) > 0:
                assignments = line.split(",")
                first_elf = assignments[0].split("-")
                second_elf = assignments[1].split("-")
                if range_overlap(
                    int(first_elf[0]),
                    int(first_elf[1]),
                    int(second_elf[0]),
                    int(second_elf[1])
                ): contained_pairs += 1
        
        print(f"PART TWO: {contained_pairs}")

def full_range_overlap(min1, max1, min2, max2):
    if max2 > max1: return min2 <= min1
    elif max2 == max1: return True
    else: return min1 <= min2
    
def range_overlap(min1, max1, min2, max2):
    return not (max1 < min2 or max2 < min1)
