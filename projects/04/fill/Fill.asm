// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
    @counter // stores which word of the screen is to be changed next
    M=0

(LOOP)
    @KBD
    D=M
    @FILL
    D;JNE // if a key is pressed jump to fill, else continue

    @counter
    D=M
    @LOOP
    D;JLT // jump to LOOP if counter is negative

    @counter
    D=M
    @SCREEN
    A=D+A   // select correct address
    M=0  // fill with all 0s

    @counter
    M=M-1

    @LOOP
    0;JMP

(FILL)
    @counter
    D=M
    @8192
    D=D-A
    @LOOP
    D;JGE //jump to LOOP if counter >= 8192

    @counter
    D=M
    @SCREEN
    A=D+A // select correct memory address for current screen segment
    D=0
    M=!D // fill with all 1s

    @counter
    M=M+1

    @LOOP
    0;JMP
