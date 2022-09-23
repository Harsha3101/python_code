import Mean_mid_var.Sample_mean.sample as m
import unittest

class testsample(unittest.TestCase):
    def test_std(self):
        k=[[1,2],[3,4]]
        result = m.mat_std(k)
        self.assertEqual(result,1.11803398875)
    def test_mean(self):
        k=[[1,2],[3,4]]
        result = m.mat_mean(k)
        self.assertEqual(result,2.5)
    def test_var(self):
        k=[[1,2],[3,4]]
        result = m.mat_var(k)
        self.assertEqual(result,1.25)

if __name__ == '__main__':
    unittest.main()