#include <stdio.h>
#include <stdlib.h>

#define ASCII_QUANTITY_CHARS 256

void extractCharsAndFreqs(char *filename, char** outChars, int** outFreqs, int* outSize);
void terminateProgram();