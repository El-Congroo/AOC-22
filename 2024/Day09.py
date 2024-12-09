with open('2024/data/input09.txt') as f:
    content = [int(y) for x in f for y in x.strip()]

################
### part one ###
################

free = finished = False
fill_in = content[::-2]
all_cnt = sum(content)
free_cnt = sum(content[1::2])
cur_back_id = (len(content) - 1) // 2 + 1
i = sum1 = cur_front_id = cur_back_cnt = 0

for x in content:
    for j in range(x):
        if free:
            if cur_back_cnt == 0:
                cur_back_cnt = fill_in.pop(0)
                cur_back_id -= 1
            cur_back_cnt -= 1
            sum1 += cur_back_id * i
        else: 
            sum1 += cur_front_id * i
        i += 1
        if i == (all_cnt - free_cnt): finished = True; break
    if finished: break
    if not (free := not free): 
        cur_front_id += 1

print("Part 1:", sum1)

################
### part two ###
################

enumerated_blocks = [(i//2, x) if i % 2 == 0 else (None, x) for i, x in enumerate(content) if x > 0]
blocks_reverse_not_empty_only = [x for x in enumerated_blocks[::-1] if x[0] != None]       # bc of x > 0

for b in blocks_reverse_not_empty_only:                 # go through all possibly movable blocks
    for i in range(len(enumerated_blocks)):             # go over blocks
        if enumerated_blocks[i] == b: break             # stop if there is no free space before cur element
        
        if None == enumerated_blocks[i][0] and (free_space := enumerated_blocks[i][1]) >= b[1]:
            j = enumerated_blocks.index(b)              # get index of current block
            del enumerated_blocks[j]                    # delete block being moved
            enumerated_blocks.insert(j, (None, b[1]))   # "replace" with empty block
            
            del enumerated_blocks[i]                    # delete old empty block
            if (free_space := free_space - b[1]) > 0:   # insert new empty block
                enumerated_blocks.insert(i, (None, free_space))
            enumerated_blocks.insert(i, b)              # "move" full block
            break


print("Part 2:", sum((x if x != None else 0) * sum(range(i, i := i + j)) for x, j in enumerated_blocks))
