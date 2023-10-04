#include "../input.h"

int main(int argc, char **argv)
{
    // ---------- //
    // read input //
    // ---------- //
    int len;
    char **input = readInput("data/input03.txt", &len);

    // -------- //
    // part one //
    // -------- //
    int result = 0, g = 0, e = 0;
    int binaryWidth = strlen(input[0]);
    int *oneCnt = calloc(binaryWidth, sizeof(int));

    for(int i=0; i<len; i++)
        for (int j=0; j<binaryWidth; j++)
            oneCnt[j] += input[i][j] - 48;

    int mask = 0;
    for(int i=0; i<binaryWidth; i++) {
        g += ((oneCnt[i] > len/2) ? 1 : 0) << (binaryWidth-i-1);
        mask = (mask << 1) + 1;
    }

    e = ~g & mask;
    result = e * g;
    printf("E: %d, G: %d\n", e, g);

    printf("Part 1: %d\n", result);

    // -------- //
    // part two //
    // -------- //
    result = 0;
    int out = 0;
    for(int i=0; i<binaryWidth; i++) {

        for(int j=0; j<len; j++) {
            if(!input[j]) continue;

            if (input[j][i] - '0' != ((oneCnt[i] >= len / 2) ? 1 : 0)) {
                input[j] = NULL;
                out++;
            }
        }

        if (out != len - 1) break;
    }

    printf("Part 2: %d\n", result);
}
