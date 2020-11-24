
import numpy as np
import math

rng = np.random.default_rng()

def roll(maxDie, count, explode=-1):
    result = rng.integers(1,1+maxDie,size=count)
    mask = (result == maxDie)
    explodeCount = 0
    while mask.any() and (explodeCount < explode or explode==-1):
        explodeCount += 1
        newRoll = mask * rng.integers(1,1+maxDie,size=count)
        result += newRoll
        mask = (newRoll == maxDie)
    return result

        
def wildDieRoll(maxDie, count, explode=-1):
    aaa = roll(maxDie, count, explode)
    bbb = roll(6, count, explode)
    result = np.max(np.vstack([aaa,bbb]),axis=0)
    return result


def printHeader(maxRoll):
    print("|    | " + " | ".join([">={:2d}".format(ccc) for ccc in range(1,maxRoll+1)]) + " |")
    print("|----"+("|------"*maxRoll)+"|")


def printStats(maxDie, count, maxRoll=999, explode=-1):
    rolls,pdf = np.unique(roll(maxDie,count,explode),return_counts=True)
    maxRoll = min(np.max(rolls),maxRoll)
    pdf = pdf / count
    allResults = {}
    for ii in range(rolls.size):
        allResults[rolls[ii]] = pdf[ii]
    for ii in range(1,np.max(rolls)):
        if ii not in allResults:
            allResults[ii] = 0
    rolls = sorted(allResults.keys())
    values = np.zeros((len(allResults),));
    for ii,r in enumerate(rolls):
        values[ii] = allResults[r]
    pdf = np.array(values)
    cdf = np.flip(np.cumsum(np.flip(pdf)))
    print("|d{:<2d} | ".format(maxDie)
          +" | ".join(["{:3d}%".format(int(ccc)) for ccc in (cdf[:maxRoll]*100).round()])+" |")

maxRoll=18
    
#printStats(4, 10000000, maxRoll, 1)
#printStats(6, 10, maxRoll, 1)
#printStats(8, 10000000, maxRoll, 1)
#printStats(10, 10000000, maxRoll, 1)
#printStats(12, 10000000, maxRoll, 1)


printHeader(maxRoll)
printStats(4, 10000000, maxRoll, -1)
printStats(6, 10000000, maxRoll, -1)
printStats(8, 10000000, maxRoll, -1)
printStats(10, 10000000, maxRoll, -1)
printStats(12, 10000000, maxRoll, -1)

#import matplotlib.pyplot as plt
#
#count=1000000
#explode=-1
#for maxDie in [4,6,8,10,12]:
#    rolls,pdf = np.unique(roll(maxDie,count,explode),return_counts=True)
#    #rolls,pdf = np.unique(wildDieRoll(maxDie,count,explode),return_counts=True)
#    pdf = pdf / count
#    cdf = np.flip(np.cumsum(np.flip(pdf)))
#    plt.plot(cdf[:17],rolls[:17],'-o')
#plt.plot([0.25, 0.25],[0, 20],'--')
#plt.plot([0.5, 0.5],[0, 20],'--')
#plt.plot([0.75, 0.75],[0, 20],'--')
#plt.show()
