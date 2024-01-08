digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def is_symbol(c):
    return c not in digits and c != "."

def p1(lines):
    sum = 0
    
    num = ""
    part = False
    
    for row in range(len(lines)):
        lines[row] = lines[row].strip("\n")
        for col in range(len(lines[row])):
            if lines[row][col] in digits:
                num += lines[row][col]
                if row != 0: # Top side
                    if is_symbol(lines[row - 1][col]):
                        part = True
                if row != len(lines) - 1: # Bottom side
                    if is_symbol(lines[row + 1][col]):
                        part = True
                if len(num) == 1 and col != 0: # Only need to check for num start
                    if is_symbol(lines[row][col - 1]): # Left side
                        part = True
                    if row != 0 and is_symbol(lines[row - 1][col - 1]): # TL diag
                        part = True
                    if row != len(lines) - 1 and is_symbol(lines[row + 1][col - 1]): # BL diag
                        part = True
                if col != len(lines[row]) - 1:
                    if lines[row][col + 1] not in digits: # Only check end of num
                        if is_symbol(lines[row][col + 1]): # Right side
                            part = True
                        if row != 0 and is_symbol(lines[row - 1][col + 1]): # TR diag
                            part = True
                        if row != len(lines) - 1 and is_symbol(lines[row + 1][col + 1]): # BR diag
                            part = True
                        if part: # Add if part num, reset vars (next is non-num slot)
                            sum += int(num)
                        num = ""
                        part = False
                
                else:
                    if part: # Add if part num, reset vars (reached right side)
                        sum += int(num)
                    num = ""
                    part = False
    
    print(sum)
    
def p2(lines):
    gear_ratios = {}
    
    num = ""
    attached_gears = []
    
    for row in range(len(lines)):
        lines[row] = lines[row].strip("\n")
        for col in range(len(lines[row])):
            if lines[row][col] in digits:
                num += lines[row][col]
                if row != 0: # Top side
                    if lines[row - 1][col] == "*":
                        attached_gears.append((row - 1, col))
                if row != len(lines) - 1: # Bottom side
                    if lines[row + 1][col] == "*":
                        attached_gears.append((row + 1, col))
                if len(num) == 1 and col != 0: # Only need to check for num start
                    if lines[row][col - 1] == "*": # Left side
                        attached_gears.append((row, col - 1))
                    if row != 0 and lines[row - 1][col - 1] == "*": # TL diag
                        attached_gears.append((row - 1, col - 1))
                    if row != len(lines) - 1 and lines[row + 1][col - 1] == "*": # BL diag
                        attached_gears.append((row + 1, col - 1))
                if col != len(lines[row]) - 1:
                    if lines[row][col + 1] not in digits: # Only check end of num
                        if lines[row][col + 1] == "*": # Right side
                            attached_gears.append((row, col + 1))
                        if row != 0 and lines[row - 1][col + 1] == "*": # TR diag
                            attached_gears.append((row - 1, col + 1))
                        if row != len(lines) - 1 and lines[row + 1][col + 1] == "*": # BR diag
                            attached_gears.append((row + 1, col + 1))
                            
                        for gear in attached_gears:
                            if gear in gear_ratios:
                                gear_ratios[gear].append(int(num))
                            else:
                                gear_ratios[gear] = [int(num)]
                        num = ""
                        attached_gears = []
                
                else:
                    for gear in attached_gears:
                        if gear in gear_ratios:
                            gear_ratios[gear].append(int(num))
                        else:
                            gear_ratios[gear] = [int(num)]
                    num = ""
                    attached_gears = []
    
    sum = 0
    for gear in gear_ratios.keys():
        if len(gear_ratios[gear]) == 2:
            sum += gear_ratios[gear][0] * gear_ratios[gear][1]
    
    print(sum)

with open("input.txt", "r") as f:
    lines = f.readlines()
    p2(lines)
