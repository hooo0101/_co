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
@SCREEN
M=D        
(LOOP)
    @KBD
    D=M        
    @CHECK_KEY
    D;JNE     
    @WHITE
    0;JMP       

(CHECK_KEY)
    @BLACK
    0;JMP       

(WHITE)
    @SCREEN
    M=D         
    D=0xFFFF    
    @SCREEN_LOOP
    M=D
    @SCREEN
    D=M+1
    @SCREEN_LOOP
    @LOOP
    0;JMP

(BLACK)
    @SCREEN
    M=D         
    D=0x0000    
    @SCREEN_LOOP2
    M=D
    @SCREEN
    D=M+1 
    @SCREEN_LOOP2