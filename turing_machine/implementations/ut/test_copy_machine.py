import unittest
from turing_machine.implementations import CopyMachineFactory


class TestCopyMachine(unittest.TestCase):
    def _get_machine_printable_output(self, *args, **kwargs):
        machine = CopyMachineFactory.create(*args, **kwargs)
        machine.run(verbosity=0)
        return machine.printable_output

    def test_default_parameters(self):
        self.assertEqual(self._get_machine_printable_output(), '')

    def test_empty(self):
        self.assertEqual(self._get_machine_printable_output(''), '')

    def test_simple_string(self):
        self.assertEqual(self._get_machine_printable_output('simple'), 'simple')

    def test_string_with_special_characters(self):
        self.assertEqual(self._get_machine_printable_output('N0T-th@t_$1mpIe'), 'N0T-th@t_$1mpIe')
