#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4

    listing = dir(hidden_4)
    for name in listing:
        if not name.startswith('__'):
            print('{:s}'.format(name))
