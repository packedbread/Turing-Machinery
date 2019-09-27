from turing_machine import Tape, Head, Turing


class CopyMachineFactory:
    @staticmethod
    def create(tape=None, head=None):
        tape = tape or Tape()
        if not isinstance(tape, Tape):
            tape = Tape(tape)
        head = head or Head()
        if not isinstance(head, Head):
            head = Head(head)
        alphabet_representation = dict((symbol, index) for index, symbol in enumerate(tape.alphabet))
        states = set()
        for symbol in tape.alphabet:
            if symbol == tape.blank_symbol:
                continue
            states.add(f'move.{alphabet_representation[symbol]}')
            states.add(f'skip_right.{alphabet_representation[symbol]}')
            states.add(f'skip_left.{alphabet_representation[symbol]}')
            states.add(f'return.{alphabet_representation[symbol]}')
        initial_state = 'continue'
        terminal_state = 'terminate'
        states.add(initial_state)
        states.add(terminal_state)

        def tau(state, symbol):
            if state == initial_state:
                if symbol == tape.blank_symbol:
                    return terminal_state, tape.blank_symbol, Head.MoveDirection.right
                return f'move.{symbol}', tape.blank_symbol, Head.MoveDirection.right
            elif state.startswith('move'):
                state_symbol = state[len('move.'):]
                if symbol == tape.blank_symbol:
                    return f'skip_right.{state_symbol}', tape.blank_symbol, Head.MoveDirection.right
                return state, symbol, Head.MoveDirection.right
            elif state.startswith('skip_right'):
                state_symbol = state[len('skip_right.'):]
                if symbol == tape.blank_symbol:
                    return f'skip_left.{state_symbol}', state_symbol, Head.MoveDirection.left
                return state, symbol, Head.MoveDirection.right
            elif state.startswith('skip_left'):
                state_symbol = state[len('skip_left.'):]
                if symbol == tape.blank_symbol:
                    return f'return.{state_symbol}', tape.blank_symbol, Head.MoveDirection.left
                return state, symbol, Head.MoveDirection.left
            elif state.startswith('return'):
                state_symbol = state[len('return.'):]
                if symbol == tape.blank_symbol:
                    return initial_state, state_symbol, Head.MoveDirection.right
                return state, symbol, Head.MoveDirection.left
            return terminal_state, symbol, Head.MoveDirection.stay

        return Turing(
            states=states,
            alphabet=tape.alphabet,
            transition_function=tau,
            initial_state=initial_state,
            final_states=(terminal_state,),
            tape=tape,
            head=head,
        )
