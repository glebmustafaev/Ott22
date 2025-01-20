import runner
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner.Runner('Усейн', 10)
        self.runner2 = runner.Runner('Андрей', 9)
        self.runner3 = runner.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def test_1(self):
        obj_1 = runner.Tournament(90, self.runner1, self.runner3)
        result = obj_1.start()
        self.assertTrue(list(result.values())[-1] == self.runner3)
        self.all_results[f'Результат {self.runner1} и {self.runner3}'] = result

    def test_2(self):
        obj_2 = runner.Tournament(90, self.runner2, self.runner3)
        result = obj_2.start()
        self.assertTrue(list(result.values())[-1] == self.runner3)
        self.all_results[f'Результат {self.runner2} и {self.runner3}'] = result

    def test_3(self):
        obj_3 = runner.Tournament(90, self.runner1,self.runner2, self.runner3)
        result = obj_3.start()
        self.assertTrue(list(result.values())[-1] == self.runner3)
        self.all_results[f'Результат {self.runner1} и {self.runner1} и {self.runner3}'] = result
