from ternaryMux import *
import unittest

class TestMux(unittest.TestCase):
  def setupMux(self, mux_type):
    writer_1 = ConnectionPoint(ConnectionPoint.WRITER)
    wire_1 = Wire()
    writer_2 = ConnectionPoint(ConnectionPoint.WRITER)
    wire_2 = Wire()
    writer_3 = ConnectionPoint(ConnectionPoint.WRITER)
    wire_3 = Wire()
    writer_4 = ConnectionPoint(ConnectionPoint.WRITER)
    wire_4 = Wire()
    mux = mux_type()
    wire_5 = Wire()
    reader = ConnectionPoint(ConnectionPoint.READER)

    wire_1.Connect(writer_1)
    wire_2.Connect(writer_2)
    wire_3.Connect(writer_3)
    wire_4.Connect(writer_4)

    mux.SetInputWireA(wire_1)
    mux.SetInputWireB(wire_2)
    mux.SetInputWireC(wire_3)
    mux.SetInputWireS(wire_4)

    wire_5.Connect(reader)
    mux.SetOutputWire(wire_5)

    return (writer_1, writer_2, writer_3, writer_4, reader, mux)

  def genericMuxTest(self, mux_type, ins_outs):
    (a, b, c, s, o, g) = self.setupMux(mux_type)
    for (ina, inb, inc, ins) in ins_outs:
      expected = ins_outs[(ina, inb, inc, ins)]
      a.SetStateWrite(ina)
      b.SetStateWrite(inb)
      c.SetStateWrite(inc)
      s.SetStateWrite(ins)
      result = o.GetState()
      self.assertEqual(expected, result, '%s expected output [%s]' % (g, STATE_NAME[result]))

  def testMux3to1(self):
    self.genericMuxTest(Mux3to1, {
      (PLUS, NEUTRAL, NEUTRAL, MINUS): (PLUS),
      (PLUS, PLUS, MINUS, PLUS): (MINUS),
      (PLUS, PLUS, MINUS, NEUTRAL): (PLUS),
      (NEUTRAL, NEUTRAL, MINUS, PLUS): (MINUS),
      (NEUTRAL, NEUTRAL, PLUS, NEUTRAL): (NEUTRAL)
      })

if __name__ == '__main__':
  unittest.main()
