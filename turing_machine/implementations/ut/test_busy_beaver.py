import unittest
from turing_machine.implementations import BusyBeaverFactory


class TestBusyBeaver(unittest.TestCase):
    def _get_sigma_function_value(self, *args, **kwargs):
        machine = BusyBeaverFactory.create(*args, **kwargs)
        machine.run(verbosity=0)
        return sum(machine.tape)

    def test_one_state(self):
        self.assertEqual(self._get_sigma_function_value(state_count=1), 1)

    def test_two_state(self):
        self.assertEqual(self._get_sigma_function_value(state_count=2), 4)

    def test_three_state(self):
        self.assertEqual(self._get_sigma_function_value(state_count=3), 6)

    def test_four_state(self):
        self.assertEqual(self._get_sigma_function_value(state_count=4), 13)
