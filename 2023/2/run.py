def is_game_possible(draws):
    for draw in draws:
        colors = draw.split(", ")
        for color in colors:
            info = color.split(" ")
            info[1] = info[1].strip("\n")
            if info[1] == "red" and int(info[0]) > 12: return False
            elif info[1] == "green" and int(info[0]) > 13: return False
            elif info[1] == "blue" and int(info[0]) > 14: return False
    return True

def p1(lines):
    sum = 0
    for line in lines:
        if len(line) > 7:
            components = line.split(": ")
            id = int(components[0][5:])
            draws = components[1].split("; ")
            if is_game_possible(draws):
                sum += id
                print(id)
    print(sum)
    
def cube_power(draws):
    mins = {"red": 0, "blue": 0, "green": 0}
    for draw in draws:
        colors = draw.split(", ")
        for color in colors:
            info = color.split(" ")
            info[1] = info[1].strip("\n")
            if int(info[0]) > mins[info[1]]:
                mins[info[1]] = int(info[0])
    return mins["red"] * mins["blue"] * mins["green"]

def p2(lines):
    sum = 0
    for line in lines:
        if len(line) > 7:
            components = line.split(": ")
            draws = components[1].split("; ")
            sum += cube_power(draws)
    print(sum)

with open("input.txt", "r") as f:
    lines = f.readlines()
    p2(lines)
