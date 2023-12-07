inputData = '2023/data/input07.txt'

def getTypeRankOne(hand, labels):
    cnt = []
    for l in labels:
        rank = hand.count(l)
        if rank > 0:
            cnt.append(rank)

    match max(cnt):
        case 5:
            return 6
        case 4:
            return 5
        case 3:
            if min(cnt) == 2: return 4
            return 3
        case 2:
            if cnt.count(2) == 2: return 2
            return 1
        case 1:
            return 0
        
def getTypeRankTwo(hand, labels):
    cnt = [0]
    for l in labels[1:]:
        rank = hand.count(l)
        if rank > 0:
            cnt.append(rank)
    cnt.sort()
    cnt[-1] += hand.count("J")
    if(cnt[0] == 0): cnt = cnt[1:]
    match max(cnt):
        case 5:
            return 6
        case 4:
            return 5
        case 3:
            if min(cnt) == 2: return 4
            return 3
        case 2:
            if cnt.count(2) == 2: return 2
            return 1
        case 1:
            return 0

def getRankValue(hand, labels, getTypeRank):
    priority = len(hand)
    lableCnt = len(labels)
    rank = getTypeRank(hand, labels) * (lableCnt ** priority)
    for c in hand:
        priority -= 1
        rank += labels.index(c) * (lableCnt ** priority)
    return rank

def partition(array, low, high):
    pivot = array[high][0]
    i = low - 1
    for j in range(low, high):
        if array[j][0] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def getSum(content):
    sum, rank = 0, 0
    for _, _, bid in content:
        rank += 1
        sum += rank * bid
    return sum

labelsOne = list("AKQJT98765432")[::-1]
with open(inputData) as f:
    content = [(getRankValue(y, labelsOne, getTypeRankOne), y, int(z)) for y, z in [x.split(" ") for x in f.readlines()]]
quickSort(content, 0, len(content)-1)

print("Part one", getSum(content))


labelsTwo = list("AKQT98765432J")[::-1]
with open(inputData) as f:
    content = [(getRankValue(y, labelsTwo, getTypeRankTwo), y, int(z)) for y, z in [x.split(" ") for x in f.readlines()]]
quickSort(content, 0, len(content)-1)
print("Part two", getSum(content))