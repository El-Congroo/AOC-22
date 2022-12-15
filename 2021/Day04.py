###################
###  read data  ###
###################

def getContent():
    with open('data/2021/input04.txt') as f:
        content = [x for x in f.readlines()]
        numbers = [int(x.strip()) for x in content[0].strip().split(",")]
        dimension = 5
        boards = [[[int(x) for x in line.strip().split(" ") if x != ''] for line in content[i:i+dimension]] for i in range(2, len(content), dimension+1)]
        return numbers, boards


####################
###    part 1    ###
####################

def draw(board, n):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == n:
                board[y][x] += 1j
                return

def getUnmarkedSum(board):
    return sum([sum([int(element.real) for element in line if element.imag == 0 ]) for line in board])


def getWinningSum(board):
    for _ in range(2):
        for line in board:
            if sum(line).imag == 5:
                return getUnmarkedSum(board)
        board = list(zip(*board[::-1]))


def part1():
    numbers, boards = getContent()

    for n in numbers:
        for board in boards:
            draw(board, n)
            winningSum = getWinningSum(board)
            if winningSum is not None:
                return int(n * winningSum)


####################
###    part 2    ###
####################

def part2():
    numbers, boards = getContent()
    for n in numbers:
        for board in boards:
            draw(board, n)
        for board in boards:
            winningSum = getWinningSum(board)
            if winningSum is not None:
                boards.remove(board)
                if len(boards) == 0:
                    return int(n * winningSum)
        

####################
### print answer ###
####################

print("part1:", part1())
print("part2:", part2())