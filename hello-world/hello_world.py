# Solution for the Python "Hello World" exercise.

def isBlank(str=None):
    return True if ((str is None) or (str == '')) else False 

def hello(name=''):
    if (isBlank(name)):
        name = 'World'
    return 'Hello, ' + name + '!'