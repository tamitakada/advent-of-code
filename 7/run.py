def create_file_tree(lines):
    current_dir = ""
    file_sizes = {}
    for i in range(len(lines)):
        if len(lines[i]) > 0:
            if lines[i][0] == "$":
                components = lines[i].split(" ")
                command = components[1]
                if command == "cd":
                    dir = components[2]
                    if dir == "..":
                        last_dir = current_dir.rindex("/")
                        current_dir = current_dir[:last_dir]
                    elif current_dir == "":
                        current_dir = dir
                        file_sizes[current_dir] = 0
                    else:
                        current_dir += f"/{dir}"
                        file_sizes[current_dir] = 0
            else:
                file_info = lines[i].split(" ")
                if file_info[0] != "dir":
                    file_sizes[current_dir] += int(file_info[0])
                    path = current_dir
                    while len(path) > 1:
                        last_dir = path.rindex("/")
                        path = path[:last_dir]
                        file_sizes[path] += int(file_info[0])
    return file_sizes

def part_one():
    with open("test_data.txt", "r") as file:
        lines = file.read().split("\n")
        file_sizes = create_file_tree(lines)

        sum = 0
        for dir in file_sizes.keys():
            if file_sizes[dir] <= 100000: sum += file_sizes[dir]
        
        print(f"PART ONE: {sum}")

def part_two():
    with open("data.txt", "r") as file:
        lines = file.read().split("\n")
        file_sizes = create_file_tree(lines)
        min_size = 30000000 - (70000000 - file_sizes["/"])
        smallest_dir = 70000000
        for dir in file_sizes.keys():
            if file_sizes[dir] >= min_size and \
                file_sizes[dir] < smallest_dir:
                smallest_dir = file_sizes[dir]
        print(f"PART TWO: {smallest_dir}")
