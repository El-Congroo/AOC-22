import re

with open('2023/data/input15.txt') as f:
    content = [line.strip() for line in f.readlines()][0].split(",")

def get_hash(s):
    hash = 0
    for c in s:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash


print("Part 1", sum([get_hash(s) for s in content]))


hashmap = {}

for c in content: 
    el = [label, focus] = re.split("=|-", c)
    hash = get_hash(label)

    if hash not in hashmap:
        if len(focus) > 0:
            hashmap[hash] = [el]
        else: continue

    bucket = hashmap[hash]
    bucket_labels_only = tuple(e for e,_ in bucket)
    
    if label in bucket_labels_only:
        idx = bucket_labels_only.index(label)
        if len(focus) > 0: 
            bucket[idx][1] = focus
        else: 
            del bucket[idx]

    elif len(focus) > 0:
        bucket.append(el)

print("Part 2", sum([sum([(hash+1) * (slot+1) * int(focal) for slot, [_, focal] in enumerate(elements)]) for hash, elements in hashmap.items()]))
