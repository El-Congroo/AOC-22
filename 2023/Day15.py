with open('2023/data/input15.txt') as f:
    content = [line.strip() for line in f.readlines()][0]

def get_hash(s):
    hash = 0
    for c in s:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash


print(sum([get_hash(s) for s in content.split(",")]))

