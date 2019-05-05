addi x3,x3,-5
slli x3,x3,12
try:
addi x4,x0,256
ori x31,x31,2047
lb x13,-64(x22)
beq x5,x4,try
so:
addi x0,x0,0
bne x0,x0,so
