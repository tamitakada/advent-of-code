def part_one():
    with open("data.txt", "r") as file:
        data = file.read()
        i = 0
        while i < len(data):
            if not contains_duplicates(data[i:(i + 4)]):
                print(f"PART ONE: {i + 4}")
                break
            i += 1

def part_two():
    with open("data.txt", "r") as file:
        data = file.read()
        i = 0
        while i < len(data):
            if not contains_duplicates(data[i:(i + 14)]):
                print(f"PART TWO: {i + 14}")
                break
            i += 1

def contains_duplicates(str):
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if str[j] == str[i]: return True
    return False
