#include "dataPreparation.h"
#include "huffman.h"

int main(int argc, char *argv[]) {
    char* chars;
    int* freqs;
    int size;
    table *huffmanTableCodes;
    FILE *file = fopen(argv[2], "w");

    extractCharsAndFreqs(argv[1], &chars, &freqs, &size);
    huffmanCodes(file,argv[1],chars, freqs, size);
    printf("worked");

    free(chars);
    free(freqs);
    return 0;
}

