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

(KEYBOARD)
// handle if depress or not
@KBD
D=M
@BLACK
D;JGT
@WHITE
D;JEQ

// Make loop for black screen
(BLACK)
  // set counter max = 8192
  @8192
  D=A
  @count
  M=D

  // set i = 0
  @0
  D=A
  @i
  M=D

  // set pointer to starting address
  @16384
  D=A
  @screen
  M=D
  // Check count if at end of screen, if so jump to check for keyboard state change
  (DRAWB)
  @count
  D=M
  @KEYBOARD
  D;JEQ

  // Draw all black
  @screen
  D=M
  @i
  A=D+M
  M=-1
  
  // increment counters
  @count
  M=M-1
  @i
  M=M+1
  @DRAWB
  0;JMP

// Make loop for white screen
(WHITE)
  // set counter max = 8192
  @8192
  D=A
  @count
  M=D

  // set i = 0
  @0
  D=A
  @i
  M=D

  // set pointer to starting address
  @16384
  D=A
  @screen
  M=D
  // Check count if at end of screen, if so jump to check for keyboard state change
  (DRAWW)
  @count
  D=M
  @KEYBOARD
  D;JEQ

  // Draw all white
  @screen
  D=M
  @i
  A=D+M
  M=0
  
  // increment counters
  @count
  M=M-1
  @i
  M=M+1
  @DRAWW
  0;JMP
