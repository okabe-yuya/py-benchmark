## py-benchmark
### description
This package can measure elapsed time(average time) of function too easy.  
Result is output to log(info level).


### Usage
※ example /src/funcs.py

1. import benchmark function
```python
from bench import benchmark
```

2. write decorator and number of executions on taget function
```python
# number of executions is 100
@benchmark(100)
def target_func():
  print("hello world")
```

3. execute function and result is output to log
```python
target_func()
INFO : 2020-03-14 19:10:52,033 : Start benchmark  target_func ...
INFO : 2020-03-14 19:10:52,169 : Result: Average execution time -> 0.00001 s (total exec 100)
````