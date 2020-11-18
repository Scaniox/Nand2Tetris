// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
    @R2
    M=0 // zero sum

(LOOP)
    @R1
    D=M
    @END
    D;JLE // jump out of loop if counter <=0

    @R0
    D=M // put first value in D
    @R2
    M=D+M // add D to the sum
    @R1
    MD=M-1 // subtract 1 from R1, the counter
    @LOOP
    0;JMP

(END)
    @END
    0;JMP
