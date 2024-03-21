#include "dataPreperation.h"
#include "huffman.h"

int main(int argc, char *argv[]) {
    char* chars;
    int* freqs;
    int size;
    table *huffmanTableCodes;
    FILE *file = fopen("HuffmanCodes.txt", "w");

    extractCharsAndFreqs(argv[1], &chars, &freqs, &size);
    huffmanCodes(file,argv[1],chars, freqs, size);
    printf("worked");

    free(chars);
    free(freqs);

    return 0;
}

