## CS415_Project_02
By Nicholas Keng and Ryan McAlpine
 
### About:
This python program makes use of Karatsuba multiplication to either multiply or exponentiate two values A and B (<=1000) after initially converting them into lists of single digits.

### Instructions:
When executing the program, enter 1 for multiplication, enter 2 for exponentiation, or enter 3 to quit. 

For task 1, the expected output is the accurate result of inputs A and B multiplied (A*B).

For task 2, the expected output is the accurate result of raising input A to the power of B (A^B).

### Known Issues:
If the function subtract_arrays(A, B) is given parameters such that A < B, its return value will be incorrect. In other words, the function as it is written is incapable of handling negative values. This does not seem to cause any problems when it is called by karatsuba_mult(), however, so we have left it as is for now.
