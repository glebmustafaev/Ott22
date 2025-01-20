import runner
import unittest

class TournamentTest(unittest.TestCase):
    def setUpClass(self):
        self.all_results = None

    def setUp(self):
        r_1 = runner.Runner('Усэйн',10)
        r_2 = runner.Runner('Андрей',9)
        r_3 = runner.Runner('Ник',3)

    def tearDownClass(self):
        print(self.all_results, end='\n')
