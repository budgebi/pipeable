import sys

used = False

def get_input():
    if not sys.stdin.isatty():
        inp = sys.stdin.read()
    else:
        try:
            inp = sys.argv[1]
        except IndexError:
            message = 'No input provided.'
            raise IndexError(message)
    return inp

def pipeable(transform=None):
    def real_pipeable(func):
        global used
        if used:
            raise Exception('Error: cannot decorate multiple functions with @pipeable!')

        used = True
        def wrapper_func():
            inp = get_input()
            if transform != None:
                func(transform(inp))
            else:
                func(inp)

        wrapper_func()
    return real_pipeable
