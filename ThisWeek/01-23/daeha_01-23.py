#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 프로퍼티 속성을 이용한 예제

    refer link:
    https://whatisthenext.tistory.com/115

"""

class Movie:
    def __init__(self, movie_name):
        self.__movie_name = movie_name
        
    @property  # 클래스 정의에 있는 코드만 수정하면 손쉽게 속성을 변경할 수 있음
    def movie_name(self):
        return self.__movie_name
    
    @movie_name.setter
    def movie_name(self, new_movie_name):
        self.__movie_name = new_movie_name
        print(' Change movie name by using setter ')
        print(' Changed movie name: {}'.format(self.movie_name))
        print("\n")
        

movie = Movie("23 personality")
print(movie.movie_name)

movie.movie_name = 'IO'
print(movie.movie_name)

movie.movie_name = '23 personality'
print(movie.movie_name)