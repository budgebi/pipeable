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

The main component of @pipeable is the Pipe decorator. The Pipe decorator is used to specify the entrance point into a "pipeable" Python script. A function that is decorated with the Pipe decorator should take one argument as input. The value that is read from stdin will be automatically bound to that input.

__Example__:

test.py
```python
from pipeable import Pipe

@Pipe()
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
from pipeable import Pipe

@Pipe()
def print_input(inp):
  return inp
```

```
> echo 'This is another test.' | python test.py
This is another test.
```

__transform__

You may have noticed that to use the Pipe decorator we do this `@Pipe()` instead of this `@Pipe`. This is because you may optionally pass in a function as an argument to Pipe which "transforms" the string read from stdin in some way. Let's look at another simple example to demonstrate the point.

add_4.py
```python
from pipeable import Pipe

@Pipe(int)
def add_4(inp):
  return inp + 4
```

```
> echo 3 | python test.py
7
```

Since we passed the int function in as a transform to our Pipe decorator, the string read from stdin will be converted into an int before it is passed into the add_4 function which was decorated. Since inp is an int, we can add 4 to it without issue.

__A more advanced example:__

Suppose we have the following Python code, which can write JSON to a Mongo Database.

to_db.py
```python
from pipeable import Pipe
from pymongo import MongoClient
import json

@Pipe(json.loads)
def write_json_to_db(j):
    client = MongoClient('localhost', 27017)
    db = client.sandbox
    collection = db.test_collection
    if type(j) == dict:
        print(collection.insert_one(j).inserted_id)
    elif type(j) == list:
        print(collection.insert_many(j).inserted_ids)
    print(j)
```

Since we decorated the write_json_to_db function with our Pipe decorator and provided json.loads as our transformation function, our script can now read a JSON string from stdin, load that JSON into a Python dictionary, and write the result to a MongoDB.

Example usage:
```
> curl https://jsonplaceholder.typicode.com/posts | python to_db.py
```

Sure enough, if you open up your favorite Mongo client, you'll see that indeed the JSON list was written to the collection specified. A big thank you to [jsonplaceholder.typicode.com](jsonplaceholder.typicode.com) for providing the test data for this example.

__Reading command line arguments:__

If, for whatever reason, you want to pass a value into your script from the command line rather than reading it from stdin, you can do that too.

test.py
```python
from pipeable import Pipe

@Pipe()
def print_input(inp):
  return inp
```

```
> python test.py 'This is a test.'
This is a test.
```
