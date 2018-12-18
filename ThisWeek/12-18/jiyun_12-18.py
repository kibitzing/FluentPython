# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 22:39:58 2018

@author: jiyun
"""

from mirror import LookingGlass

manager = LookingGlass()
monster = manager.__enter__()
print(monster == 'JABBERWOCKY') #eurT
print(monster) #YKCOWREBBAJ
manager.__exit__(None, None, None)
print(monster) #JABBERWOCKY

"""
import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write
    
    def reverse_write(text):
        original_write(text[::-1])
        
    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write
"""

from mirror_gen import looking_glass
with looking_glass() as what:
    print('1218')  #8121
    print(what) #YKCOWREBBAJ
    
"""
import contextlib

@contextlib.contextmanager
def looking_glass2():
    import sys
    original_write = sys.stdout.write
    
    def reverse_write(text):
        original_write(text[::-1])
        
    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please Do Not divide by zero'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)
    
"""

from mirror_gen import looking_glass2
with looking_glass2() as what:
    print('1218')  #8121
    print(what) #YKCOWREBBAJ
