//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
D=M-D
M=0
@FALSE0
D;JNE
@SP
A=M-1
M=-1
(FALSE0)
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
D=M-D
M=0
@FALSE1
D;JNE
@SP
A=M-1
M=-1
(FALSE1)
//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
D=M-D
M=0
@FALSE2
D;JNE
@SP
A=M-1
M=-1
(FALSE2)
//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
D=M-D
M=0
@FALSE3
D;JGE
@SP
A=M-1
M=-1
(FALSE3)
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
D=M-D
M=0
@FALSE4
D;JGE
@SP
A=M-1
M=-1
(FALSE4)
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
D=M-D
M=0
@FALSE5
D;JGE
@SP
A=M-1
M=-1
(FALSE5)
//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
D=M-D
M=0
@FALSE6
D;JLE
@SP
A=M-1
M=-1
(FALSE6)
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
D=M-D
M=0
@FALSE7
D;JLE
@SP
A=M-1
M=-1
(FALSE7)
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
D=M-D
M=0
@FALSE8
D;JLE
@SP
A=M-1
M=-1
(FALSE8)
//push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 53
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D+M
//push constant 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=M-D
//neg
@SP
A=M-1
M=-M
//and
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D&M
//push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
//or
@SP
A=M-1
D=M
M=0
@SP
M=M-1
A=M-1
M=D|M
//not
@SP
A=M-1
M=!M
