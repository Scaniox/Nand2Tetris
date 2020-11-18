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
(Sys.init) // function
@4000 // push constant 4000
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // pop pointer 0
M=M-1
A=M
D=M
@3
M=D
@5000 // push constant 5000
D=A
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
@Sys.init&ret.1 // call Sys.main //save return address
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
@Sys.main
0;JMP
(Sys.init&ret.1)
@SP // pop temp 1
M=M-1
A=M
D=M
@6
M=D
(Sys.Sys.init$LOOP)
// goto
@Sys.Sys.init$LOOP
0;JMP
(Sys.main) // function
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
@0 // push constant 0
D=A
@SP
A=M
M=D
@SP
M=M+1
@4001 // push constant 4001
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // pop pointer 0
M=M-1
A=M
D=M
@3
M=D
@5001 // push constant 5001
D=A
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
@200 // push constant 200
D=A
@SP
A=M
M=D
@SP
M=M+1
@1 // pop local 1
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
@1
D=A
@LCL
M=M-D
@40 // push constant 40
D=A
@SP
A=M
M=D
@SP
M=M+1
@2 // pop local 2
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
@2
D=A
@LCL
M=M-D
@6 // push constant 6
D=A
@SP
A=M
M=D
@SP
M=M+1
@3 // pop local 3
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
@3
D=A
@LCL
M=M-D
@123 // push constant 123
D=A
@SP
A=M
M=D
@SP
M=M+1
@Sys.main&ret.2 // call Sys.add12 //save return address
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
@Sys.add12
0;JMP
(Sys.main&ret.2)
@SP // pop temp 0
M=M-1
A=M
D=M
@5
M=D
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
@LCL // push local 2
D=M
@2
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@LCL // push local 3
D=M
@3
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@LCL // push local 4
D=M
@4
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
@SP // add
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D+M
@SP // add
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D+M
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
(Sys.add12) // function
@4002 // push constant 4002
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // pop pointer 0
M=M-1
A=M
D=M
@3
M=D
@5002 // push constant 5002
D=A
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
@12 // push constant 12
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
