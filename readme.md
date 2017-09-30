# @pipeable

@pipeable is a nifty Python package that allows developers to make their own python scripts "pipeable". In essence, @pipeable allows Python scripts to easily accept input from stdin and write to stdout along with a few additional bells and whistles. This allows developers to use their Python scripts in conjunction with the | (pipe) operator from the command line.

__Example__:
```
> echo 'test' | python test.py
```

## Installation

You may install @pipeable with the following.

```
pip install pipeable
```

## Usage

The main component of @pipeable is the pipe decorator. The pipe decorator is used to specify the entrance point into a "pipeable" Python script. A function that is decorated with the pipe decorator should take one argument as input. The value that is read from stdin will be automatically bound to that input.

__Example__:

test.py
```python
from pipeable import pipe

@pipe()
def print_input(inp):
  print(inp)
```

And using the script:

```
> echo 'This is a test.' | python test.py
This is a test.
```

The example above can also be achieved with the following, since @pipeable will write whatever is returned from the decorated function to stdout.

test.py
```python
from pipeable import pipe

@pipe()
def print_input(inp):
  return inp
```

```
> echo 'This is another test.' | python test.py
This is another test.
```
