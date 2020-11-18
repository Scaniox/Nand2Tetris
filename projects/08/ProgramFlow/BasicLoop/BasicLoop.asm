@256 //boostrap code
D=A
@SP
M=D
@0 // push constant 0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0 // pop local 0
D=A
@LCL
M=D+M
@SP
A=M-1
D=M
M=0
@LCL
A=M
M=D
@SP
M=M-1
@0
D=A
@LCL
M=M-D
(BasicLoop.None$LOOP_START)
@ARG // push argument 0
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@LCL // push local 0
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // add
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D+M
@0 // pop local 0
D=A
@LCL
M=D+M
@SP
A=M-1
D=M
M=0
@LCL
A=M
M=D
@SP
M=M-1
@0
D=A
@LCL
M=M-D
@ARG // push argument 0
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@1 // push constant 1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // sub
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=M-D
@0 // pop argument 0
D=A
@ARG
M=D+M
@SP
A=M-1
D=M
M=0
@ARG
A=M
M=D
@SP
M=M-1
@0
D=A
@ARG
M=M-D
@ARG // push argument 0
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // if goto
M=M-1
A=M
D=M
@BasicLoop.None$LOOP_START
D;JGT
@LCL // push local 0
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
