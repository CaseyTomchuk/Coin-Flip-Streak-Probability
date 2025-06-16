import random
streakCounter = 0

for experiment in range (10000):
    streakChecker = 0 # streak checker and coin list is reset at the start of each loop
    coinList = [] 

    for coinFlip in range (100):
        if random.randint(0,1) == 0:
            coinList.append("Heads")
        else:
            coinList.append("Tails")

# If the current flip = previous flip, start accumulating streak checker. If not, reset checker.
        if len(coinList) > 1 and coinList[-1] == coinList[-2]:
            streakChecker += 1
            if streakChecker == 5:
                streakCounter += 1
                break
        else:
            streakChecker = 0

print(streakCounter)
print(f'Chance of streak: %s%%' % (streakCounter / 100))