import Linearalgebra.Sample_Linear.sample as l
import unittest

class testsample(unittest.TestCase):
    def test_linear(self):
        k = [[1.1,1.1],[1.1,1.1]]
        result= l.linear(k)
        self.assertEqual(result,0.0)

if __name__ == '__main__':
    unittest.main()
