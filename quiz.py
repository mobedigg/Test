#!python3
﻿#!python3
#Написать функцию-фабрику, которая будет возвращать функцию сложения с аргументом.
def addition(n):
    '''
    >>> add5 = addition(5) # функция addition возвращает функцию сложения с 5
    >>> add5(3) # вернет 3 + 5 = 8
    8
    >>> add5(8) # вернет 8 + 5 = 13
    13

    >>> add8 = addition(8)
    >>> add8(2) # вернет 2 + 8 = 10
    10
    >>> add8(4) # вернет 4 + 8 = 12
    12
    '''
    def add(x):
        return x+n
    return add

def addition_lambda(n):
    '''
    >>> add5 = addition_lambda(5) # функция addition возвращает функцию сложения с 5
    >>> add5(3) # вернет 3 + 5 = 8
    8
    >>> add5(8) # вернет 8 + 5 = 13
    13

    >>> add8 = addition_lambda(8)
    >>> add8(2) # вернет 2 + 8 = 10
    10
    >>> add8(4) # вернет 4 + 8 = 12
    12
    '''
    return lambda x: x+n


###############################################################################
class Observable:
    '''
    >>> class X(Observable):
    ...     pass
    >>> x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
    >>> #print(x)
    #X(bar=5, foo=1, name='Amok', props=('One', 'two'))
    >>> x.foo
    1
    >>> x.name
    'Amok'
    >>> x._bazz
    12
    '''
    def __init__(self, **kwargs):
        for i in kwargs:
            setattr(self, i, kwargs[i])

    def __str__(self):
        pass

    def some(self):
        return self.name

###############################################################################
#Написать класс, который бы по всем внешним признакам был бы словарем,
#но позволял обращаться к ключам как к атрибутам.
class DictAttr():

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __getitem__(self, key, val=None):
        if val:
            return self.__dict__.get(key, val)
        else:
            return self.__dict__[key]

    get = __getitem__

    def __setattr__(self, key, value):
       self.__dict__[key] = value

    __setitem__ = __setattr__

###############################################################################
#Реализовать дескрипторы, которые бы фиксировали тип атрибута
class Property():

    def __init__(self, value):
        self.val = value

    def __get__(self, obj, owner=None):
        return self.val

    def __set__(self, obj, val):
        if isinstance(val, type(self.val)):
            self.val = val
        else:
            raise TypeError


class Image(object):
    '''
    >>> img = Image()
    >>> img.height = 340
    >>> img.height
    340
    >>> img.path = '/tmp/x00.jpeg'
    >>> img.path
    '/tmp/x00.jpeg'
    >>> img.path = 320
    Traceback (most recent call last):
      ...
    TypeError
    '''
    height = Property(0)
    width = Property(0)
    path = Property('/tmp/')
    size = Property(0)


###############################################################################
#Реализовать базовый класс (используя метакласс), который бы фиксировал тип атрибута
'''
>>> class Image(Object):
...     height = 0
...     width = 0
...     path = '/tmp'
...     size = 0

>>> img = Image()
>>> img.height = 340
>>> img.height
340
>>> img.path = '/tmp/x00.jpeg'
>>> img.path
'/tmp/x00.jpeg'
>>> img.path = 320
Traceback (most recent call last):
  ...
TypeError
'''


###############################################################################
#Реализовать базовый класс (используя метакласс) и дескрипторы, которые бы на основе класса создавали SQL-схему (ANSI SQL) для модели:
'''
>>> class Image(Table):
...     height = Integer()
...     width = Integer()
...     path = Str(128)

>>> print(Image.sql())
CREATE TABLE image (height integer, width integer, path varchar(128))
'''
class Integer():
    def __get__(self):
        return 'integer'


class Str():

    def __init__(self, length):
        self.length = length

    def __get__(self):
        return 'varchar({0.length})'.format(self)


class MetaSQL(type):
    def __new__(cls, classname, bases, dictionary):

        def msql():
            string = 'CREATE TABLE {tablename} ('.format(tablename=classname.lower())
            lst = []

            for k in sorted(dictionary):
                if isinstance(dictionary[k], Integer):
                    lst.append(str(k)+' integer')
                elif isinstance(dictionary[k], Str):
                    lst.append(str(k) + ' varchar({0.length})'.format(dictionary[k]))

            string += ', '.join(lst) + ')'
            return string

        dictionary['sql'] = msql
        return super().__new__(cls, classname, bases, dictionary)


class Table(metaclass=MetaSQL):
    pass
###############################################################################


def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
