#ifndef INPUT_HPP
#define INPUT_HPP

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXLINELENGTH 512

char **readInput(char *filePath, int *len);
void die(char *msg);

#endif 