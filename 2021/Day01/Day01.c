#include "../input.h"

int main(int argc, char **argv) {

    int len;
    char **input = readInput("data/input01.txt", &len);

    for(int i=0; i<len; i++) {
        printf("%s\n", input[i]);
    }
    

}
