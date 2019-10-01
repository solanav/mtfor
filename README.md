# What is mtfor

"mtfor" or "multithreaded for" is a simple package that provides a for loop that automatically distributes the processing through a number of threads.

# Installation

You can use pip3 to install this utility by executing:
```
pip3 install mtfor
```

# Usage

The function signature is mtfor(list, function, number_of_threads). It returns your list already modified.

This example prints the result of applying my_function to my_list using 4 threads.

```python
from mtfor import mtfor

NUM_THREADS = 4

def my_function(x):
  return x * x

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
modified_list = mtfor(my_list, my_function, NUM_THREADS)

print(modified_list)
```
