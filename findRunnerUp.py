arr = [34,67,32,98,68,55]
highest = 0
runnerUp = 0
bReak = False
for item in arr:
    if item > highest:
        highest = item

lowest = highest
for item in arr:
    if item < lowest:
        lowest = item
        
for i in range (highest-1,lowest-1,-1):
    if bReak:
        break
    for item in arr:
        if item == i:
            runnerUp = item
            bReak = True
            break
            
print (runnerUp)
