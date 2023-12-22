import unittest
from src.converter import Converter

class TestConverter(unittest.TestCase):

    def test_single_digit_numbers(self):
        converter = Converter([1, 2, 3], 'french')
        self.assertEqual(converter.convert_to_words(), ["un", "deux", "trois"])

    def test_tens_french(self):
        converter = Converter([10, 20, 30], 'french')
        self.assertEqual(converter.convert_to_words(), ["dix", "vingt", "trente"])

    def test_special_cases_french(self):
        converter = Converter([71, 80, 91], 'french')
        self.assertEqual(converter.convert_to_words(), ["soixante-et-onze", "quatre-vingts", "quatre-vingt-et-onze"])

    def test_tens_belgian(self):
        converter = Converter([70, 80, 90], 'belgian')
        self.assertEqual(converter.convert_to_words(), ["septante", "huitante", "nonante"])

    def test_larger_numbers(self):
        converter = Converter([100, 101, 111, 120, 999], 'french')
        expected = ["cent", "cent-un", "cent-onze", "cent-vingt", "neuf-cent-quatre-vingt-dix-neuf"]
        self.assertEqual(converter.convert_to_words(), expected)

    def test_thousands(self):
        converter = Converter([1000, 2001, 3010, 12345], 'french')
        expected = ["mille", "deux-mille-un", "trois-mille-dix", "douze-mille-trois-cent-quarante-cinq"]
        self.assertEqual(converter.convert_to_words(), expected)

    def test_edge_cases(self):
        converter = Converter([0], 'french')
        self.assertEqual(converter.convert_to_words(), ["zéro"])

        converter = Converter([999999], 'french')
        self.assertEqual(converter.convert_to_words(), ["neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf"])

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            converter = Converter([-1], 'french')
            converter.convert_to_words()
    
    def test_out_of_range_numbers(self):
        with self.assertRaises(ValueError):
            converter = Converter([1000000], 'french')
            converter.convert_to_words()

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            converter = Converter(["twenty"], 'french')
            converter.convert_to_words()

    def test_french_70s_and_90s(self):
        converter = Converter([72, 73, 74, 75, 76, 77, 78, 79, 92, 93, 94, 95, 96, 97, 98, 99], 'french')
        expected = ["soixante-douze", "soixante-treize", "soixante-quatorze", "soixante-quinze", "soixante-seize", 
                    "soixante-dix-sept", "soixante-dix-huit", "soixante-dix-neuf", "quatre-vingt-douze", 
                    "quatre-vingt-treize", "quatre-vingt-quatorze", "quatre-vingt-quinze", "quatre-vingt-seize", 
                    "quatre-vingt-dix-sept", "quatre-vingt-dix-huit", "quatre-vingt-dix-neuf"]
        self.assertEqual(converter.convert_to_words(), expected)

    def test_french_80s(self):
        converter = Converter([81, 82, 83, 84, 85, 86, 87, 88, 89], 'french')
        expected = ["quatre-vingt-et-un", "quatre-vingt-deux", "quatre-vingt-trois", "quatre-vingt-quatre", 
                    "quatre-vingt-cinq", "quatre-vingt-six", "quatre-vingt-sept", "quatre-vingt-huit", 
                    "quatre-vingt-neuf"]
        self.assertEqual(converter.convert_to_words(), expected)

    def test_belgian_specific_numbers(self):
        converter = Converter([70, 71, 80, 81, 90, 91], 'belgian')
        expected = ["septante", "septante-et-un", "huitante", "huitante-et-un", "nonante", "nonante-et-un"]
        self.assertEqual(converter.convert_to_words(), expected)

    def test_belgian_larger_numbers(self):
        converter = Converter([100, 200, 500, 999], 'belgian')
        expected = ["cent", "deux-cents", "cinq-cents", "neuf-cent-nonante-neuf"]
        self.assertEqual(converter.convert_to_words(), expected)

    def test_belgian_thousands(self):
        converter = Converter([1000, 2001, 3010, 12345], 'belgian')
        expected = ["mille", "deux-mille-un", "trois-mille-dix", "douze-mille-trois-cent-quarante-cinq"]
        self.assertEqual(converter.convert_to_words(), expected)


if __name__ == '__main__':
    unittest.main()
