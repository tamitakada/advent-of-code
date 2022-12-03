def part_one():
    with open("data.txt", "r") as f:
        elf_snacks = [0]
        current_elf = 0
        max_elf_calories = 0
        
        for line in f.read().split("\n")[:-1]:
            if line == "":
                if elf_snacks[current_elf] > max_elf_calories:
                    max_elf_calories = elf_snacks[current_elf]
            
                elf_snacks.append(0)
                current_elf += 1
            else:
                calories = int(line)
                elf_snacks[current_elf] += calories
        
        print(f"PART 1: {max_elf_calories}")
        
def part_two():
    with open("data.txt", "r") as f:
        elf_snacks = []
        current_elf_calories = 0
        top_three_elves = [0, 0, 0]
        
        for line in f.read().split("\n")[:-1]:
            if line == "":
                for i in range(len(top_three_elves)):
                    if current_elf_calories > top_three_elves[i]:
                        top_three_elves.insert(i, current_elf_calories)
                        top_three_elves.pop(-1)
                        break
                
                elf_snacks.append(current_elf_calories)
                current_elf_calories = 0
            else:
                calories = int(line)
                current_elf_calories += calories
                
        sum = 0
        for elf in top_three_elves: sum += elf
        
        print(f"PART 2: {sum}")
