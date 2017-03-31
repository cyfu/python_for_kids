'''
https://pyformat.info/
'
'''
Basic formatting
'''
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))

print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

#not available in old way
print('{1} {0}'.format('one', 'two'))



'''Value conversion
'''
class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'

print('%s %r' % (Data(), Data()))
print('{0!s} {0!r}'.format(Data()))

class Data1(object):

    def __repr__(self):
        return 'räpr'

print('%r %a' % (Data(), Data()))
print('{0!r} {0!a}'.format(Data()))


'''Padding and aligning strings
'''
print('%10s' % ('test',))
print('{:>10}'.format('test'))

print('%-10s' % ('test',))
print('{:10}'.format('test'))
print('{:<10}'.format('test'))

#This operation is not available with old-style formatting.
print('{:_<10}'.format('test'))
print('{:_>10}'.format('test'))

#This operation is not available with old-style formatting.
print('{:^10}'.format('test'))
print('{:#^10}'.format('test'))

print('{:#^11}'.format('test'))

'''Truncating long strings
'''
print('%5s' % ('xylophone'))
print('%.5s' % ('xylophone'))
print('{:5}'.format('xylophone'))
print('{:.5}'.format('xylophone'))

'''Combining truncating and padding
'''
print('%-10.5s' % ('xylophone',))
print('{:10.5}'.format('xylophone'))


'''Numbers
'''
#Integers
print('%d' % (42,))
print('{:d}'.format(42))

#Floats
print('%f' % (3.141592653589793,))
print('{:f}'.format(3.141592653589793))

'''Padding numbers
'''
print('%4d' % (42,))
print('{:4d}'.format(42))

print('%04d' % (42,))
print('{:04d}'.format(42))

print('%06.2f' % (3.141592653589793,))
print('{:06.2f}'.format(3.141592653589793))

'''Signed numbers
'''
print('%+d' % (42,))
print('{:+d}'.format(42))


print('% d' % ((- 23),))
print('{: d}'.format((- 23)))


#This operation is not available with old-style formatting.
print('{:=5d}'.format((- 23)))
print('{:=+5d}'.format(23))

'''Named placeholders
'''
data = {'first': 'Hodor', 'last': 'Hodor!'}
print('%(first)s %(last)s' % data)
print('{first} {last}'.format(**data))

#This operation is not available with old-style formatting.
print('{first} {last}'.format(first='Hodor', last='Hodor!'))

'''Getitem and Getattr
'''
#This operation is not available with old-style formatting.
person = {'first': 'Jean-Luc', 'last': 'Picard'}
print('{p[first]} {p[last]}'.format(p=person))
data = [4, 8, 15, 16, 23, 42]
print('{d[4]} {d[5]}'.format(d=data))

class Plant(object):
    type = 'tree'

print('{p.type}'.format(p=Plant()))

class Plant1(object):
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]

print('{p.type}: {p.kinds[0][name]}'.format(p=Plant1()))

'''Datetime
'''
#This operation is not available with old-style formatting.
from datetime import datetime
print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))

'''Parametrized formats
'''
#This operation is not available with old-style formatting.
print('{:{align}{width}}'.format('test', align='^', width='10'))

print('%.*s = %.*f' % (3, 'Gibberish', 3, 2.7182))
print('{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3))


print('%*.*f' % (5, 2, 2.7182))
print('{:{width}.{prec}f}'.format(2.7182, width=5, prec=2))

print('{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.3'))

from datetime import datetime
dt = datetime(2001, 2, 3, 4, 5)
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))

print('{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3))
print('{:{}{sign}{}.{}}'.format(2.7182818284, '>', 10, 3, sign='+'))

'''Custom objects
'''
class HAL9000(object):

    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL 9000'

print('{:open-the-pod-bay-doors}'.format(HAL9000()))
