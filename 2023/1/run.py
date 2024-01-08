def p1(lines):
    sum = 0
    
    for line in lines:
        if len(line) > 0:
            first = -1
            last = -1
            
            for c in line:
                if c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    if first < 0: first = int(c)
                    last = int(c)
            first = 0 if first < 0 else first
            last = 0 if last < 0 else last
            sum += first * 10 + last
    
    print(sum)

def find_digits(s):
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alpha_digits = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    
    digits_by_len = {}
    for d in alpha_digits.keys():
        if len(d) in digits_by_len:
            digits_by_len[len(d)].append(d)
        else: digits_by_len[len(d)] = [d]
    
    nums = []
    for i in range(len(s)):
        if s[i] in digits:
            nums.append(int(s[i]))
        else:
            for l in digits_by_len.keys():
                if s[i:(i+l)] in digits_by_len[l]:
                    nums.append(alpha_digits[s[i:(i+l)]])
    return nums
    
def p2(lines):
    sum = 0
    for line in lines:
        if len(line) > 0:
            nums = find_digits(line)
            first = 0 if len(nums) == 0 else nums[0]
            last = 0 if len(nums) == 0 else nums[-1]
            sum += first * 10 + last
    print(sum)
    
with open("input.txt", "r") as f:
    lines = f.readlines()
    p2(lines)
