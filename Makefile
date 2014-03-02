# Makefile
#
# This Makefile will compile abcpp using Linux, djgpp or mingw out of the box.
# If you use cygwin but want to make a mingw binary, change CFLAGS below.

ABC2PRT = abc2prt
CC      = gcc
VERSION = 1.0.1
# settings for Linux, djgpp or mingw32
CFLAGS  = -O3 -Wall 
# to make a mingw executable using cygwin, use these CFLAGS:
# CFLAGS = -O3 -Wall -mno-cygwin -DWIN32

SOURCE  = $(ABC2PRT).c

$(ABC2PRT): $(SOURCE)
	$(CC) $(CFLAGS) -o $(ABC2PRT) $(SOURCE)

tgz:    $(ABC2PRT)
	ln -s . $(ABC2PRT)-$(VERSION); \
	tar -zcvf $(ABC2PRT)-$(VERSION).tar.gz \
	COPYING abc2prt.spec Makefile* README $(SOURCE)

clean:
	rm -f *.o

# End of file Makefile
