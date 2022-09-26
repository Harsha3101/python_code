import Floor_Ceil_Rint.Floor_Sample.sample as f
import unittest

class testsample(unittest.TestCase):
    def test_floor(self):
        result= f.floors([1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9])
        self.assertEqual(result,[ 1.,2.,3.,4.,5.,6.,7.,8.,9.])
    def test_ceil(self):
        result= f.floors([1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9])
        self.assertEqual(result,[2.,3.,4.,5.,6.,7.,8.,9.,10.])
    def test_rint(self):
        result= f.floors([1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9])
        self.assertEqual(result,[1.,2.,3.,4.,6.,7.,8.,9.,10.])
if __name__ == '__main__':
    unittest.main()
