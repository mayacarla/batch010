#Maya Carla Loletha Anderson
#July 2022
#this program loops until it has reached 50

ADDI $s0, $zero, 0 #set s0 to num(zero)
ADDI $s1, $zero, 1 #use to increase counter, $s0
ADDI $s2, $zero, 50

AGAIN: ADD $s0, $s0, $s1
BEQ $s0, $s2, DONE
J AGAIN
DONE:
