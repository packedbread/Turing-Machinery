class Tape:
    def __init__(self, tape='', alphabet=None, blank_symbol=None):
        if tape == '':
            if alphabet is None:
                if blank_symbol is None:
                    blank_symbol = ' '
                    alphabet = ' 0'
                else:
                    alphabet = blank_symbol
            else:
                if blank_symbol is None:
                    blank_symbol = ' '
                alphabet = {blank_symbol} | set(alphabet)
        else:
            if alphabet is None:
                if blank_symbol is None:
                    blank_symbol = ' '
                alphabet = {blank_symbol} | set(tape)
        self.tape_dict = dict((index, symbol) for index, symbol in enumerate(tape) if symbol != blank_symbol)
        self.alphabet = alphabet
        self.blank_symbol = blank_symbol

    @property
    def min_used_index(self):
        return min(self.tape_dict.keys() or [0])

    @property
    def max_used_index(self):
        return max(self.tape_dict.keys() or [-1])

    class Iterator:
        def __init__(self, tape):
            self.tape = tape
            self.index = self.tape.min_used_index
            self.max_index = self.tape.max_used_index

        def __next__(self):
            if self.index <= self.max_index:
                self.index += 1
                return self.tape[self.index - 1]
            raise StopIteration

    def __iter__(self):
        return Tape.Iterator(self)

    def __str__(self):
        min_used_index = self.min_used_index
        max_used_index = self.max_used_index
        tape = ''
        for i in range(min_used_index, max_used_index + 1):
            tape += str(self[i])
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
