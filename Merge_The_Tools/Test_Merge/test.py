import Merge_The_Tools.Sample_Merge.sample as m
import unittest

class testsample(unittest.TestCase):
    def test_merge(self):
        string='AABCAAADA'
        k=3
        l=['AB','CA','AD']
        result= m.merge_the_tools(string,k)
        self.assertEqual(result,l)

if __name__ == '__main__':
    unittest.main()