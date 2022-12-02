input = open("input.txt", "r").readlines()

win = 6
loss = 0
draw = 3

points = { "rock": 1, "paper": 2, "scissors": 3 }

def translate(hand):
    if hand == "A" or hand == "X":
        return "rock"
    elif hand == "B" or hand == "Y":
        return "paper"
    elif hand == "C" or hand == "Z":
        return "scissors"
    
def score_b(outcome, move):
    if outcome == "Y":
        return (draw + points[move]) 
    elif outcome == "X":
        if move == "rock":
            return points["scissors"]
        elif move == "paper":
            return points["rock"]
        elif move == "scissors":
            return points["paper"]
    elif outcome == "Z":
        if move == "rock":
            return (6 + points["paper"])
        elif move == "paper":
            return (6 + points["scissors"])
        elif move == "scissors":
            return (6 + points["rock"])
    
def outcome(action, reaction):
    if action == reaction:
        return draw
    else:
        if action == "rock":
            if reaction == "paper":
                return win
            elif reaction == "scissors":
                return loss
        elif action == "paper":
            if reaction == "rock":
                return loss
            elif reaction == "scissors":
                return win
        elif action == "scissors":
            if reaction == "rock":
                return win
            elif reaction == "paper":
                return loss

def get_score_a():
    score = 0
    for line in input:
        action = translate(line[0])
        reaction = translate(line[2])
        score += (outcome(action, reaction) + points[reaction])
        
    return score

def get_score_b():
    score = 0
    for line in input:
        action = translate(line[0])
        score += score_b(line[2], action)
    return score
        
print(get_score_b())