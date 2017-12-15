from gates import *

class Mux3to1:
	def __init__(self):
		self._inputa = ConnectionPoint(ConnectionPoint.READER, self)
    	self._inputb = ConnectionPoint(ConnectionPoint.READER, self)
    	self._inputc = ConnectionPoint(ConnectionPoint.READER, self)
    	self._inputs = ConnectionPoint(ConnectionPoint.READER, self)
    	self._output = ConnectionPoint(ConnectionPoint.WRITER, self)
    	self._delay = 0	

    	wires = [Wire() for i in range(12)]
	    # a
	    self._identity_a = GateIdentity()
	    self._identity_a.SetOutputWire(wires[0])
	    # b
	    self._identity_b = GateIdentity()
	    self._identity_b.SetOutputWire(wires[1])
	    # c
	    self._identity_c = GateIdentity()
	    self._identity_c.SetOutputWire(wires[2])
	    # select
	    self._identity_s = GateIdentity()
	    self._identity_s.SetOutputWire(wires[3])

	    sIsLow = GateIsLow()
	    sIsLow.SetInputWire(wires[3])
	    sIsLow.SetOutputWire(wires[4])
	    sIsZero = GateIsNeutral()
	    sIsZero.SetInputWire(wires[3])
	    sIsZero.SetOutputWire(wires[5])
	    sIsHigh = GateIsHigh()
	    sIsHigh.SetInputWire(wires[3])
	    sIsHigh.SetOutputWire(wires[6])
	    #A
	    aAnd = GateAnd()
	    aAnd.SetInputWire1(wires[0])
	    aAnd.SetInputWire2(wires[4])
	    aAnd.SetOutputWire(wires[7])
	    #B
	    bAnd = GateAnd()
	    bAnd.SetInputWire1(wires[1])
	    bAnd.SetInputWire2(wires[5])
	    bAnd.SetOutputWire(wires[8])
	    #C
	    cAnd = GateAnd()
	    cAnd.SetInputWire1(wires[2])
	    cAnd.SetInputWire2(wires[6])
	    cAnd.SetOutputWire(wires[9])

	    # A v B
	    or1 = GateOr()
	    or1.SetInputWire1(wires[7])
	    or1.SetInputWire2(wires[8])
	    or1.SetOutputWire(wires[10])

	    # (A v B) v C
	    self._output_gate = GateOr()
	    self._output_gate.SetInputWire1(wires[9])
	    self._output_gate.SetInputWire2(wires[10])

	def SetInputWireA(self, wire):
	    self._identity_a.SetInputWire(wire)

	def SetInputWireB(self, wire):
	    self._identity_b.SetInputWire(wire)

	def SetInputWireC(self, wire):
	    self._identity_c.SetInputWire(wire)

	def SetInputWireS(self, wire):
	    self._identity_s.SetInputWire(wire)

	def SetOutputWire(self, wire):
	    self._output_gate.SetOutputWire(wire)

	def Update(self):
	    pass
