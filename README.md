# Big Data Processing
.pem for ssh to ec2

`import inspect` https://docs.python.org/3/library/inspect.html



# Python Package Hosting
so its ofishal

[pypiserver](https://www.linode.com/docs/applications/project-management/how-to-create-a-private-python-package-repository/)

[pypa/warehouse](https://github.com/pypa/warehouse)


# TODO
- debugger
- print current thread
- hosting python package over the internet


# Interesting
[import inspect](https://docs.python.org/3/library/inspect.html)
```
>>> test_for_class = inspect.stack()
>>> type(test_for_class)
<class 'list'>
>>> test_for_class.isclass()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'isclass'
>>> inspect.isclass(test_for_class)
False
```




```
# doesnt work
# print(threading.currentThread()) # or current_thread()
# or [2][3] for parent function

# is of type class:
# inspect.stack()


# print(inspect.getframeinfo())
# for thing in my_list:
#     print(thing)


# print(inspect.stack()) 
```


