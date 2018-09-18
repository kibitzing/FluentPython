from operator import eq
Player_Stat = [
    ('FW', 'Kim Sin Wook'),
    ('MF', 'Koo Ja Chul'),
    ('GK', 'Kim Seung Gyu'),
    ('MF', 'Son Heung Min'),
    ('MF', 'Ki Sung Yong'),
    ('MF', 'Lee Jae Sung'),
    ('MF', 'Go Yo Han'),
    ('DF', 'Kim Jin Soo'),
    ('DF', 'Kim Young Kwon'),
    ('DF', 'Jang Hyun Soo'),
    ('DF', 'Lee Yong'),
    ('FW', 'Lee Keun Ho'),
    ('MF', 'Lee Chung Yong')
]
Player = {Name : Position for Position, Name in Player_Stat}

print('FW Player : ')
print({Name for Name,Position in Player.items() if eq(Position,'FW')})

print('MF Player : ')
print({Name for Name,Position in Player.items() if eq(Position,'MF')})

print('DF Player : ')
print({Name for Name,Position in Player.items() if eq(Position,'DF')})

print('GK Player : ')
print({Name for Name,Position in Player.items() if eq(Position,'GK')})

