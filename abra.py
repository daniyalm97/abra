"""
A Bad RISC-V Assembler
"""
import sys
import binascii
from bitstring import Bits
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
Outfile = open('../prog.txt','w')
bin_instr=[]
label=[]
lc=[]
v=1
for r in range(0,len(lines)):
	if lines[r][-2]==':':
		label.append(lines[r][:-2])
		lc.append(r+2-len(label))
for n in range(0,len(lines)):
	if lines[n][-2]!=':':
		op = lines[n].split()
	else:
		continue
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
				if param[1][0] == 'x':
					bin_instr.insert(0,format(int(param[1][1:]),'05b'))
				else:
					tp = param[1].split('(')
					param[1]=tp[1][:-1]
					param.insert(2,tp[0])
					bin_instr.insert(0,format(int(param[1][1:]),'05b'))
				if instr=='slli' or instr=='srli' or instr=='srai':
					func7 = word[4]
					bin_instr.insert(0,format(int(param[2]),'05b'))
					bin_instr.insert(0,func7[:-1])
				else:
					if param[2][0] == '-':
						neg = Bits(int=int(param[2]),length=12)
						bin_instr.insert(0,neg.bin)
					else:
						bin_instr.insert(0,format(int(param[2]),'012b'))	
			if word[1] == 's': #S-Type
				func3 = word[3]
				tp = param[1].split('(')
				param[1]=tp[1][:-1]
				param.insert(2,tp[0])
				if param[2][0] == '-':
					neg = Bits(int=int(param[2]),length=12)
					imm = neg.bin
				else:
					imm = format(int(param[2]),'012b')
				bin_instr.insert(0,imm[7:])
				bin_instr.insert(0,func3)
				bin_instr.insert(0,format(int(param[1][1:]),'05b'))
				bin_instr.insert(0,format(int(param[0][1:]),'05b'))
				bin_instr.insert(0,imm[:7])
			if word[1] == 'u': #U-Type
				bin_instr.insert(0,format(int(param[0][1:]),'05b'))
				bin_instr.insert(0,format(int(param[1][2:],16),'020b'))
			if word[1] == 'j': #J-Type
				bin_instr.insert(0,format(int(param[0][1:]),'05b'))
				if param[1][0] == '-':
					neg = Bits(int=int(param[1]),length=20)
					imm = neg.bin
				else:
					imm = format(int(param[1]),'020b')
				bin_instr.insert(0,imm[0]+imm[10:]+imm[9]+imm[1:9])
			if word[1]=='b': #B-Type
				func3 = word[3]
				if param[2] in label:
					if n>lc[label.index(param[2])]:
						neg = Bits(int=int(lc[label.index(param[2])]-(n)),length=12)
					else:
						neg = Bits(int=int(lc[label.index(param[2])]-(n+1)),length=12)
					imm = neg.bin
					bin_instr.insert(0,imm[8:]+imm[1])
					bin_instr.insert(0,func3)
					bin_instr.insert(0,format(int(param[0][1:]),'05b'))
					bin_instr.insert(0,format(int(param[1][1:]),'05b'))
					bin_instr.insert(0,imm[0]+imm[2:8])
					param[2] = lc[label.index(param[2])]-(n+1)
	out = ''.join(bin_instr)
	ol = hex(int(out,2))[2:]
	ol = ol[:-1] if ol[-1]=='L' else ol
	for l in range(8-len(ol)):
		ol = '0'+ol
	Outfile.write(out+'\n')#binascii.unhexlify(ol))
	sp=' '
	print format(v,'02d'),lines[n][:-1],sp*(20-len(lines[n]))+'->'+sp,out,sp+'='+sp,'0x{}'.format(ol)
	del bin_instr[:]
	v=v+1
print '-----------------------'
print 'Output to file: prog.txt'
