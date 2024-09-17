with open('2023/data/input13.txt') as f:
    content = [line.strip() for line in f.readlines()]
    content.append("")

def getIdxPartOne(block):
    possIdx = list(range(1, len(block[0])))
    for line in block:
        for i in possIdx.copy():
            if not line[:i][::-1].startswith(line[i:i*2]): 
                possIdx.remove(i)
        
    return possIdx[0] if len(possIdx) == 1 else 0

def getIdxPartTwo(block):
    cnt = {idx:0 for idx in range(1, len(block[0]))}
    
    for line in block:
        for i in list(cnt):
            if (dif := sum(c1 != c2 for c1, c2 in zip(line[:i][::-1],line[i:i*2]))) > 1: del cnt[i]
            else: cnt[i] += dif
    
    return next((k for k,v in cnt.items() if v ==1), 0)
            
                
def getResult(content, func):
    b, result = [], 0
    for line in content:
        if line == "":
            result += func(b)
            b = [''.join(a) for a in zip(*b)][::-1]
            result += func(b) * 100
            b = []
        else:
            b.append(line)
    return result


print("Part one:", getResult(content, getIdxPartOne))


print("Part two:", getResult(content, getIdxPartTwo))