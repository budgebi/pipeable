import sys

# Used to denote whether the pipe decorator has previously been used.
used = False

class Pipe:

    def __init__(self, transform=None):
        """ Initer will take the transformation to be applied to the string read from stdin. """
        self.transform = transform

    def __call__(self, func):
        """ __call__ is the function which will decorate other functions. """
        self.__verify_single_use()

        def wrapper_func():
            inp = self._get_input()
            out = self.__execute(func, self.transform, inp)

            if out != None:
                sys.stdout.write(str(out))

        wrapper_func()


    ##### Private. Strongly discouraged from external use.
    def __execute(self, func, transform, inp):
        """ Execute the decorated function. If transform is not None, then transform the input.
        Otherwise, pass in the raw input. """
        out = None
        if transform != None:
            out = func(transform(inp))
        else:
            out = func(inp)
        return out

    def __verify_single_use(self):
        """ Ensures that the pipe decorator is only used on a single function. """
        global used
        if used:
            raise Exception('cannot decorate multiple functions with @pipe!')
        used = True

    ##### Discouraged from external use.
    def _get_input(self):
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
