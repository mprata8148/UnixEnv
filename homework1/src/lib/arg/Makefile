CC      := gcc
AR      := ar
CFLAGS  := -Wall -Wextra -g -I../../../include
ARFLAGS := rcs

OUTDIR  := ../../../lib
LIB     := $(OUTDIR)/libarg.a

SRC     := getarg.c
OBJ     := getarg.o

.PHONY: all clean

all: $(LIB)

$(LIB): $(OBJ) | $(OUTDIR)
	$(AR) $(ARFLAGS) $@ $^

$(OBJ): $(SRC)
	$(CC) $(CFLAGS) -c $< -o $@

$(OUTDIR):
	mkdir -p $(OUTDIR)

clean:
	rm -f $(OBJ) $(LIB)
