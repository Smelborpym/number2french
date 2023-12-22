class Converter:
    def __init__(self, numbers, lang='french'):
        self.numbers = numbers
        self.lang = lang
        self.units = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", 
                      "onze", "douze", "treize", "quatorze", "quinze", "seize"]
        self.tens = ["dix", "vingt", "trente", "quarante", "cinquante", "soixante"]
        if self.lang == 'belgian':
            self.tens.extend(["septante", "huitante", "nonante"])
        else:
            self.tens.extend(["soixante", "quatre-vingt", "quatre-vingt"])

    def convert_to_words(self):
        return [self._convert_number(number) for number in self.numbers]

    def _convert_number(self, number):
        if number < 17:
            return self.units[number]
        elif number < 100:
            return self._convert_tens(number)
        else:
            return self._convert_larger_numbers(number)

    def _convert_tens(self, number):
        if number < 20:
            return "dix-" + self.units[number - 10]
        tens_index = number // 10
        remainder = number % 10
        tens_word = self.tens[tens_index - 1]

        # french numbers 70-79 and 90-99
        if self.lang == 'french':
            if 70 <= number < 80:
                tens_word = "soixante"
                remainder = number - 60
            elif 90 <= number < 100:
                tens_word = "quatre-vingt"
                remainder = number - 80

        # handling french 71 and 91
        if self.lang == 'french' and number in [71, 91]:
            return tens_word + "-et-onze"

        if remainder == 0:
            return tens_word + ("s" if number == 80 and self.lang == 'french' else "")
        
        elif remainder == 1:
            if self.lang == 'french' and number != 71:
                return tens_word + "-et-un"
            elif self.lang == 'belgian':
                return tens_word + "-et-un"
            else:
                return tens_word + "-un"
        else:
            return tens_word + "-" + self._convert_number(remainder)

    def _convert_larger_numbers(self, number):
        if number == 100:
            return "cent"
        elif number < 1000:
            hundreds = number // 100
            remainder = number % 100
            hundreds_word = ("cent" if hundreds == 1 else self._convert_number(hundreds) + "-cent") + ("s" if remainder == 0 and hundreds > 1 else "")

            # rule for 11 to 19, except when it is exactly 11 after hundreds
            if 12 <= remainder <= 19:
                return hundreds_word + "-et-" + self._convert_number(remainder)
            else:
                return hundreds_word + ("" if remainder == 0 else "-" + self._convert_number(remainder))
        else:
            thousands = number // 1000
            remainder = number % 1000
            # making "mille" plural for whole thousands greater than 1000
            thousands_word = ("mille" if thousands == 1 else self._convert_number(thousands) + "-mille") + ("s" if remainder == 0 and thousands > 1 else "")
            return thousands_word + ("" if remainder == 0 else "-" + self._convert_number(remainder))


