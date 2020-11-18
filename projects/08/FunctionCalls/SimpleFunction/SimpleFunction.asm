@256 //boostrap code
D=A
@SP
M=D
(SimpleFunction.test) // function
@0 // push constant 0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0 // push constant 0
D=A
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
@LCL // push local 1
D=M
@1
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
@SP // not
A=M-1
M=!M
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
@SP // add
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D+M
@ARG // push argument 1
D=M
@1
A=D+A
D=M
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
@LCL // return
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG // return stack pointer
D=M+1
@SP
M=D
@R13 // return memory segment THAT
M=M-1
A=M
D=M
@THAT
M=D
@R13 // return memory segment THIS
M=M-1
A=M
D=M
@THIS
M=D
@R13 // return memory segment ARG
M=M-1
A=M
D=M
@ARG
M=D
@R13 // return memory segment LCL
M=M-1
A=M
D=M
@LCL
M=D
@R14 // jump to return address
A=M
0;JMP
