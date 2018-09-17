import bisect
#중복된 아이디 확인하여 하나씩만 출력

contributor = ['kbitzing','114569','zelabean','114569','114569','khahn0213','khahn0213','zelabean','zelabean','sseung0703','114569','kdhht2334','zelabean']
contributor = sorted(contributor)
count = 0;
result = []
for i in range(0,contributor.__len__()):
    search = contributor[i]
    l_idx = bisect.bisect_left(contributor,search)
    r_idx = bisect.bisect_right(contributor,search)
    if(l_idx+1 < r_idx):
        contributor[i] = ''
        count = count+1;

contributor = sorted(contributor)
print(contributor[count:])
