from random import shuffle
lotto_make = list(range(1,45))
i = 1
while(True):
    shuffle(lotto_make)
    lotto = sorted(lotto_make[0:7])
    print(str(i)+"회차 당첨번호 : "+str(lotto[0:6]) + "보너스 번호 : " + str(lotto[6]))
    shuffle(lotto_make)
    picked = sorted(lotto_make[0:6])
    print("내 자동생성 번호 : "+str(picked))
    if(picked[0] in lotto and picked[1] in lotto and picked[2] in lotto and picked[3] in lotto and picked[4] in lotto and picked[5] in lotto):
        print(str(i)+"회차에 당첨되셨습니다.")
        print("자동으로 당첨될 확률은 : " +str(1/i))
        print("당첨되려고 박은 금액 : " + str(i*1000)+"원")
        print("인생을 갈아넣으셨네요")
        if(i*1000 < 500000000):
            print("근데 이정도면 이득이네요")
        break
    i = i+1
