CC      := gcc
AR      := ar
CFLAGS  := -Wall -Wextra -g -I../../../include
ARFLAGS := rcs

OUTDIR  := ../../../lib
LIB     := $(OUTDIR)/libtemp_conv.a

SRC     := temp_conv.c
OBJ     := temp_conv.o

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
