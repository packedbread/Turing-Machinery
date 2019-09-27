class Tape:
    def __init__(self, tape='', blank_symbol=' '):
        self.__tape = dict((index, symbol) for index, symbol in enumerate(tape) if symbol != blank_symbol)
        self.blank_symbol = blank_symbol

    @property
    def tape_dict(self):
        return self.__tape

    @tape_dict.setter
    def tape_dict(self, value):
        self.__tape = value

    @property
    def alphabet(self):
        return set(self.tape_dict.values()) | {self.blank_symbol}

    @property
    def min_used_index(self):
        return min(self.tape_dict.keys())

    @property
    def max_used_index(self):
        return max(self.tape_dict.keys())

    def __str__(self):
        min_used_index = self.min_used_index
        max_used_index = self.max_used_index
        tape = ''
        for i in range(min_used_index, max_used_index + 1):
            tape += self[i]
        return tape

    def __repr__(self):
        return f'{self.__class__.__name__}(tape=\'{str(self)}\', blank_symbol={repr(self.blank_symbol)})'

    def __getitem__(self, index):
        if index in self.tape_dict:
            return self.tape_dict[index]
        return self.blank_symbol

    def __setitem__(self, key, value):
        if value == self.blank_symbol and key in self.tape_dict:
            del self.tape_dict[key]
        else:
            self.tape_dict[key] = value
