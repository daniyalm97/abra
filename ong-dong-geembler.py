"""
A Bad RISC-V Assembler
Authored by DD
"""
import sys
import binascii
try:
	Infile = sys.argv[1]
except:
	print 'No input file'
	sys.exit()
with open(Infile,'r') as i:
	lines=i.readlines()
try:
	fil = open('data.csv','r')
	data = fil.readlines()
except:
	print 'data.csv file missing'
	sys.exit()
Outfile = open('out.bin','w')
bin_instr=[]
for n in range(0,len(lines)):
	op = lines[n].split()
	instr,param = op[0],op[1].split(',')
	for line in data:
		word = line.split(',')
		if instr == word[0]:
			opcode = word[2]
			bin_instr.append(opcode)
			if word[1] == 'r': #R-Type
				func3,func7 = word[3],word[4]
				bin_instr.insert(0,format(int(param[0][1:]),'05b'))
				bin_instr.insert(0,func3)
				bin_instr.insert(0,format(int(param[1][1:]),'05b'))
				bin_instr.insert(0,format(int(param[2][1:]),'05b'))
				bin_instr.insert(0,func7[:-1])
			if word[1] == 'i': #I-Type
				func3 = word[3]
				bin_instr.insert(0,format(int(param[0][1:]),'05b'))
				bin_instr.insert(0,func3)
				bin_instr.insert(0,format(int(param[1][1:]),'05b'))
				if instr=='slli' or instr=='srli' or instr=='srai':
					bin_instr.insert(0,format(int(param[2]),'05b'))
					bin_instr.insert(0,func7[:-1])
				else:
					bin_instr.insert(0,format(int(param[2]),'012b'))	
			if word[1] == 's': #S-Type
				func3 = word[3]
				bin_instr.insert(0,format(int(param[2]),'012b')[-5:])
				bin_instr.insert(0,func3)
				bin_instr.insert(0,format(int(param[0][1:]),'05b'))
				bin_instr.insert(0,format(int(param[1][1:]),'05b'))
				bin_instr.insert(0,format(int(param[2]),'012b')[:-5])				
	out = ''.join(bin_instr)
	ol = hex(int(out,2))[2:]
	for l in range(8-len(ol)):
		ol = '0'+ol
	Outfile.write(binascii.unhexlify(ol))
	print (n+1),lines[n][:-1],'->',out,'=',hex(int(out,2))
	del bin_instr[:]
print '-----------------------'
print 'Output to file: out.bin'
