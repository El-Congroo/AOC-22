#include "../input.h"
int main(int argc, char **argv)
{
    // ---------- //
    // read input //
    // ---------- //
    int len;
    char **input = readInput("data/input02.txt", &len);
    char **input2 = readInput("data/input02.txt", &len); // TODO pfusch weg

    // -------- //
    // part one //
    // -------- //
    int result = 0;
    int depth = 0, horizontal = 0;
    for (int i=0; i < len; i++)
    {
        char *direction = strtok(input[i], " ");
        int val = atoi(strtok(NULL, " "));

        if (!strcmp("forward", direction))
            horizontal += val;
        else if(!strcmp("down", direction))
            depth += val;
        else
            depth -= val;
    }

    result = depth * horizontal;
    printf("Part 1: %d\n", result);

    // -------- //
    // part two //
    // -------- //
    result = 0;
    depth = 0, horizontal = 0;
    int aim = 0;
    for (int i = 0; i < len; i++)
    {

        char *direction = strtok(input2[i], " ");
        int val = atoi(strtok(NULL, " "));

        if (!strcmp("forward", direction)) {
            horizontal += val;
            depth += aim * val;
        }
        else if (!strcmp("down", direction))
            aim += val;
        else
            aim -= val;
    }
    result = depth * horizontal;
    printf("Part 2: %d\n", result);
}
