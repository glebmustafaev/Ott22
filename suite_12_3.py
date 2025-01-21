import unittest
import test_runner
import Tournament
runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(Tournament.TournamentTest))

runners = unittest.TextTestRunner(verbosity=2)
runners.run(runST)
