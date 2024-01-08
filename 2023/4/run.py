def p1(lines):
    points = 0
    for line in lines:
        if len(line) > 0:
            winning_nums = 0
        
            line = line.strip("\n")
            sides = line.split(": ")[1].split(" | ")
            
            winners = sides[0].split(" ")
            guesses = sides[1].split(" ")
            
            for guess in guesses:
                if len(guess) > 0 and guess in winners:
                    winning_nums += 1
            
            if winning_nums > 0:
                points += 2**(winning_nums - 1)
        
    print(points)
    

def total_cards(card, data):
    if len(data[card]) == 0: return 0
    else:
        sum = 0
        for winner in data[card]:
            sum += total_cards(winner, data)
        return sum + len(data[card])
    
def p2(lines):
    total = 0
    num_cards = {} # {card_index: [winning_card_indices]}
    for i in range(len(lines)):
        if len(lines[i]) > 0:
            num_cards[i] = []
            
            winning_nums = 0
        
            lines[i] = lines[i].strip("\n")
            sides = lines[i].split(": ")[1].split(" | ")
            
            winners = sides[0].split(" ")
            guesses = sides[1].split(" ")
            
            for guess in guesses:
                if len(guess) > 0 and guess in winners:
                    winning_nums += 1
            
            for j in range(1, winning_nums + 1):
                num_cards[i].append(i + j)
    
    for card in num_cards.keys():
        total += 1
        total += total_cards(card, num_cards)
        
    print(total)

with open("input.txt", "r") as f:
    lines = f.readlines()
    p2(lines)
