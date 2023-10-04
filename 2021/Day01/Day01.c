#include "../input.h"
#include <xlocale.h>
#define WINDOWSZIE 3

int getWindow(char **input, int index) {
    int sum = 0;
    for(int i=index; i<index+WINDOWSZIE; i++)
        sum += atoi(input[i]);
    return sum;
}

int main(int argc, char **argv) {
    // ---------- //
    // read input //
    // ---------- //
    int len, count = 0;
    char **input = readInput("data/input01.txt", &len);

    // -------- //
    // part one //
    // -------- //
    for(int i=1; i<len; i++)
        if (atoi(input[i-1]) < atoi(input[i])) 
            count++;
    printf("Part 1: %d\n", count);

    // -------- //
    // part two //
    // -------- //
    count = 0;
    for(int i=1; i<len-WINDOWSZIE+1; i++)
        if (getWindow(input, i - 1) < getWindow(input, i))
            count++;
    printf("Part 2: %d\n", count);
}
