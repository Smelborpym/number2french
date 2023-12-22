class Converter:
    def __init__(self, numbers, lang='french'):
        self.numbers = numbers
        self.lang = lang

    def convert_to_words(self):
        return [self._convert_number(number) for number in self.numbers]

    def _convert_number(self, number):
        if self.lang == 'french':
            return self._convert_french(number)
        elif self.lang == 'belgian':
            return self._convert_belgian(number)
        else:
            raise ValueError("Unsupported language")

    def _convert_french(self, number):
        # fr conversion logic here
        pass

    def _convert_belgian(self, number):
        # be conversion logic here
        pass


