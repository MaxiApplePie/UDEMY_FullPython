from ast import Param


def foo(param):
    print(id(param))

var = 5 
print(id(var))
foo(param=var)

