"""Basic unit test for lambdata"""

import unittest
import random

from example_module import favorite_animals, colors, add, increment, becca, rand_num

class ExampleTests(unittest.TestCase):
    """Making sure examples work as expected"""

    def test_add(self):
        """Testing that add works as expected"""
        num1 = 0
        num2 = 1
        self.assertEqual(add(num1,num2), 1)
        self.assertEqual(add(num2, num2), 2)

    
    def test_increment(self):
        """Testing the increment function"""
        x0 = 0
        y0 = increment(x0)
        self.assertEqual(y0,1)
        
        x1 = 100
        y1 = increment(x1)
        self.assertEqual(y1,101)

        x2 = -1
        y2 = increment(x2)
        self.assertEqual(y2,0)

    def test_colors(self):
        """Testing the colors function"""
        self.assertIn("Teal", colors)
        self.assertNotIn("yellow", colors)

    def test_favorite_animals(self):
        """Testing the favorite animals function"""
        length_fa = len(favorite_animals)
        self.assertEqual(length_fa, 4)

    def test_becca(self):
        """Testing the becca function"""
        self.assertIn('Becca is crying', becca)

    def test_rand_num(self):
        """Testing the rand_num funciton"""
        y4 = random.randint(0, 100)
        y5 = rand_num(y4)
        self.assertGreater(y5,1000)

    

if __name__ == "__main__":
    unittest.main()




