"""
This is a script to simulate a ternary search, and a ternary adder based on basic ternary gates 

author: @xiaozhengxu
"""

def negation_gate(a):
	"""Takes in input in the form of -1, 0 or 1"""
	assert a in [-1, 0, 1]
	if a == 0:
		return 0
	else:
		return a*(-1)

def increment1(a):
	"""Takes in input in the form of -1, 0 or 1"""
	assert a in [-1, 0, 1]
	if a == -1:
		return 0
	elif a == 0:
		return 1
	elif a == 1:
		return -1

def decrement1(a):
	"""Takes in input in the form of -1, 0 or 1"""
	assert a in [-1, 0, 1]
	if a == -1:
		return 1
	elif a == 0:
		return -1
	elif a == 1:
		return 0

def min_and_gate(a, b):
	"""Takes in trit a and b in the form of -1, 0 or 1""" 
	if a<=b:
		return a
	else:
		return b

def max_or_gate(a, b):
	"""Takes in trit a and b in the form of -1, 0 or 1""" 
	if a>=b:
		return a
	else:
		return b

