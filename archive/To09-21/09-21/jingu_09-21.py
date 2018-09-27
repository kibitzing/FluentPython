"""
created by Jingu Kang on 2018-09-21
"""

script = "python은 매우 실용적이고 user-friendly한 프로그래밍 언어로 프로그래밍을 처음 접하는 사람들이 부담없이 시작할 수 있다. 이는 JAVA보다도 쉽지만\
그 안에 담고 있는 내용은 결코 쉽지 않고 많은 philosophy를 담아낸 아주 delicate한 language이다."
            
script_set = {i for i in script}
alphabet_set = {chr(abc) for abc in range(65,123)}

found = script_set & alphabet_set
print(found)

alphabetInScript = []

for char in found:
    script_list = list(script)
    i_compensation = 0;
    for i in range(script_list.count(char)):
        idx = script_list.index(char)
        alphabetInScript.append(idx+i)
        script_list.pop(idx)
        i = i+1
        
alphabetInScript.sort()



alphabetOnlyScript = ''.join([script[i] for i in alphabetInScript])

print(str(alphabetOnlyScript))
        
        