# Wrap Swift for Python

A small example project showing how to wrap Swift code for Python.

For a full tutorial, see [my post here](https://www.eliaslundgaard.com/posts/wrapping-swift-for-python/)

## Setup

Clone the repository, and open Terminal at the project directory.

In an environment with Python 3.10 activated, run:

```shell
pip install -e .
```

You can now import the module from Python:

```python
from mymodule import add
# This will call the Swift function
add(2, 2)
>> 4
```