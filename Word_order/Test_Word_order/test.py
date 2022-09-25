import Word_order.Sample_Word_order.Sample as w
import unittest

class testsample(unittest.TestCase):
    def test_linear(self):
        k =4
        j = ['bcdef','abcdefg','bcde','bcdef']
        g=[2,1,1]
        result= w.Word_order(k,j)
        self.assertEqual(result,g)

if __name__ == '__main__':
    unittest.main()
