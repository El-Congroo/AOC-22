#include "../input.h"
#define BOARDSIZE 5

// -------------------------------------- //
// HOW TO BE UNREPLACABLE IN YOUR COMPANY //
// -------------------------------------- //

int check4CrashLanding(int ***planes, int fleetCnt);
int findNearestIsland(int ***plane);
int ***boarding(char **boardingPass, int const waitingPassengers);
void strike(int **boardPass, int passengerNbr);
int check4NoCrashLanding(int ***planes, int fleetCnt, int *leftBoards);

    int main(int argc, char **argv)
{
    // ---------- //
    // read input //
    // ---------- //
    int len;
    char **input = readInput("data/input04.txt", &len);

    // -------- //
    // part one //
    // -------- //
    int result = 0, drawCnt;
    char *iter = input[0];

    // count , in first line
    for (drawCnt = 1; iter[drawCnt]; iter[drawCnt] == ',' ? drawCnt++ : *iter++)
        ;

    // save draw Nbrs in int array
    int *drawOrder = calloc(sizeof(size_t), drawCnt);

    drawOrder[0] = atoi(strtok(input[0], ","));
    for (int i = 1; i < drawCnt; i++)
        drawOrder[i] = atoi(strtok(NULL, ","));

    // calculate number of boards
    const int boardCnt = (len - 2) / (BOARDSIZE + 1);

    // malloc boards as fast as my bus 298 (O(n^3))
    int ***boards = boarding(input, boardCnt);

    // strike all passengers
    int sum, curDraw = 0;
    do
    {
        for (int i = 0; i < boardCnt; i++)
            strike(boards[i], drawOrder[curDraw]);
        curDraw++;
    } while (!(sum = check4CrashLanding(boards, boardCnt)));
    result = drawOrder[curDraw - 1] * sum;

    printf("Part 1: %d\n", result);

    // ------------------- //
    // part two - segfault//
    // ------------------- //
    int leftBoards = boardCnt-1;
    while (leftBoards)
    {
        for (int i = 0; i < boardCnt; i++)
            if(!boards[i])
                strike(boards[i], drawOrder[curDraw]);
        curDraw++;
        sum = check4NoCrashLanding(boards, boardCnt, &leftBoards);
    } 

    result = sum * drawOrder[curDraw - 1];

    printf("Part 2: %d\n", result);
}

int check4CrashLanding(int ***planes, int fleetCnt)
{
    for (int plane = 0; plane < fleetCnt; plane -= -1)
    {

        // is there a line full of shit
        for (int i = 0; i < BOARDSIZE; i++)
        {
            int tmp = 0;
            for (int j = 0; j < BOARDSIZE; j++)
            {
                tmp += planes[plane][i][j];
            }
            if (tmp == -5)
                return findNearestIsland(&planes[plane]);
        }
        for (int i = 0; i < BOARDSIZE; i++)
        {
            int tmp = 0;
            for (int j = 0; j < BOARDSIZE; j++)
            {
                tmp += planes[plane][j][i];
            }
            if (tmp == -5)
                return findNearestIsland(&planes[plane]);
        }
        int tmp = 0, tmp2 = 0;
        for (int i = 0; i < BOARDSIZE; i++)
        {
            tmp += planes[plane][i][i];
            tmp2 += planes[plane][i][BOARDSIZE - i - 1];
        }
        if (tmp == -5 || tmp2 == -5)
            return findNearestIsland(&planes[plane]);
    }
    return 0;
}

int check4NoCrashLanding(int ***planes, int fleetCnt, int *leftBoards)
{
    for (int plane = 0; plane < fleetCnt; plane++)
    {
        if (!planes[plane])
            continue;
        // check for horizontal or vertical bingos
        int tmpX, tmpY;
        for (int i = 0; i < BOARDSIZE; i++)
        {
            tmpX = 0, tmpY = 0;

            for (int j = 0; j < BOARDSIZE; j++)
            {
                tmpX += planes[plane][i][j];
                tmpY += planes[plane][j][i];
            }

            if (tmpX == -5 || tmpY == -5) {
                (*leftBoards)--;
                return findNearestIsland(&planes[plane]);
            }
        }

        // check for diagonal bingos
        tmpX = 0, tmpY=0;
        for (int i = 0; i < BOARDSIZE; i++)
        {
            tmpX += planes[plane][i][i];
            tmpY += planes[plane][i][BOARDSIZE - i - 1];
        }
        if (tmpX == -5 || tmpY == -5) {
            (*leftBoards)--;
            return findNearestIsland(&planes[plane]);
        }
    }
    return 0;
}

int findNearestIsland(int ***plane)
{
    int sum = 0;
    for (int i = 0; i < BOARDSIZE; i++)
        for (int j = 0; j < BOARDSIZE; j++)
            sum += *plane[i][j] != -1 ? *plane[i][j] : 0;
    *plane = NULL;
    return sum;
}

void strike(int **boardPass, int passengerNbr)
{
    for (int i = 0; i < BOARDSIZE; i++)
        for (int j = 0; j < BOARDSIZE; j++)
            if (boardPass[i][j] == passengerNbr)
                boardPass[i][j] = -1;
}

int ***boarding(char **boardingPass, int const waitingPassengers)
{
    int ***boards = calloc(sizeof(int **), waitingPassengers);
    for (int curBoard = 0; curBoard < waitingPassengers; curBoard++)
    {
        int **board = calloc(sizeof(int *), BOARDSIZE);
        for (int boardLine = 0; boardLine < BOARDSIZE; boardLine++)
        {
            int *line = calloc(sizeof(int), BOARDSIZE);
            line[0] = atoi(strtok(boardingPass[2 + curBoard * (BOARDSIZE + 1) + boardLine], " "));
            for (int boardElem = 1; boardElem < BOARDSIZE; boardElem++)
                line[boardElem] = atoi(strtok(NULL, " "));
            board[boardLine] = line;
        }
        boards[curBoard] = board;
    }
    return boards;
}