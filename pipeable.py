import sys

registry = []

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
        if len(registry) > 0:
            print('Error: only one function may be marked as a pipeline step.')
            exit()

        registry.append(func)
        def wrapper_func():
            inp = get_input()
            if transform != None:
                func(transform(inp))
            else:
                func(inp)

        wrapper_func()
    return real_pipeable
