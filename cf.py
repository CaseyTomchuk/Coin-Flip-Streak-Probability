import random
streakCounter = 0
streakChecker = 0
coinList = []

for experiment in range (10000): 
    for coinFlip in range (100):
        if random.randint(0,1) == 0:
            coinList.append("Heads")
        else:
            coinList.append("Tails")

# If the current flip = previous flip, start accumulating streak checker. If not, reset checker.
        if len(coinList) > 1 and coinList[-1] == coinList[-2]:
            streakChecker += 1
            if streakChecker == 5:
                streakChecker = 0
                streakCounter += 1
        else:
            streakChecker = 0

print(streakCounter)

# 100 CF will be run 10,000 times
# How often will a streak of six heads or six tails come up?