# Turing machinery
## Description
This is simple turing machine package. There are some machine implementations:

- copy machine - that copies given input in following way: 'input-text' becomes 'input-text input-text'.
- busy beaver - currently supported sizes are up to 5 non-terminal states on binary alphabet,
5 state already takes quite a while to finish (therefore there is no test for it),
but current 6 state best contender will take more time to finish, than the current age of the universe.

This list will extend upon implementation of additional procedures and functions.

Feel free to contribute and add your own implementation.

### Functions wishlist
You can submit functions, procedures or algorithms, which you would like to see implemented. The current list is:

- RAM
- Tape marks reader and writer
- Other turing machine executor, basically simple procedure call

## Tests
You can run implementation tests with the following command:
```bash
python -m unittest
```

Additional tests are always welcome.

## Licence
This project is distributed under MIT License.
