import unittest
import bs11

class TestAdd(unittest.TestCase):

    def test_add10(self): self.assertEqual(bs11.Calculator.add(5,5), 10)
    def test_add11(self): self.assertEqual(bs11.Calculator.add(20,5), 25)
    def test_add12(self): self.assertEqual(bs11.Calculator.subtract(30,5), 25)
    def test_add13(self): self.assertEqual(bs11.Calculator.subtract(100,5), 95)
    def test_add14(self): self.assertEqual(bs11.Calculator.multiply(5,5), 25)
    def test_add15(self): self.assertEqual(bs11.Calculator.multiply(100,5), 500)
    def test_add16(self): self.assertEqual(bs11.Calculator.divide(10,5), 2)
    def test_add16(self): self.assertEqual(bs11.Calculator.divide(100,5), 20)
    