from gates import *

class GateSum3(GateDiadic):
  """
  Sums three inputs (a, b, carryin), for use in adder
  (+, +, +) => +,0 (3)
  (-, -, -) => -,0 (-3)
  (+, +, -) => 0,+ (1)
  ...The carryout never creates its own carryover because the way the algebra is defined.
  """
  def __init__(self):
    super().__init__()
    self._input3 = ConnectionPoint(ConnectionPoint.READER, self)
    self._overflow = ConnectionPoint(ConnectionPoint.WRITER)

    wires = [Wire() for i in range(6)]
    # a
    self._identity_a = GateIdentity()
    self._identity_a.SetOutputWire(wires[0])
    # b
    self._identity_b = GateIdentity()
    self._identity_b.SetOutputWire(wires[1])
    # carryin
    self._identity_c = GateIdentity()
    self._identity_c.SetOutputWire(wires[2])
    # A = a+b ,  carry = (a+b)carry (wire 4)
    sumAB = GateSum()
    sumAB.SetInputWire1(wires[0])
    sumAB.SetInputWire2(wires[1])
    sumAB.SetOutputWire(wires[3])
    sumAB.SetOverflowWire(wires[4])
    # sum = (a+b)+c
    self._sumAll = GateSum()
    self._sumAll.SetInputWire1(wires[3])
    self._sumAll.SetInputWire2(wires[2])
    self._sumAll.SetOverflowWire(wires[5])
    # carry = wire 4 + new carry (this can not create another carry)
    self._overflow_gate = GateSum()
    self._overflow_gate.SetInputWire1(wires[4])
    self._overflow_gate.SetInputWire2(wires[5])

  def SetInputWire3(self, wire):
    self._identity_c.SetInputWire(wire)
    wire.Connect(self._input3)

  def SetInputWire1(self, wire):
    self._identity_a.SetInputWire(wire)
    wire.Connect(self._input1)

  def SetInputWire2(self, wire):
    self._identity_b.SetInputWire(wire)
    wire.Connect(self._input2)

  def SetOutputWire(self, wire):
    self._sumAll.SetOutputWire(wire)
    wire.Connect(self._output)

  def SetOverflowWire(self, wire):
    self._overflow_gate.SetOutputWire(wire)
    wire.Connect(self._overflow)

  def Update(self):
    pass

  def __str__(self):
    return '%s<I1: %s, I2: %s, I3: %s, Overflow: %s, Out: %s>' % \
        (type(self).__name__, self._input1.State(), self._input2.State(), self._input3.State(),\
         self._overflow.State(), self._output.State())