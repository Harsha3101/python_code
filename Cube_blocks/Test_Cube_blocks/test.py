import Cube_blocks.Sample_Cube_blocks.sample as c
import unittest

class testsample(unittest.TestCase):
    def test_cube_blocks_1(self):
        n=6
        l=[4,3,2,1,3,4]
        result= c.Cube_Block(n,l)
        self.assertEqual(result,'Yes')
    def test_cube_blocks_2(self):
        n=3
        l=[1,3,2]
        result= c.Cube_Block(n,l)
        self.assertEqual(result,'No')

if __name__ == '__main__':
    unittest.main()