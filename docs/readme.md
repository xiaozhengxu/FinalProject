### Project Abstract
This project creates a simulation in python of ternary computer architecture, starting with basic ternary gates to muxes, adders and counters. The final product is a story stored in ternary representation and told using a ternary clock. The code can be used to build other components, and it is possible to build an entire cpu and more. 

### Project Motivation
Ternary numeral system uses base 3 instead of the binary base 2 that is typically used in computers. Base 3 has the lowest (most efficient) radix economy. Radix economy E(b,N) for any particular number N in a given base b is defined as E(b,N) = b*floor(logbN + 1). Base 3 has the lowest average radix economy of 2.73, followed by base 2 of 2.89. Read more about radix economy here https://en.wikipedia.org/wiki/Radix_economy.

Besides being an efficient base, ternary arithimetic has easy addition and multiplication with negative numbers. If we use -1, 0 and 1 as the three possible value for each trit (the ternary bit), 1 represents a positive (+), -1 represents a negative (-) and 0 represents zero. For example, 1 is 0 0 + , 2 is 0 + - (3 - 1 = 2), 3 is 0 + 0, 4 is 0 + + and 5 is + - - (9-3-1 = 5). -1 is 0 0 -, -2 is 0 - + (-3+1 = -2), -3 is 0 - 0, -4 is 0 - -, and -5 is - + + (-9+3+1 = -5).
This notation system makes it easy to add 2 numbers, as 1 + 1 = + -, (-1) + (-1) = - +, 1 + (-1) = 0 0, and so on. 

### The Basic Gates
The basic gates implemented in the code are referenced off this webpage: http://homepage.divms.uiowa.edu/~jones/ternary/logic.shtml. The single input gates are Identity (output = input), Negation (output = ~Input), Increment (output = Input + 1), and Decoders (ouput = (input = a)). For two input gates, the binary And gate becomes a Min gate in ternary, and the binary Or gate becomes a Max gate. Most ternary logic gates can be built from a combination of the single input gates, And gate, and Or gate.    

### Component Implementation in python: Adder
The implementation of the adder is very similar to Lab1 in class where we implemented an alu in verilog. Instead of using XOR to sum two bits in binary, in ternary a sum function is used (also defined in the Douglas W. Jones on gates link above). For the carryout, a consensus function is used. Because this is implemented in python, there is also two functions that convert decimal to ternary and vice versa. 

### Component Implementation in python: Mux


### Component Implementation in python: Flip Flop (Register)


### Atribution of part of the code
Most of gates.py and gates_test.py are written by @mkwock. These two files are copied from his repository: 
