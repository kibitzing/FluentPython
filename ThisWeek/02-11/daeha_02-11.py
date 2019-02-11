#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" hashtable examples

    refer below:
    https://github.com/anatoliy325/hashtable

"""        
import sqlite3

class hashtable(object):
    def __init__(self, dbname):
        self.con = sqlite3.connect(dbname)

    def __del__(self):
        self.con.close()

    def commit(self):
        self.con.commit()

    def createtable(self,hash_algs=['md5']):
	#print hash_algs
        self.hash_algs = hash_algs
        self.con.execute('create table wordlist(word)')
        for alg in self.hash_algs:
            self.con.execute('create table %s(hash,wordid)' % alg)
            self.con.execute('create index %s on %s(hash)' % (alg+'hidx',alg))
            self.con.execute('create index %s on %s(wordid)' % (alg+'widx',alg))
        self.con.commit()
        
    def getwordid(self, word):
        res = self.con.execute("select rowid from wordlist where word='%s'" % word).fetchone()
        if res == None:
            cur = self.con.execute("insert into wordlist(word) values ('%s')" % word)
            return cur.lastrowid
        else:
            return res[0]

    def isexists(self,hash_value,hash_alg='md5'):
	    if hash_alg not in self.hash_algs: return None
	    h = self.con.execute("select wordid from %s where hash='%s'" \
		                      % (hash_alg,hash_value)).fetchone()
	    if h != None:
	        w = self.con.execute("select * from wordlist where rowid='%d'" \
		                          % h[0]).fetchone()
	    if w != None:
	        return True
	    return False

    def addentry(self, word, hash_value,hash_alg='md5'):
	    if hash_alg not in self.hash_algs: return None
	    if not self.isexists(hash_value,hash_alg):
	        wordid = self.getwordid(word)
	        #cur = self.con.execute("insert into hashlist(%s,wordid) values ('%s','%d')" \
			    #% (hash_alg,hash_value,wordid))
	    u = self.con.execute('select * from %s where wordid=%d' % (hash_alg,wordid)).fetchone()
	    if u != None:
	    	cur = self.con.execute("update %s set hash='%s' where wordid=%d" \
		    	% (hash_alg,hash_value,wordid))
	    else:
		    cur = self.con.execute("insert into %s(hash,wordid) values ('%s','%d')" \
			    % (hash_alg,hash_value,wordid))
	    self.commit()
	    return cur.lastrowid
	    return None

    def search(self, hash_value,hash_alg='md5'):
	    if hash_alg not in self.hash_algs: return None
	    wordid = self.con.execute("select wordid from %s where hash='%s'" \
		    	% (hash_alg,hash_value)).fetchone()[0]
	    return self.con.execute("select word from wordlist where rowid='%d'" \
		    % wordid).fetchone()[0]
    
    

import hashlib


def calc_hash(word,hash_alg='md5'):
    if hash_alg not in hashlib.algorithms:
        print ("%s isn't exists in 'hashlib'!" % hash_alg)
        return None

    hash_obj = hashlib.new(hash_alg)
    hash_obj.update(word.encode())
    return hash_obj.hexdigest()


htable = hashtable('party_list.db')

print("\n")
try:
    htable.createtable(hashlib.algorithms)
except:
    pass

print("\n")
try:
    with open('party_list.txt','r') as file:
        line = file.readline()
        i = 1
        while line != None and i < 10:
            if line == '\n' or line == ' ':
                line = file.readline()
                continue
        line = (line.split(' ')[0]).split('\n')[0]
        for alg in htable.hash_algs:
            hash_string = calc_hash(line,alg)
        if hash_string != None and len(hash_string) > 0:
            htable.addentry(line,hash_string,alg)
        print('(%d) added %s' % (i,line))
        i += 1
        line = file.readline()
except:
    htable.con.close()

print("Finish!")

htable.con.close()