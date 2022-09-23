import disjoin_sets.Sample_disjoin_sets.sample as d
import unittest

class testsample(unittest.TestCase):
    def test_disjoin(self):
        k = []
        result= d.disj([1,5,3],[3,1],[5,7])
        self.assertEqual(result,1)

if __name__ == '__main__':
    unittest.main()