import hashlib

id = ""
id_i = ""
pw_i = ""
pw = ""
pw_c = ""



def signup():
    print("회원가입 화면입니다. 등록할아이디와 패스워드를 입력하세요")
    print("ID : ")
    ck = 1;
    global id
    id = input()
    while(ck):
        print("PW : ")
        global pw,pw_c
        pw = input()
        pw = pw.encode()
        h1 = hashlib.md5()
        h1.update(pw)
        pw = h1.hexdigest()

        print("PW_conf : ")
        pw_c = input()
        pw_c = pw_c.encode()
        h2 = hashlib.md5()
        h2.update(pw_c)
        pw_c = h2.hexdigest()
        if pw == pw_c:
            ck = 0
            print("가입이 완료되었습니다.")
        else:
            print("비밀번호가 다릅니다.")


def signin():
    print("ID : ")
    id_i = input()
    print("PW : ")
    pw_i = input()
    pw_i = pw_i.encode()
    h3 = hashlib.md5()
    h3.update(pw_i)
    pw_i = h3.hexdigest()
    if pw == pw_i and id == id_i:
        print("로그인 되었습니다")
    else:
        print("로그인 실패")
        signin()




signup()
signin()
