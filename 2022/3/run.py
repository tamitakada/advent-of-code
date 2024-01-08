def part_one():
    with open("data.txt", "r") as file:
        sum = 0
        for line in file.read().split("\n"):
            item_priority = 0
            for i in range(int(len(line) / 2)):
                for j in range(int(len(line) / 2)):
                    if line[i] == line[-(j + 1)]:
                        item_priority = get_priority(line[i])
                        break
                if item_priority > 0:
                    sum += item_priority
                    break
        print(f"PART ONE: {sum}")
        
def part_two():
    with open("data.txt", "r") as file:
        sum = 0
        current_group = 0
        
        lines = file.read().split("\n")
        while current_group < (len(lines) - 3):
            for item in lines[current_group]:
                if lines[current_group + 1].__contains__(item):
                    if lines[current_group + 2].__contains__(item):
                        sum += get_priority(item)
                        break
            current_group += 3

        print(f"PART TWO: {sum}")

def get_priority(char):
    ascii = ord(char)
    if ascii < 97: return (ascii - 65) + 27
    else: return (ascii - 96)

part_two()
