CC = gcc
CFLAGS = -Wall -g -fPIC

all: Clib.so

Clib.so: compression.o dataPreparation.o huffman.o
	$(CC) compression.o dataPreparation.o huffman.o -shared -o Clib.so

compression.o: compression.c
	$(CC) $(CFLAGS) -c compression.c

dataPreparation.o: dataPreparation.c dataPreparation.h
	$(CC) $(CFLAGS) -c dataPreparation.c

huffman.o: huffman.c huffman.h
	$(CC) $(CFLAGS) -c huffman.c

clean:
	rm compression.o dataPreparation.o huffman.o Clib.so
