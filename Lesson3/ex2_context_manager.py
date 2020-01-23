from random import randint
from contextlib import contextmanager

#
# with open('ex_3.txt') as test_file:
#     for each in test_file.read().split(' '):
#         print('test case is ' + each + ' ')
#

@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print('Не открывается файл!')
    finally:
        print('Closing file')
        f_obj.close()


if __name__ == '__main__':
    with file_open('test.txt') as fobj:
        fobj.write('My new context manager')
