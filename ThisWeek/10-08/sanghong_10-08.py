#!/usr/bin/envs python3
# -*- coding: utf-8 -*-

#################################
#
#       Inha University
#     DSP Lab Sanghong Kim
#
#
#################################

"""
2018_10_08_Fluent_Python
@Author Sanghong.Kim
오늘 해당 예제를 보면서 기존에 정제하고 있던 Yelp_review Data가 떠올랐다.
json 파일을 csv 파일로 변경하는 것인데 csv가 unicode형태가 아니라 동작을 하지 않았었다.
이를 from unicodedata 를 할때 unicodecsv라는 것을 잘못 불러왔던 것을 이용하여 해결 한 것을 적어본다.
json 파일의 크기가 크기 때문에 작게 파일을 가지고 코드를 올려 본다.
"""

# Import Modules
import time
import os
import sys
import argparse
from unicodedata import normalize, name
import unicodecsv as csv
import json

def main(args):
    # Started Time
    st=time.time()

    """
    # example Code
    
    s1 = 'Café'
    s2 = 'Cafe\u0301'

    print(len(s1),len(s2))
    print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
    print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
    print(normalize('NFC', s1) == normalize('NFC', s2))
    print(normalize('NFD', s1) == normalize('NFD', s2))

    ohm = '\u2126'
    ohm_c = normalize('NFC', ohm)
    
    
    print(ohm == ohm_c)
    print(normalize('NFC', ohm) == normalize('NFC',ohm_c))
    # NFC 와 NFD로 Normalize 한것은 모두 TRUE
    print(normalize('NFD', ohm) == normalize('NFD',ohm_c))

    half = '½'
    print(normalize('NFKC', half))

    micro = 'µ'
    micro_kc = normalize('NFKC', micro)
    ohm_kc = normalize('NFKC', ohm)
    print(micro, micro_kc)
    print(ohm, ohm_kc)

    for i in ohm, ohm_c, ohm_kc, micro, micro_kc:
        print(name(i))


    """

    """
    # 원래의 코드는 아래와 같다. 해당 코드도 직접 짠 코드이지만 python2에서 작업을 하였다.
    # 해당 코드를 python3에 맞도록 변경 하여 보았다.
    
    import os
    import sys
    import unicodecsv as csv
    import json
    import io
    
    with io.open("yelp_review_data_original.json", mode="r", encoding="utf-8") as file:
        lines = file.readlines()


    with io.open("yelp_review_10per.json", mode="w", encoding="utf-8") as file:
    #       for i in range(0,530700):
            for i in range(0,len(lines)/10):
                file.write(lines[i])

    os.system('bash tab.sh')

    input = open("test.json", "r")
    data = json.load(input)
    input.close()

    file = csv.writer(open("yelp_review_10per.csv", "wb+"), encoding='utf-8')
    file.writerow(["review_id", "user_id", "business_id", "stars", "date", "text", "useful", "funny", "cool"])

    for x in data:
        file.writerow([
                x["review_id"],
                x["user_id"],
                x["business_id"],
                x["stars"],
                x["date"],
                x["text"],
                x["useful"],
                x["funny"],
                x["cool"]
                ])

    # 개인적인 이유로 Yelp dataset 으로 제공되는 json 파일을 csv 형태로 바꾸어 달라는 요청이 들어와 작업한 것이다.
    """

    with open("yelp_review_10000.json", "r") as file:
        data = json.load(file)

    file = csv.writer(open("yelp_review_10000.csv", "wb+"), encoding='utf-8')
    file.writerow(["review_id", "user_id", "business_id", "stars", "date", "text", "useful", "funny", "cool"])

    for x in data:
        file.writerow([
                x["review_id"],
                x["user_id"],
                x["business_id"],
                x["stars"],
                x["date"],
                x["text"],
                x["useful"],
                x["funny"],
                x["cool"]
                ])

    # Ended Time
    et=time.time()

    print("json file is successfully converted as csv file")

    # Running Time (End Time - Start Time)
    print ("Running Time : ",et-st,"s")


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
