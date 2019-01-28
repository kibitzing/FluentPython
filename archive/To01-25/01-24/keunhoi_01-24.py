#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# p615-ch19end
# Example 19-27~2

"""
	예제 위주로 작성
	프로퍼티 문서화

"""

# Example 19-26
class BlackKnight:

	def __init__(self):
		self.members = ['an arm', 'another arm',
						'a leg', 'another leg']
		self.phrases = ["'Tis but a scratch.",
						"It's just a flesh wound.",
						"I'm invincible!",
						"All right, we'll call it a draw."]

	@property
	def member(self):
		print('next member is:')
		return self.members[0]

	@member.deleter # 이런 deleter의 존재는 어디서 찾아내는거죠...?
	def member(self):
		text = 'BLACK KNIGHT (loses {})\n-- {}'
		print(text.format(self.members.pop(0), self.phrases.pop(0)))


if __name__ == "__main__":
	knight = BlackKnight()
	print(knight.member)
	del knight.member
	del knight.member
	del knight.member
	del knight.member

