game_map = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3
}

def part_one():
    with open("data.txt", "r") as file:
        score = 0
        for line in file.read().split("\n"):
            if len(line) > 0:
                plays = line.split(" ")
                score += get_play_value(plays[1]) + \
                    get_play_result(plays[0] + plays[1])
                    
        print(f"PART 1: {score}")
        
def part_two():
    with open("data.txt", "r") as file:
        score = 0
        for line in file.read().split("\n"):
            if len(line) > 0:
                plays = line.split(" ")
                result = get_result_value(plays[1])
                score += result + \
                    get_play_value(get_play_for_result(plays[0], result))
                    
        print(f"PART 2: {score}")

def get_play_value(play):
    value_map = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    return value_map[play]

def get_play_result(plays):
    return game_map[plays]
    
def get_result_value(play):
    value_map = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    return value_map[play]
    
def get_play_for_result(opponent, result):
    for key in game_map.keys():
        if key[0] == opponent:
            if game_map[key] == result:
                return key[1]

part_two()
