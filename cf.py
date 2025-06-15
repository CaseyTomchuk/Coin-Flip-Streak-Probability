import random
streakCounter = 0
coinList = []
for experiment in range (10000): 
    for coinFlip in range (100):
        if random.randint(0,1) == 0:
            coinList.append("Heads")
        else:
            coinList.append("Tails")
#print(coinList)
    

# 100 CF will be run 10,000 times
# how often will a streak of six heads or six tails come up