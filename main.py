from turing_machine import *


def main():
    machine = implementations.BusyBeaverFactory.create(state_count=4)
    machine.run(verbosity=2)
    print(f'Sigma function value: {sum(machine.tape)}')


if __name__ == '__main__':
    main()
