addi x3,x0,-5
slli x3,x3,12
addi x4,x0,256
beq x4,x4,goto
addi x0,x0,0
addi x0,x0,0
addi x0,x0,0
goto:
or x31,x3,x4
