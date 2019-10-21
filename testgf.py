from gf import gf2
import unittest
zero = gf2(0)
one = gf2(1)
class TestGF2(unittest.TestCase):
    def testAddOperation(self):
        self.assertEqual(zero+one,one)
        self.assertEqual(one+zero,one)
        self.assertEqual(zero+zero,zero)
        self.assertEqual(one+one,zero)
    def testSubOperation(self):
        self.assertEqual(one-zero,one)
        self.assertEqual(zero-one,one)
        self.assertEqual(one-one,zero)
        self.assertEqual(zero-zero,zero)
    def testMulOperation(self):
        self.assertEqual(zero*zero,zero)
        self.assertEqual(zero*one,zero)
        self.assertEqual(one*zero,zero)
        self.assertEqual(one*one,one)
    def testDivOperation(self):
        self.assertEqual(zero/one,zero)
        self.assertEqual(one/one,one)


if __name__ == "__main__":
    unittest.main()
    


