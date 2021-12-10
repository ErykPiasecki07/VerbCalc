"""
Tests translator module.
"""
import unittest
import verbcalc


class TestTranslator(unittest.TestCase):
    """
    Tests how translator works.
    """

    def setUp(self):
        self._custom_symbols = verbcalc.Symbols()
        self._custom_symbols.additions = ['foo']
        self._custom_symbols.subtractions = ['bar']
        self._custom_symbols.multiplications = ['boo']
        self._custom_symbols.divisions = ['far']
        self.expected = ['2 + 2', '2 - 2', '2 * 2', '2 / 2', '2 ** 2',
                         'abs 2', '2 % 2']

    def test_translation(self):
        values = [verbcalc.translate('2 plus 2'),
                  verbcalc.translate('2 minus 2'),
                  verbcalc.translate('2 times 2'),
                  verbcalc.translate('2 divided by 2'),
                  verbcalc.translate('2 to the power of 2'),
                  verbcalc.translate('absolute of 2'),
                  verbcalc.translate('2 mod 2')]
        self.assertListEqual(self.expected, values)


if __name__ == '__main__':
    unittest.main()
