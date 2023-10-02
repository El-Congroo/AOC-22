#include "input.h"

void die(char *msg) {
    perror(msg);
    exit(EXIT_FAILURE);
}

char **readInput(char *filePath, int *len)
{
    FILE *fptr;
    if(!(fptr = fopen(filePath, "r")))
        die("fopen");

    char buffer[MAXLINELENGTH];
    int curLine = 0;
    int maxLine = 16;
    char **ret = calloc(maxLine+1, sizeof(char *));
    if(!ret)
        die("calloc");

    while(fgets(buffer, MAXLINELENGTH, fptr)) {
        int size = strlen(buffer);
        char *save;
        if (!(save = calloc(size + 1, sizeof(char))))
            die("calloc");

        strcpy(save, buffer);
        if (save[size-1] == '\n')
            save[size-1] = '\0';

            // reallocs new memory as needed
            if (curLine == maxLine)
            {
                maxLine = maxLine << 1;
                if (!(ret = (char **)realloc(ret, maxLine * sizeof(char *))))
                    die("realloc");
            }
        ret[curLine++] = save;
    }

    fclose(fptr);
    *len = curLine;
    return ret;
}
