"""
created by jingu on 2018-09-18
"""

avengers = ['Thor', 'Iron man', 'Captain', 'Hulk', 'Spider man']
names = ['Thor', 'Tony Stark', 'Steve Rogers', 'Dr.Banner', 'Peter']

avengers_info = dict(zip(avengers, names))

print("Who are avengers? ans: ", avengers_info.keys())
print("Who are they? ans: ", avengers_info.values())
print("How many are ther? ans: ", len(avengers_info))

#### from the book
#a = dict(one=1,two=2,three=3)
#b = {'one': 1, 'two': 2, 'three': 3}
#c = dict(zip(['one', 'two', 'three'],[1,2,3]))
#d = dict([('two', 2),('one', 1),('three',3)])
#e = dict({'three':3, 'one':1, 'two': 2})
#
#DIAL_CODES = [(86,'CHINA'), (91,'INDIA'), (1,'US'),
#              (62,'INDONESIA'), (55,'BRAZIL'), (92,'PAKISTAN'), (880,'BANGLADESH')]
#country_code = {country: code for code, country in DIAL_CODES}
####