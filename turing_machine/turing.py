import string

from .tape import Tape
from .head import Head


class Turing:
    def __init__(
            self,
            states,
            alphabet,
            transition_function,
            initial_state,
            final_states,
            tape=Tape(),
            head=Head(),
    ):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transition_function = transition_function
        self.initial_state = initial_state
        self.final_states = set(final_states)
        self.initial_tape = tape
        self.initial_head = head

        self.__state = initial_state
        self.__tape = tape
        self.__head = head

    @property
    def tape(self):
        return self.__tape

    @tape.setter
    def tape(self, value):
        self.__tape = value

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, value):
        self.__head = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @property
    def has_terminated(self):
        return self.state in self.final_states

    @property
    def output(self):
        output = []
        for index in range(self.head.position, self.tape.max_used_index + 1):
            if self.tape[index] == self.tape.blank_symbol:
                break
            output.append(self.tape[index])
        return tuple(output)

    @property
    def printable_output(self):
        if all(symbol in string.printable for symbol in self.alphabet):
            return ''.join(self.output)
        return self.output

    def step(self):
        next_state, symbol_to_write, move_direction = self.transition_function(
            self.state,
            self.tape[self.head.position],
        )
        transition = (self.state, self.tape[self.head.position], next_state, symbol_to_write, move_direction)
        self.state = next_state
        self.tape[self.head.position] = symbol_to_write
        self.head.position += move_direction.value
        return transition

    def reset(self):
        self.state = self.initial_state
        self.tape = self.initial_tape
        self.head = self.initial_head

    def run(self, verbosity=2):
        transitions = []
        machine_states = [(self.state, self.head.position)]

        def print_current_state():
            state, position = machine_states[-1]
            print(f'At step {step_index}, machine was in state {repr(state)} in position {position}.')

        def print_terminated_state():
            state, position = machine_states[-1]
            print(f'Machine terminated in state {repr(state)} in position {position} totaling {step_index} steps.')

        def print_output():
            print(f'Machine output: {self.printable_output}')

        step_index = 0
        while not self.has_terminated:
            if verbosity > 1:
                print_current_state()
            step_index += 1
            transition = self.step()
            transitions.append(transition)
            machine_states.append((self.state, self.head.position))
        if verbosity > 1:
            print_terminated_state()
        if verbosity > 0:
            print_output()
        return machine_states, transitions

    def __repr__(self):
        return (
            f'{self.__class__.__name__}(states={repr(self.states)}, alphabet={repr(self.alphabet)}, '
            f'transition_function={repr(self.transition_function)}), initial_state={repr(self.initial_state)}, '
            f'final_states={repr(self.final_states)}, tape={repr(self.tape)}, head={repr(self.head)})'
        )
