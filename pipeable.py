import sys

used = False

def _get_input():
    """ Gets the input from stdin if it exists.
        Otherwise, it looks for a command line argument.
        Raises an error if no argument is given. """
    if not sys.stdin.isatty():
        inp = sys.stdin.read()
    else:
        try:
            inp = sys.argv[1]
        except IndexError:
            message = 'No input provided.'
            raise IndexError(message)
    return inp

def __execute(func, transform, inp):
    """ Execute the decorated function. If transform is not None, then transform the input.
        Otherwise, pass in the raw input. """
    out = None
    if transform != None:
        out = func(transform(inp))
    else:
        out = func(inp)
    return out

def pipe(transform=None):
    """ Decorator to read the input from stdin or as a command line argument
        and pass the result to the decorated function. """
    def pipe_in(func):
        global used
        if used:
            raise Exception('Error: cannot decorate multiple functions with @pipe!')

        used = True
        def wrapper_func():
            inp = _get_input()
            out = __execute(func, transform, inp)

            if out != None:
                sys.stdout.write(str(out))

        wrapper_func()
    return pipe_in
