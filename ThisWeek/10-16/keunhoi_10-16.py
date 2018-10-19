#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from inspect import signature

def tag(name, *content, cls=None, **attrs):
	"""Generate one or more HTML tags"""
	if cls is not None:
		attrs['class'] = cls
	if attrs:
		attr_str = ''.join(' %s="%s"' % (attr, value)
						   for attr, value
						   in sorted(attrs.items()))
	else:
		attr_str = ''
	if content:
		return '\n'.join('<%s%s>%s</%s>' %
						 (name, attr_str, c, name) for c in content)
	else:
		return '<%s%s />' % (name, attr_str)

class Exercise:

	def clip(self, text, max_len=80):
		'''max_len 앞 혹은 뒤의 마지막 공백에서 잘라낸 텍스트를 리턴한다.
		'''
		end = None
		if len(text) > max_len:
			space_before = text.rfind(' ', 0, max_len)
			if space_before >= 0:
				end = space_before
			else:
				space_after = text.rfind(' ', max_len)
				if space_after >= 0:
					end = space_after
		if end is None: # 공백이 없는 상황.
			end = len(text)
		return text[:end].rstrip()

	def clip_annot(self, text:str, max_len:'int > 0' = 80):
		'''max_len 앞 혹은 뒤의 마지막 공백에서 잘라낸 텍스트를 리턴한다. annotation 추가
		'''
		end = None
		if len(text) > max_len:
			space_before = text.rfind(' ', 0, max_len)
			if space_before >= 0:
				end = space_before
			else:
				space_after = text.rfind(' ', max_len)
				if space_after >= 0:
					end = space_after
		if end is None: # 공백이 없는 상황.
			end = len(text)
		return text[:end].rstrip()

E = Exercise

print(E.clip.__defaults__)
print(E.clip.__code__) # doctest: +ELLIPSIS
print(E.clip.__code__.co_varnames)
print(E.clip.__code__.co_argcount)
print(E.clip.__doc__) # 이전에 해봄
# print(E.clip.__name__) # 쓰잘데기 없이 너무 쉬움
print('Annotation of clip function:' , E.clip.__annotations__)
print('Annotation of clip_annot function:' , E.clip_annot.__annotations__)
# print(E.clip.__dict__)
print(E.clip.__globals__) # globals는 함수 뒤에 붙여서 작성해도 메모리에 선언된 객체 모두를 반환하는듯.
print(E.clip.__class__)
print(E.__class__) # class 객체는 <class 'type'> 을 출력.
print(E.clip.__hash__())
# print(E.__hash__()) # 이 경우는 TypeError: descriptor '__hash__' of 'object' object needs an argument

print("="*100)

sig = signature(E.clip)
print(sig) # 와..보기 엄청 편하네
print(sig.parameters.items())
print(sig.parameters)
print(type(sig.parameters.items()))
print(type(sig.parameters))

print("="*100)

for name, param in sig.parameters.items():
	print(param.kind, ':', name, '=', param.default)

print("="*100)
sig = signature(E.clip_annot)
for param in sig.parameters.values():
	note = repr(param.annotation).ljust(13)
	print(note, ':', param.name, '=', param.default)

print("="*100)

# param.kind나 default는 탭을 쳐도 안 나오던데
print('type of sig.parameters is :', type(sig.parameters)) # MappingProxyType 은 읽기 전용 dict로 Python 3.3에서 추가되었다고 한다.
print('type of sig.parameters is :', type(sig.parameters.items()))
# print('type of signature.parameters is :', type(signature.parameters))  # AttributeError: 'function' object has no attribute 'parameters'
# print('type of signature.parameters is :', type(signature().parameters)) # TypeError: signature() missing 1 required positional argument: 'obj'

print("="*100)

sig = signature(tag)
my_tag = {'name': 'sound', 'title': 'Gloomy Sunday','src': "GS.mp3",'cls':'tuned'}
bound_args = sig.bind(**my_tag)
print(bound_args)
for name, val in bound_args.arguments.items():
	print(name, '=', val)

print("="*100)

from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))
hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))

print("="*100)


from operator import mul
from functools import partial
import numpy as np
triple = partial(mul, 3)
print(triple(7))
print(list(map(triple, range(1,10))))
print(sum(map(mul, [3, 4], [-3, -4])))

# matmul = partial(np.matmul(), np.matrix([1,2],[3,4])) # 둘 다 에러.
# matmul = partial(np.matmul, np.matrix([1,2],[3,4]))
