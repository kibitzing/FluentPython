# created by Jingu Kang on 2019-02-08
# reference: Fluent Python by Luciano Ramalho
# Implement to check the sequence of executions.

import os
print('#### Import HiHello ####')
from HiHello import Hi


print('#### exec python HiHello.py ####')
os.system('python HiHello.py')

print('#### play with Hi ####')
Hi.nihao()

hi = Hi()
hi.hello()
hi.bye()


