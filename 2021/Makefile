.PHONY: all clean

CFLAGS = -Wall -Werror
CC = gcc
DAY = 04
SRCDIR = Day$(DAY)
TARGET = Day$(DAY)

all: $(TARGET)

clean:
	rm -f *.o $(TARGET)/*.o

$(TARGET): $(SRCDIR)/$(TARGET).o input.o
	$(CC) $(CFLAGS) $^ -o $(SRCDIR)/$@

$(SRCDIR)/$(TARGET).o: $(SRCDIR)/$(TARGET).c input.h
	$(CC) $(CFLAGS) -c $< -o $@

input.o: input.c 
	$(CC) $(CFLAGS) -c $< -o $@