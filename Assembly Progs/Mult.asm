// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// initialise to zero
@0
D=A
@R2
M=D

// Create count variable based on R0 
@R0
D=M
@count
M=D
@ZERO  // Zero check
D;JEQ

// Create variable to be increased into the product from R1
@R1
D=M
@product
M=D
@ZERO  // Zero check
D;JEQ

// Loop that increments the product based on counts in count variable, if 0 then jump to Product
(LOOP)
// decrement count
@count
M=M-1
D=M

// check if count is at 0
@PRODUCT
D;JEQ

// increment product and loop
@R1
D=M
@product
M=M+D
@LOOP
0;JMP

(END)
0;JMP

(ZERO)
@0
D=A
@R2
M=D
@END
0;JMP

(PRODUCT)
@product
D=M
@R2
M=D
@END
0;JMP
