from gates import *
from gates_triadic import *
import math

class TernaryAdder:
	def __init__(self):

		self.operandA = [Wire() for i in range(9)]
		self.operandB = [Wire() for i in range(9)]
		self.connectPointA = [i for i in range(9)] #To be replaced with connectionPoints in AddTernary
		self.connectPointB = [i for i in range(9)]
		self.overflows = [Wire() for i in range(9)]
		self.result = [Wire() for i in range(9)]
		self.resultRead = [ConnectionPoint(ConnectionPoint.READER) for i in range(9)]
		self.gates = []
		
		self.decA = 0
		self.decB = 0
		self.decRes = 0
		self.triA = []
		self.triB = []
		self.output = []

	def addTernary(self, Adigits, Bdigits):
		"""Adigits: 
			[0,0,-1,1,1,0,1,1,1]
		   Bdigits:
		   	[1,0,-1,1,1,0,0,0,1]
		   The 0th element is the most significant trit
		"""
		if len(Adigits)<9:
			for j in range(9-len(Adigits)):
				Adigits.insert(0,0)
		if len(Bdigits)<9:
			padnum = 9-len(Bdigits)
			for j in range(padnum):
				Bdigits.insert(0,0)
		assert len(Adigits) == 9 and len(Bdigits) == 9
		self.triA = Adigits
		self.triB = Bdigits
		self.decA = self.convertToDecimal(Adigits)
		self.decB = self.convertToDecimal(Bdigits)
		#Connecting the wires to the input digits and result wires to the connection points:
		for i in range(9):
			self.connectPointA[i]= ConnectionPoint(ConnectionPoint.WRITER, state=Adigits[i])
			self.operandA[i].Connect(self.connectPointA[i])
			self.connectPointB[i]= ConnectionPoint(ConnectionPoint.WRITER, state=Bdigits[i])
			self.operandB[i].Connect(self.connectPointB[i])
			self.operandA[i].Update()
			self.operandB[i].Update()
			self.result[i].Connect(self.resultRead[i])

		zero = ConnectionPoint(ConnectionPoint.WRITER, state = 0)
		zeroWire = Wire()
		zeroWire.Connect(zero)

		#Doing the addition using 9 sum3 gates
		for k in range(9):

			curGate = GateSum3()
			curGate.SetInputWire1(self.operandA[8-k])
			curGate.SetInputWire2(self.operandB[8-k])
			self.operandA[8-k].Update()
			self.operandB[8-k].Update()
			if k == 0:
				curGate.SetInputWire3(zeroWire)
				zeroWire.Update()
			else:
				curGate.SetInputWire3(self.overflows[k-1])
				self.overflows[k-1].Update()
			curGate.SetOutputWire(self.result[8-k])
			self.result[8-k].Update() #Update the result wire: writes to resultRead
			curGate.SetOverflowWire(self.overflows[k])
			# self.gates.append(curGate)
			
		self.output = [cp.GetState() for cp in self.resultRead]
		self.decRes = self.convertToDecimal(self.output)

		self.reset()

	def reset(self):
		for k in range(9):
			self.operandA[k].DisconnectAll()
			self.operandB[k].DisconnectAll()
			self.result[k].DisconnectAll()
			self.overflows[k].DisconnectAll()

	def printResult(self):
		print (self.triA, self.decA)
		print (self.triB, self.decB)
		print (self.output, self.decRes)

	def convertToDecimal(self, digits):
		"""
		digits is a list of -1, 0 and 1s, 
		with the 0th element being the most significant (on the left).
		"""
		assert len(digits) == 9
		result = 0
		for i in range(9):
			if digits[i] == 1:
				result += 3**(8-i)
			elif digits[i] == -1:
				result -= 3**(8-i)
		return result

	def addDecimal(self, a, b):
		self.addTernary(self.convertToTernary(a), self.convertToTernary(b))

	def convertToTernary(self, number):
		res = [0,0,0, 0,0,0, 0,0,0]
		if number == 0:
			return res
		while number != 0:
			if number< 0:
				sign = -1
				number = -1* number
			else:
				sign = 1
			top = math.ceil(math.log(number, 3))
			if number > 3.0**top/2.0:
				res[8-top] = sign
				number = (number - 3**top)*sign 
			else:
				res[8-top+1] = sign 
				number = (number - 3**(top-1))*sign
		return res

if __name__ == '__main__':
	myadder = TernaryAdder()
	myadder.addTernary([1,0,-1,1,0,0,-1],\
					   [0,1,0,1,0,0,-1])
	myadder.printResult()
	myadder.addDecimal(-333,733)
	myadder.printResult()

	# print(5, myadder.convertToTernary(5))
	# print(26, myadder.convertToTernary(26))
	# print(0, myadder.convertToTernary(0))
	# print(-9, myadder.convertToTernary(-9))
	# print(676, myadder.convertToTernary(676))
	# print(-28, myadder.convertToTernary(-28))


