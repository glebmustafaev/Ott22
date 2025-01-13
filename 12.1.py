import runner
import unittest
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        my_walk = runner.Runner('1')
        for i in range(10):
            my_walk.walk()
        self.assertEqual(my_walk.distance,50)
    def test_run(self):
        my_run = runner.Runner('2')
        for j in range(10):
            my_run.run()
        self.assertEqual(my_run.distance,100)
    def test_challenge(self):
        my_walk_ = runner.Runner('3')
        my_run_ = runner.Runner('4')
        for k in range(10):
            my_walk_.walk()
            my_run_.run()
        self.assertNotEqual(my_run_.distance,my_walk_.distance)
