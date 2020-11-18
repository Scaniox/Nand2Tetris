@256 //boostrap code
D=A
@SP
M=D
@None&ret.0 // call Sys.init //save return address
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL //saving frame (LCL)
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG //saving frame (ARG)
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS //saving frame (THIS)
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT //saving frame (THAT)
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP //move ARG
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP //move LCL
D=M
@LCL
M=D
@Sys.init
0;JMP
(None&ret.0)
@None&ret.0
0;JMP
(Main.fibonacci) // function
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
@SP // lt
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
D=M-D
M=0
@FALSE0
D;JGE
@SP
A=M-1
M=1
(FALSE0)
@SP // if goto
M=M-1
A=M
D=M
@Main.Main.fibonacci$IF_TRUE
D;JGT
// goto
@Main.Main.fibonacci$IF_FALSE
0;JMP
(Main.Main.fibonacci$IF_TRUE)
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
(Main.Main.fibonacci$IF_FALSE)
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
@Main.fibonacci&ret.1 // call Main.fibonacci //save return address
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL //saving frame (LCL)
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG //saving frame (ARG)
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS //saving frame (THIS)
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT //saving frame (THAT)
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP //move ARG
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP //move LCL
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci&ret.1)
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
@Main.fibonacci&ret.2 // call Main.fibonacci //save return address
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL //saving frame (LCL)
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG //saving frame (ARG)
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS //saving frame (THIS)
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT //saving frame (THAT)
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP //move ARG
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP //move LCL
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci&ret.2)
@SP // add
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D+M
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
(Sys.init) // function
@4 // push constant 4
D=A
@SP
A=M
M=D
@SP
M=M+1
@Sys.init&ret.3 // call Main.fibonacci //save return address
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL //saving frame (LCL)
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG //saving frame (ARG)
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS //saving frame (THIS)
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT //saving frame (THAT)
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP //move ARG
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP //move LCL
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Sys.init&ret.3)
(Sys.Sys.init$WHILE)
// goto
@Sys.Sys.init$WHILE
0;JMP
