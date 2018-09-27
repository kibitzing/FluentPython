"""
created by Jingu Kang on 09-19
"""
# 어려워서 예제만 약간 변형..
# 내림차순 정렬 -> 오름차순 정렬 

import sys
import re
import collections

WORD_RE =re.compile(r'\w+')
index = {}

with open (sys.argv[1],encoding='utf-8') as fp:
    for line_no, line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            
            word = match.group()
            column_no = match.group()
            
            location = (line_no, column_no)
            
            occurences = index.get(word, [])
            occurences.append(location)
            index[word] = occurences
            
for word in sorted(index, key=str.lower):
    print(word, index[word])
#index = collections.defaultdict(list)
#
#with open(sys.argv[1], encoding='utf-8') as fp:
#    for line_no, line in enumerate(fp, 1):
#        for match in WORD_RE.finditer(line):
#            word = match.group()
#            column_no = match.start()+1
#            location = (line_no, column_no)
#            index[word].append(location)
#            
#            
#for word in sorted(index, key=str.lower):
#    print(word, index[word])
#
#
##WORD_RE =re.compile(r'\w+')
##
##index = {}
##with open(sys.argv[1], encoding='utf-8') as fp:
##    for line_no, line in enumerate(fp, 1):
##        for match in WORD_RE.finditer(line):
##            word = match.group()
##            column_no = match.start() + 1
##            location = (line_no, column_no)
##            index.setdefault(word, []).append(location)
##            
##for word in sorted(idnex, key=str.upper):
##    print(word, index[word])
