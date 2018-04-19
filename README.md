# nqueens

In my first semester, we had to solve the n-queens problem as an exercise in Racket.
Let's see what it looks like after I (almost) finished my Master's in Computer Sience.

## The Problem
The task is, to find the number of possible combinations for the placement of n queens on a 
nxn grid where no queen is able to threaten any other. ([wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle))

## hundredsemesters later
With a backpack full of algorithms, lets see what can be thrown on the nqueens problem.

 - Implemented a naive version of nqueens, passes the tests, works! (4ba81997afd4bacdc5f5e82cd600eb2952b6b4b8)
 - Implemented a more sophisticated approach to checing if a field is blocked. Twice as fast! Yay! (dc97dbfed628cd26d53433210890905d80c88e35)
 - Lets make it a bit harder and also count the unique solutions. A solution is only counted when no rotated or mirrored version of that solution is already found.
   - naive approach implemented.
