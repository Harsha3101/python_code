import Calender.Sample_Calander.sample as c
import unittest

class testsample(unittest.TestCase):
    def test_Calander(self):
        result= c.cal(2015,5,8)
        self.assertEqual(result,'FRIDAY')

if __name__ == '__main__':
    unittest.main()
