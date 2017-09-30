import sys

used = False

def __get_input():
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

def pipe(transform=None):
    """ Decorator to read the input from stdin or as a command line argument
        and pass the result to the decorated function. """
    def pipe_in(func):
        global used
        if used:
            raise Exception('Error: cannot decorate multiple functions with @pipe!')

        used = True
        def wrapper_func():
            inp = __get_input()
            if transform != None:
                func(transform(inp))
            else:
                func(inp)

        wrapper_func()
    return pipe_in
