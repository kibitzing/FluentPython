DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan')
        ]
d1 = dict(DIAL_CODES)
print('d1: ', d1.keys())

d2 = dict(sorted(DIAL_CODES))
print('d2: ', d2.keys())

d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))
print('d3: ', d3.keys())


DIAL_CODES2 = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        # missing Russia
        (81, 'Japan')
        ]

d4 = dict(DIAL_CODES2)
print('d4: ', d4.keys())

DIAL_CODES3 = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (82, 'Korea'),
        (81, 'Japan')
        ]

d5 = dict(sorted(DIAL_CODES3))
print('d5: ', d5.keys())


assert d1 == d2 == d3
# assert d1 == d4
# assert d1 == d5
