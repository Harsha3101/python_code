import Second_larg.Sample_second_larg.sample as s
import unittest

class testsample(unittest.TestCase):
    def test_sec_max(self):
        k=[2,3,6,6,5]
        result= s.sec_max(k)
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()