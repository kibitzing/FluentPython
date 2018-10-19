#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#p177~181


class MacroCommand:
	"""명령 리스트를 실행하는 명령
	"""

	def __init__(self, commands):
		self.commands = list(commands)

	def __call__(self):
		for command in self.commands:
			command(3)

def A(input):
	print(input)
	return input

def B(input):
	print(input+1)
	return input+1

command = [A, B]

M = MacroCommand(command)
# M.__init__(command)
M()

