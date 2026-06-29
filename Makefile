# File: Makefile
# Author: Amlal El Mahrouss
# Purpose: Generate HTML and PDF papers from LaTex documents.
# (C) 2026 Amlal El Mahrouss.

PDFTEX ?= pdflatex
HTMLTEX ?= htlatex
RM := rm -rf
ECHO := @echo

.PHONY: all
all: clean
	ECHO "[SRC] Cleanup is done."

.PHONY: clean
clean:
	RM *.4ct *.4tc *.aux *.css *.pdf *.html *.tmp *.dvi *.idv *.lg *.log *.xref *.out *.png

include p1.mk
include p2.mk
include p3.mk
include p4.mk
include p5.mk
include p6.mk
