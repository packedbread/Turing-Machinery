from turing_machine import Tape, Turing, Head


class BusyBeaverFactory:
    """
    Busy Beaver game on turing machine simulations, currently using classic 2 symbol alphabet.

    Note, that busy beaver should produce max number of `1` on the tape, not in the output.

    More info at: https://en.wikipedia.org/wiki/Busy_Beaver_game
    """
    @staticmethod
    def _one_state():
        states = (0, 1)
        alphabet = (0, 1)
        blank_symbol = 0

        def tau(state, symbol):
            if state == states[0]:
                return states[1], alphabet[1], Head.MoveDirection.right
            return state, symbol, Head.MoveDirection.stay

        return Turing(
            states=states,
            transition_function=tau,
            initial_state=states[0],
            final_states={states[-1]},
            tape=Tape(tape='', alphabet=alphabet, blank_symbol=blank_symbol)
        )

    @staticmethod
    def _two_state():
        states = (0, 1, 2)
        alphabet = (0, 1)
        blank_symbol = 0

        def tau(state, symbol):
            if state == states[0]:
                if symbol == alphabet[0]:
                    return states[1], alphabet[1], Head.MoveDirection.right
                else:
                    return states[1], alphabet[1], Head.MoveDirection.left
            elif state == states[1]:
                if symbol == alphabet[0]:
                    return states[0], alphabet[1], Head.MoveDirection.left
                else:
                    return states[2], alphabet[1], Head.MoveDirection.left
            return state, symbol, Head.MoveDirection.stay

        return Turing(
            states=states,
            transition_function=tau,
            initial_state=states[0],
            final_states={states[-1]},
            tape=Tape(tape='', alphabet=alphabet, blank_symbol=blank_symbol)
        )

    @staticmethod
    def _three_state():
        states = (0, 1, 2, 3)
        alphabet = (0, 1)
        blank_symbol = 0

        def tau(state, symbol):
            if state == states[0]:
                if symbol == alphabet[0]:
                    return states[1], alphabet[1], Head.MoveDirection.right
                else:
                    return states[3], alphabet[1], Head.MoveDirection.right
            elif state == states[1]:
                if symbol == alphabet[0]:
                    return states[2], alphabet[0], Head.MoveDirection.right
                else:
                    return states[1], alphabet[1], Head.MoveDirection.right
            elif state == states[2]:
                if symbol == alphabet[0]:
                    return states[2], alphabet[1], Head.MoveDirection.left
                else:
                    return states[0], alphabet[1], Head.MoveDirection.left
            return state, symbol, Head.MoveDirection.stay

        return Turing(
            states=states,
            transition_function=tau,
            initial_state=states[0],
            final_states={states[-1]},
            tape=Tape(tape='', alphabet=alphabet, blank_symbol=blank_symbol)
        )

    @staticmethod
    def _four_state():
        states = (0, 1, 2, 3, 4)
        alphabet = (0, 1)
        blank_symbol = 0

        def tau(state, symbol):
            if state == states[0]:
                if symbol == alphabet[0]:
                    return states[1], alphabet[1], Head.MoveDirection.right
                else:
                    return states[1], alphabet[1], Head.MoveDirection.left
            elif state == states[1]:
                if symbol == alphabet[0]:
                    return states[0], alphabet[1], Head.MoveDirection.left
                else:
                    return states[2], alphabet[0], Head.MoveDirection.left
            elif state == states[2]:
                if symbol == alphabet[0]:
                    return states[4], alphabet[1], Head.MoveDirection.right
                else:
                    return states[3], alphabet[1], Head.MoveDirection.left
            elif state == states[3]:
                if symbol == alphabet[0]:
                    return states[3], alphabet[1], Head.MoveDirection.right
                else:
                    return states[0], alphabet[0], Head.MoveDirection.right
            return state, symbol, Head.MoveDirection.stay

        return Turing(
            states=states,
            transition_function=tau,
            initial_state=states[0],
            final_states={states[-1]},
            tape=Tape(tape='', alphabet=alphabet, blank_symbol=blank_symbol)
        )

    @staticmethod
    def _five_state():
        """
        Note, this is a possible busy beaver, it has not yet been rigorously proven that this TM is a busy beaver.
        """
        states = (0, 1, 2, 3, 4, 5)
        alphabet = (0, 1)
        blank_symbol = 0

        def tau(state, symbol):
            if state == states[0]:
                if symbol == alphabet[0]:
                    return states[1], alphabet[1], Head.MoveDirection.right
                else:
                    return states[2], alphabet[1], Head.MoveDirection.left
            elif state == states[1]:
                if symbol == alphabet[0]:
                    return states[2], alphabet[1], Head.MoveDirection.right
                else:
                    return states[1], alphabet[1], Head.MoveDirection.right
            elif state == states[2]:
                if symbol == alphabet[0]:
                    return states[3], alphabet[1], Head.MoveDirection.right
                else:
                    return states[4], alphabet[0], Head.MoveDirection.left
            elif state == states[3]:
                if symbol == alphabet[0]:
                    return states[0], alphabet[1], Head.MoveDirection.left
                else:
                    return states[3], alphabet[1], Head.MoveDirection.left
            elif state == states[4]:
                if symbol == alphabet[0]:
                    return states[5], alphabet[1], Head.MoveDirection.right
                else:
                    return states[0], alphabet[0], Head.MoveDirection.left
            return state, symbol, Head.MoveDirection.stay

        return Turing(
            states=states,
            transition_function=tau,
            initial_state=states[0],
            final_states={states[-1]},
            tape=Tape(tape='', alphabet=alphabet, blank_symbol=blank_symbol)
        )

    @staticmethod
    def create(state_count=2):
        if state_count == 1:
            return BusyBeaverFactory._one_state()
        elif state_count == 2:
            return BusyBeaverFactory._two_state()
        elif state_count == 3:
            return BusyBeaverFactory._three_state()
        elif state_count == 4:
            return BusyBeaverFactory._four_state()
        elif state_count == 5:
            return BusyBeaverFactory._five_state()
        raise NotImplementedError
