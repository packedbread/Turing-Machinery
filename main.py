from turing_machine import *


def main():
    machine = implementations.CopyMachineFactory.create('this-is-a-copy')
    machine.run(verbosity=2)


if __name__ == '__main__':
    main()
