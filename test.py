import unittest
import exercise_1_2011

class Mis_test(unittest.TestCase):
    def test_function(self):
        self.assertEqual(2+2,4)
    def test_func_2(self):
        self.assertTrue(True)
    def test_exercise(self):
        print('test de dominio')
        self.assertEqual(-1,exercise_1_2011.exercise_1(2,-1))

if __name__ =='__main__':
    unittest.main()