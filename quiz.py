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

class Observable:
    '''
    >>> class X(Observable):
    ...     pass
    >>> x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
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
        atr = [at for at in vars(self) if not at.startswith('_')]
        at = {k:getattr(self, k) for k in atr}
        st = "{0.__class__.__name__}({1})".format(self, at)
        return st
    
    def some(self):
        return self.name

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


def _test():
    import doctest
    doctest.testmod()
    
if __name__ == '__main__':
    _test()