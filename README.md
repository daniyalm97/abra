ABRA - A Bad RISC-V Assembler
----------------------
**(Work In Progress)**

An Assembler for the RV32I subset of the RISC-V ISA.

Status:
------
The instruction format is stored in file data.csv

The following instruction types are yet to be implemented
- B-type
- U-type
- J-type

Usage:
------
It runs as a python script and requires the input file as an arguement.

	python ong-dong-geembler.py test.s

It generates a binary file out.bin in the same work directory.

Known-Issues:
-------------
- Default ASM format for load and store instructions not considered
- Comments and next line char at the end of test.s are not considered yet and return errors
- Dirty code :P
