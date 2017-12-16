### Project Abstract
This project creates a simulation in python of ternary computer architecture, starting with basic ternary gates to muxes, adders and regs. The code can be used to build other components, and it is possible to build an entire cpu and more. 

### Project Motivation
Ternary numeral system uses base 3 instead of the binary base 2 that is typically used in computers. Base 3 has the lowest (most efficient) radix economy. Radix economy E(b,N) for any particular number N in a given base b is defined as E(b,N) = b*floor(logbN + 1). Base 3 has the lowest average radix economy of 2.73, followed by base 2 of 2.89. Read more about radix economy [here](https://en.wikipedia.org/wiki/Radix_economy).

Besides being an efficient base, ternary arithimetic has easy addition and multiplication with negative numbers. If we use -1, 0 and 1 as the three possible value for each trit (the ternary bit), 1 represents a positive (+), -1 represents a negative (-) and 0 represents zero. For example, 1 is 0 0 + , 2 is 0 + - (3 - 1 = 2), 3 is 0 + 0, 4 is 0 + + and 5 is + - - (9-3-1 = 5). -1 is 0 0 -, -2 is 0 - + (-3+1 = -2), -3 is 0 - 0, -4 is 0 - -, and -5 is - + + (-9+3+1 = -5).
This notation system makes it easy to add 2 numbers, as 1 + 1 = + -, (-1) + (-1) = - +, 1 + (-1) = 0 0, and so on. 

### The Basic Gates
The basic gates implemented in the code are referenced off this webpage: [Douglas Jones on Ternary Gates](http://homepage.divms.uiowa.edu/~jones/ternary/logic.shtml). The single input gates are Identity (output = input), Negation (output = ~Input), Increment (output = Input + 1), and Decoders (ouput = (input = a)). For two input gates, the binary And gate becomes a Min gate in ternary, and the binary Or gate becomes a Max gate. Most ternary logic gates can be built from a combination of the single input gates, And gate, and Or gate.    

### Component Implementation in python: Adder
The implementation of the adder is very similar to Lab1 in class where we implemented an alu in verilog. Instead of using XOR to sum two bits in binary, in ternary a sum function is used (also defined in the Douglas W. Jones on gates link above). For the carryout, a consensus function is used. Because this is implemented in python, there is also two functions that convert decimal to ternary and vice versa. The code is in adder.py.
![Screenshot of Adder adding numbers in Ternary](https://github.com/xiaozhengxu/TernaryCompArch/blob/master/Adder%20screenshot.png)

### Component Implementation in python: Mux
A 3 to 1 mux is also implemented in a similar way to a binary mux. A decoder, three And gates and a Or gate are used to construct the mux. It is written and tested in ternaryMux.py and mux_test.py. 

### Component Analysis: Gated D latch (Register)
A binary SR latch does not translate directly to ternary. Three values per wire introduces many illegal state into the binary SR latch. As a result, it is fairly complicated to build a ternary latch with simple and straight forward behavior. 

### Project Extensions
1. Add Delay modeling to each gate and component.
2. Build a ternary story teller by converting letters to ternary, and incrementing the story line using the oscillator and mux. 
3. Build a ternary CPU (including building more components)

### Credits
Most of gates.py and gates_test.py are written by Mitchell Kwock @mtkwock. These two files are copied from his [repository](https://github.com/mtkwock/ternary). The rest of the code are written by me. 
