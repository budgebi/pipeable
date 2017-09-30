# @pipeable

@pipeable is a nifty Python package that allows users to make their own python scripts "pipeable". In essence, @pipeable allows Python scripts to easily accept input from stdin and write to stdout along with a few additional bells and whistles. This allows users to use their Python scripts in conjunction with the | (pipe) operator from the command line.

Example:
```
echo 'test' | python test.py
```

## Usage

The main component of @pipeable is the pipe decorator.
