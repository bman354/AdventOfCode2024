import sys

left_ids = []
right_ids = []

with open('input.txt', 'r') as file:
    raw = file.readlines()

lines = [s.strip() for s in raw]

for line in lines:
    splitline = line.split()
    left_ids.append(int(splitline[0]))
    right_ids.append(int(splitline[1]))

total_distance = 0

left_ids.sort()
right_ids.sort()

def calculateDistance():
    dist = 0
    i = 0
    while(i < len(left_ids)):
        dist += abs(left_ids[i] - right_ids[i])
        i+=1
    return dist

def calculateScore():
    score = 0
    runningsum = 0

    for lid in left_ids:
        for rid in right_ids:
            if lid == rid:
                runningsum += 1
        if runningsum > 0:
            score += (lid * runningsum)
            runningsum = 0
    return score



total_distance = calculateDistance()
print("total distance: ", total_distance)
similarity_score = calculateScore()
print("Similarity Score: ", similarity_score)