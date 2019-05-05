ABRA - A Bad RISC-V Assembler
----------------------
**(Work In Progress)**

An Assembler for the RV32I subset of the RISC-V ISA.

Status:
------
The following instruction types are implemented
- R-type
- I-type
- S-type
- U-type
- J-type

The instruction format is stored in file data.csv

Installation:
------
Clone the repository

	git clone https://github.com/daniyalm97/abra

Install python package dependencies

	pip install bitstring==3.1.5

Usage:
------
It runs as a python script and requires the input file as an arguement.

	python abra.py test.s

It generates a binary file out.bin in the same work directory.

Known-Issues:
-------------
- Comments and next line char at the end of test.s are not considered yet and return errors
- Very dirty code :P
