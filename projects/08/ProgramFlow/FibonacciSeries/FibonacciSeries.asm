@256 //boostrap code
D=A
@SP
M=D
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
@SP // pop pointer 1
M=M-1
A=M
D=M
@4
M=D
@0 // push constant 0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0 // pop that 0
D=A
@THAT
M=D+M
@SP
A=M-1
D=M
M=0
@THAT
A=M
M=D
@SP
M=M-1
@0
D=A
@THAT
M=M-D
@1 // push constant 1
D=A
@SP
A=M
M=D
@SP
M=M+1
@1 // pop that 1
D=A
@THAT
M=D+M
@SP
A=M-1
D=M
M=0
@THAT
A=M
M=D
@SP
M=M-1
@1
D=A
@THAT
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
@2 // push constant 2
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
(FibonacciSeries.None$MAIN_LOOP_START)
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
@FibonacciSeries.None$COMPUTE_ELEMENT
D;JGT
// goto
@FibonacciSeries.None$END_PROGRAM
0;JMP
(FibonacciSeries.None$COMPUTE_ELEMENT)
@THAT // push that 0
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // push that 1
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
@2 // pop that 2
D=A
@THAT
M=D+M
@SP
A=M-1
D=M
M=0
@THAT
A=M
M=D
@SP
M=M-1
@2
D=A
@THAT
M=M-D
@4 // push pointer 1
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
@SP // add
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D+M
@SP // pop pointer 1
M=M-1
A=M
D=M
@4
M=D
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
// goto
@FibonacciSeries.None$MAIN_LOOP_START
0;JMP
(FibonacciSeries.None$END_PROGRAM)
