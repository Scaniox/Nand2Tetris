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
(Class1.set) // function
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
@SP // pop static 0
M=M-1
A=M
D=M
@Class1.0
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
@SP // pop static 1
M=M-1
A=M
D=M
@Class1.1
M=D
@0 // push constant 0
D=A
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
(Class1.get) // function
@Class1.0 // push static 0
D=M
@SP
A=M
M=D
@SP
M=M+1
@Class1.1 // push static 1
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
(Class2.set) // function
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
@SP // pop static 0
M=M-1
A=M
D=M
@Class2.0
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
@SP // pop static 1
M=M-1
A=M
D=M
@Class2.1
M=D
@0 // push constant 0
D=A
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
(Class2.get) // function
@Class2.0 // push static 0
D=M
@SP
A=M
M=D
@SP
M=M+1
@Class2.1 // push static 1
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
(Sys.init) // function
@6 // push constant 6
D=A
@SP
A=M
M=D
@SP
M=M+1
@8 // push constant 8
D=A
@SP
A=M
M=D
@SP
M=M+1
@Sys.init&ret.1 // call Class1.set //save return address
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
@2
D=D-A
@ARG
M=D
@SP //move LCL
D=M
@LCL
M=D
@Class1.set
0;JMP
(Sys.init&ret.1)
@SP // pop temp 0
M=M-1
A=M
D=M
@5
M=D
@23 // push constant 23
D=A
@SP
A=M
M=D
@SP
M=M+1
@15 // push constant 15
D=A
@SP
A=M
M=D
@SP
M=M+1
@Sys.init&ret.2 // call Class2.set //save return address
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
@2
D=D-A
@ARG
M=D
@SP //move LCL
D=M
@LCL
M=D
@Class2.set
0;JMP
(Sys.init&ret.2)
@SP // pop temp 0
M=M-1
A=M
D=M
@5
M=D
@Sys.init&ret.3 // call Class1.get //save return address
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
@Class1.get
0;JMP
(Sys.init&ret.3)
@Sys.init&ret.4 // call Class2.get //save return address
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
@Class2.get
0;JMP
(Sys.init&ret.4)
(Sys.Sys.init$WHILE)
// goto
@Sys.Sys.init$WHILE
0;JMP
