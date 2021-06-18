# SalesChoice_Onboarding_Task

#### Project Goal

The goal of this project was to create a command line interface for the 'Tower of Hanio' game.

#### Files

There are 2 files here, a .py python file and a video of me live coding the python code.

#### Overview

  -	Define global variables
  -	Create display function
  -	Create move function
  -	Create help function
  -	Create the game loop


#### Result

Global Variables:
The global variables set up the main variables every function needs. These included:
-	Defining all the pegs in the game (pegs)
-	Defining all the disks in the game (local_disks)
-	The disks in each peg (A, B and C which are all lists)
-	A reference to the solution we are looking for

Display Function:
The display function is supposed to display all the disks in a specified peg. We show the user all the current pegs in the game and then print the list corresponding to the user’s choice. If the user chose a non-existent peg, we output an error message.

Move Function:
The move function is responsible for moving one disk from one peg to another. We start of by asking the user what they want, what disk they want to move, where is the disk and where do they want to move it. Then we verify if the disk and pegs are in the game space. We take the input peg name which is a string and link it to the corresponding list. After we check if the disk is in the source peg and if there are no other disk(s) on top of the target disk. When all these conditions are met, we pop the disk from the source peg and append it to the destination list. When ever move is complete, we check if the game is solved by comparing the target peg (in this case peg C) with the reference solution (ref_sol).

Help Function:
The help function is supposed to answer some question the user may have. Here I just added the instructions for the game, as I myself have never heard of this game till now.
Game Loop:
The game loop is a menu in an infinite while loop. In this loop we ask the user what they would like to do and link the user input to the corresponding function. In the menu we can break out of the while loop if we want to end the game.


#### Conclusion

While there are several other thing I want to try to make the code more appealing and efficent (using pygames to create a visuallization or using dict to link user input with lists), I feel like the current product so far is good based on the limited time and my lack of UI skills. The game runs as intended based on the product and game rules.
