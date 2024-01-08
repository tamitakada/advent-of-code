def part_one():
    with open("data.txt", "r") as file:
        sections = file.read().split("\n\n")
        
        crate_lines = sections[0].split("\n")
        crates = get_crates(crate_lines)
                
        instructions = sections[1].split("\n")
        for instruction in instructions:
            if len(instruction) > 0:
                components = instruction.split(" ")
                move_count = int(components[1])
                stack_1 = int(components[3])
                stack_2 = int(components[5])
                for i in range(move_count):
                    crates[stack_2 - 1].insert(
                        0,
                        crates[stack_1 - 1].pop(0)
                    )
        
        top_crates = ""
        for stack in crates:
            top_crates += stack[0]
        
        print(f"PART ONE: {top_crates}")
        
def part_two():
    with open("data.txt", "r") as file:
        sections = file.read().split("\n\n")
        
        crate_lines = sections[0].split("\n")
        crates = get_crates(crate_lines)
        
        instructions = sections[1].split("\n")
        for instruction in instructions:
            if len(instruction) > 0:
                components = instruction.split(" ")
                move_count = int(components[1])
                stack_1 = int(components[3])
                stack_2 = int(components[5])
                i = move_count - 1
                while i >= 0:
                    crates[stack_2 - 1].insert(
                        0,
                        crates[stack_1 - 1].pop(i)
                    )
                    i -= 1
        
        top_crates = ""
        for stack in crates:
            top_crates += stack[0]
        
        print(f"PART TWO: {top_crates}")

def get_crates(crate_lines):
    crates = []
    for i in range(len(crate_lines[:-1])):
        j = 1
        while j < len(crate_lines[i]):
            if i == 0: crates.append([])
            if crate_lines[i][j] != " ":
                crates[int(j / 4)].append(
                    crate_lines[i][j]
                )
            j += 4
    return crates


part_two()
