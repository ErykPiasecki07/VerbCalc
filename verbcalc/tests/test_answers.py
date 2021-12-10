"""
    Tests how custom answers work.
"""
import unittest
import verbcalc


class TestCustomAnswers(unittest.TestCase):
    """
    Tests how custom answers work.
    """
    def setUp(self):
        self._expected_default = ['It is', 'The answer is', 'The result is',
                                  'The total is', 'Altogether you get']
        self._expected_custom = ['Foo', 'Bar']

    def test_random_phrase(self):
        result = verbcalc.calculate('What is 2 plus 2')
        check = [i for i in self._expected_default if i in result]
        self.assertTrue(check)

    def test_custom_random_phrase(self):
        result = verbcalc.calculate(
            'What is 2 plus 2', path_to_answers='fixtures/custom_answers.json')
        check = [i for i in self._expected_custom if i in result]
        self.assertTrue(check)


if __name__ == '__main__':
    unittest.main()
