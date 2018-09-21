"""
created by jingu kang on 2018-09-20
"""

class whoweare(dict):
    def __missing__(self,key):
        if isinstance(key ,str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default='normal person'):
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
    
fpStudyMember = whoweare([('Jingu','Iron man'),('Daeha', 'Dr.Strange'),('Keunhoi', 'Howkeye'),('Seongbin', 'Vision'),('Jiyun', 'Black Widow'),
                    ('Sanghong', 'Staroad'),('Seunghyun', 'Hulk')])

print('Jingu: ',fpStudyMember.get('Jingu')) # Jingu:  Iron man
print('Mingyu: ',fpStudyMember.get('Mingyu')) # Mingyu:  normal person
print(fpStudyMember['Mingyu']) # error