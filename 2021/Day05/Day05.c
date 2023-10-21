#include "../input.h"

void printCanvas(int *canvas, int maxX, int maxY);

int main(int argc, char **argv)
{
    // ---------- //
    // read input //
    // ---------- //
    int len;
    char **input = readInput("data/input05.txt", &len);

    // -------- //
    // part one //
    // -------- //
    int **coords = calloc(sizeof(int *), len);
    if (!coords)
        die("calloc");

    int dim[2] = {0, 0};

    for (int i = 0; i < len; i++)
    {
        coords[i] = calloc(sizeof(int), 4);
        if (!coords[i])
            die("calloc");

        // put data in array
        coords[i][0] = atoi(strtok(input[i], ", ->"));
        for (int j = 1; j < 4; j++)
            coords[i][j] = atoi(strtok(NULL, ", ->"));

        // switch coordinates if higher value is right
        for (int j = 0; j < 2; j++)
            if (coords[i][j] > coords[i][j + 2])
                for(int k=0; k<2; k++) {
                    int tmp = coords[i][k];
                    coords[i][k] = coords[i][k + 2];
                    coords[i][k + 2] = tmp;
                }

        // save the maximum x and y coordinates
        for (int j = 0; j < 2; j++)
            dim[j] = coords[i][j + 2] > dim[j] ? coords[i][j + 2] : dim[j];
    }

    // add one because of zero coordinates
    for (int j = 0; j < 2; j++)
        dim[j] += 1;

    int *canvas = calloc(sizeof(int), dim[0] * dim[1]);
    if (!canvas)
        die("calloc");

    for (int i = 0; i < len; i++)
    {
        if ((coords[i][0] - coords[i][2]) * (coords[i][1] - coords[i][3]))
            continue;

        for (int x = coords[i][0]; x <= coords[i][2]; x++)
            for (int y = coords[i][1]; y <= coords[i][3]; y++)
                canvas[x + y * dim[0]] += 1;
    }
    int result = 0;

    // count points where at least two lines overlap
    for (int i = 0; i < dim[0]*dim[1]; i++)
        if(canvas[i] > 1)
            result++;

    printCanvas(canvas, dim[0], dim[1]);
    printf("Part 1: %d\n", result);

    // -------- //
    // part two //
    // -------- //

    for (int i = 0; i < len; i++)
    {
        // skip non diagonal lines
        if (!((coords[i][0] - coords[i][2]) * (coords[i][1] - coords[i][3])))
            continue;

        int x = coords[i][0];
        for (int y = coords[i][1]; y <= coords[i][3]; y++) {
                canvas[x + y * dim[0]] += 1;
                x += coords[i][0] < coords[i][2] ? 1 : -1;
        }
    }


    // count points where at least two lines overlap
    result = 0;
    for (int i = 0; i < dim[0] * dim[1]; i++)
        if (canvas[i] > 1)
            result++;

        

    printf("Part 2: %d\n", result);
}

void printCanvas(int *canvas, int maxX, int maxY)
{
    for (int y = 0; y < maxY; y++)
    {
        for (int x = 0; x < maxX; x++)
        {
            if (canvas[x + maxX * y])
                printf("%d", canvas[x + maxX * y]);
            else
                printf(".");
        }
        printf("\n");
    }
}