import unittest
import packer.measurer as m
import packer.rectangle as r


class MeasurerTest(unittest.TestCase):

    # Returns True or False.
    def test_numberFitWCustom(self):
        rContainer = r.Rectangle(width=10, height=10)
        rItem = r.Rectangle(width=2, height=2)
        measurer = m.Measurer(None,None,1)
        assert measurer.numberFitWCustom(rContainer,rItem,1).count == 3
    def test_numberFitHCustom(self):
        rContainer = r.Rectangle(width=30, height=30)
        rItem = r.Rectangle(width=3, height=3)
        measurer = m.Measurer(None,None,2)
        assert measurer.numberFitHCustom(rContainer,rItem,1).count == 7
    # Returns True or False.
    def test_measure(self):
        rContainer = r.Rectangle(width=10, height=10)
        rItem = r.Rectangle(width=1, height=1)
        measurer = m.Measurer(rContainer,rItem,1)
        assert measurer.Measure() == 16


if __name__ == "__main__":
    unittest.main()

