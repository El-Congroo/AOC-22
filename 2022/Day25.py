#################
### read file ###
#################

def readData():
    with open('2022/data/input25.txt') as f:
        content = [a.strip() for a in f.readlines()]
    return content


##############
### part 1 ###
##############

def snafu2NbrsL(snafu):
    return [int(b.replace("-", "-1").replace("=", "-2")) for b in snafu]

def nbrsL2Dec(snafu):
    ret = 0
    for i in range(len(snafu)):
        ret += snafu[-i-1]*5**i
    return ret

def getSum():
    return sum(map(nbrsL2Dec, map(snafu2NbrsL, readData())))

def dec2snafu(dec):
    ret = ""
    while dec > 0:
        i = dec % 5
        if i >= 3:
            i -= 5
        ret = str(i).replace("-2", "=").replace("-1", "-") + ret 
        dec -= i
        dec //= 5
    return ret





print(dec2snafu(getSum()))