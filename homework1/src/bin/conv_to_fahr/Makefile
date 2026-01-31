CC      := gcc
CFLAGS  := -Wall -Wextra -g -I../../../include
LDFLAGS := -L../../../lib -ltemp_conv
LDLIBS :=  -larg

OUTDIR  := ../../../bin
TARGET  := $(OUTDIR)/conv_to_fahr

SRC     := conv_to_fahr.c
OBJ     := conv_to_fahr.o
STATICLIBS    :=  ../../../lib/libtemp_conv.a ../../../lib/libarg.a
.PHONY: all clean

all: $(TARGET)

# LINK step (depends on object file AND the library)
$(TARGET): $(OBJ) $(STATICLIBS) | $(OUTDIR)
	$(CC) $(OBJ) $(LDFLAGS) $(LDLIBS) -o $@

# COMPILE step (depends on source AND headers)
$(OBJ): $(SRC) ../../../include/temp_conv.h ../../../include/getarg.h
	$(CC) $(CFLAGS) -c $< -o $@

$(OUTDIR):
	mkdir -p $(OUTDIR)

clean:
	rm -f $(OBJ) $(TARGET)
