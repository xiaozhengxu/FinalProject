from gates import *

class TernaryAdder:
	def __init__(self):
		self.triA = []
		self.triB = []
		self.operandA = [Wire() for i in range(9)]
		self.operandB = [Wire() for i in range(9)]
		self.decA = 0
		self.decB = 0
		self.overflows = [Wire() for i in range(9)]
		self.result = [Wire() for i in range(9)]
		self.resultRead = [ConnectionPoint(ConnectionPoint.READER) for i in range(9)]
		self.gates = []
		self.output = []
		self.decRes = 0

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
			aDigit= ConnectionPoint(ConnectionPoint.WRITER, state=Adigits[i])
			self.operandA[i].Connect(aDigit)
			bDigit= ConnectionPoint(ConnectionPoint.WRITER, state=Bdigits[i])
			self.operandB[i].Connect(bDigit)
			self.result[i].Connect(self.resultRead[i])

		zero = ConnectionPoint(ConnectionPoint.WRITER, state = 0)
		zeroWire = Wire()
		zeroWire.Connect(zero)

		#Doing the addition using 9 sum3 gates
		for k in range(9):
			curGate = GateSum3()
			curGate.SetInputWire1(self.operandA[8-k])
			curGate.SetInputWire2(self.operandB[8-k])
			if k == 0:
				curGate.SetInputWire3(zeroWire)
			else:
				curGate.SetInputWire3(self.overflows[k-1])
			curGate.SetOutputWire(self.result[8-k])

			print (curGate.ReadOutput())
			
			curGate.SetOverflowWire(self.overflows[k])
			self.gates.append(curGate)
		for j in range(9):
			self.result[j].Update() #Update the wire, writing to the connection point
		self.output = [cp.GetState() for cp in self.resultRead]
		self.decRes = self.convertToDecimal(self.output)

	def printResult(self):
		print (self.triA)
		print (self.triB)
		print (self.output)
		print (self.decA)
		print (self.decB)
		print (self.decRes)

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
		addTernary(convertToTernary(a), convertToTernary(b))

	def convertToTernary(self):
		pass

if __name__ == '__main__':
	myadder = TernaryAdder()
	myadder.addTernary([1,0,0,-1],[1,0,0,-1])
	myadder.printResult()


