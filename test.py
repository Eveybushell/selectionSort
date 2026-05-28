import unittest
import random
from selectionSort import selectionSort

class TestSelectionSort(unittest.TestCase):

    def testRandom(self):
        testArray = []
        for _ in range(5):
            testArray.append(random.randint(1,10))
        self.assertEqual(selectionSort(testArray), sorted(testArray))
    
    def testPreSorted(self):
        self.assertEqual(selectionSort([1,2,3,4,5]), [1,2,3,4,5])
    
    def testReverse(self):
        self.assertEqual(selectionSort([5,4,3,2,1]), [1,2,3,4,5])
    
    def testAllSame(self):
        self.assertEqual(selectionSort([4,4,4,4,4,4,4]), [4,4,4,4,4,4,4])
    
    def testEmpty(self):
        self.assertEqual(selectionSort([]), [])
    
    def testOne(self):
        self.assertEqual(selectionSort([4]), [4])

if __name__=="__main__":
    unittest.main()