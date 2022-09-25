import Iterables.Sample_Iterables.sample as i
import unittest

class testsample(unittest.TestCase):
    def test_Iterable(self):
        size=4
        input=['a','a','c','d']
        k=2
        l='0.833'
        result= i.Iterables(size,input,k)
        self.assertEqual(result,l)

if __name__ == '__main__':
    unittest.main()