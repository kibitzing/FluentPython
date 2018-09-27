#!/usr/bin/envs python3
# -*- coding: utf-8 -*- --> 파이썬 3부터는 utf-8이 기본 인코딩임

#################################
#
#       Inha University
#     DSP Lab Sanghong Kim
#
#
#################################

"""
2018_09_18_Fluent_Python
@Author Sanghong.Kim
매핑 및 해시
지능형 딕셔너리
setdefault
핸드폰에서 지역 설정 및 전화 거는 프로그램
"""

# Import Modules
import time
import sys
import argparse

DIAL_CODES = [
    ('010', 'CellPhone'),
    ('02', 'Seoul'),
    ('031', 'Gyeonggido'),
    ('032', 'Incheon'),
    ('033', 'Gangwondo'),
    ('041', 'Chungcheongnamdo'),
    ('042', 'Daejeon'),
    ('043', 'Chungcheongbukdo'),
    ('044', 'Sejong'),
    ('051', 'Busan'),
    ('052', 'Ulsan'),
    ('053', 'Daegu'),
    ('054', 'Gyeongsangbukdo'),
    ('055', 'Gyeongsangnamdo'),
    ('061', 'Jeollanamdo'),
    ('062', 'Gwangju'),
    ('063', 'Jeollabukdo'),
    ('064', 'Jeju')
]

def Hello():
    time.sleep(3)
    print("          _____                    _____                    _____            _____           _______         ")
    print("         /\    \                  /\    \                  /\    \          /\    \         /::\    \        ")
    print("        /::\____\                /::\    \                /::\____\        /::\____\       /::::\    \       ")
    print("       /:::/    /               /::::\    \              /:::/    /       /:::/    /      /::::::\    \      ")
    print("      /:::/    /               /::::::\    \            /:::/    /       /:::/    /      /::::::::\    \     ")
    print("     /:::/    /               /:::/\:::\    \          /:::/    /       /:::/    /      /:::/~~\:::\    \    ")
    print("    /:::/____/               /:::/__\:::\    \        /:::/    /       /:::/    /      /:::/    \:::\    \   ")
    print("   /::::\    \              /::::\   \:::\    \      /:::/    /       /:::/    /      /:::/    / \:::\    \  ")
    print("  /::::::\    \   _____    /::::::\   \:::\    \    /:::/    /       /:::/    /      /:::/____/   \:::\____\ ")
    print(" /:::/\:::\    \ /\    \  /:::/\:::\   \:::\    \  /:::/    /       /:::/    /      |:::|    |     |:::|    |")
    print("/:::/  \:::\    /::\____\/:::/__\:::\   \:::\____\/:::/____/       /:::/____/       |:::|____|     |:::|    |")
    print("\::/    \:::\  /:::/    /\:::\   \:::\   \::/    /\:::\    \       \:::\    \        \:::\    \   /:::/    / ")
    print(" \/____/ \:::\/:::/    /  \:::\   \:::\   \/____/  \:::\    \       \:::\    \        \:::\    \ /:::/    /  ")
    print("          \::::::/    /    \:::\   \:::\    \       \:::\    \       \:::\    \        \:::\    /:::/    /   ")
    print("           \::::/    /      \:::\   \:::\____\       \:::\    \       \:::\    \        \:::\__/:::/    /    ")
    print("           /:::/    /        \:::\   \::/    /        \:::\    \       \:::\    \        \::::::::/    /     ")
    print("          /:::/    /          \:::\   \/____/          \:::\    \       \:::\    \        \::::::/    /      ")
    print("         /:::/    /            \:::\    \               \:::\    \       \:::\    \        \::::/    /       ")
    print("        /:::/    /              \:::\____\               \:::\____\       \:::\____\        \::/____/        ")
    print("        \::/    /                \::/    /                \::/    /        \::/    /         ~~              ")
    print("         \/____/                  \/____/                  \/____/          \/____/                          ")
    print("")

def Set_Region():
    region_code={region: code for code, region in DIAL_CODES}
    print("Region List : ", region_code.keys())
    User=input("Please Set Your Region : ")
    try:
        region_num=region_code[User]
    except KeyError as e:
        print("No Matching Region, Set Region Number as CellPhone")
        region_num=region_code.setdefault('CellPhone')
    return region_num

def Call(region_num):
    number = input("Press number : ")
    try:
        int(number)
    except ValueError as e:
        print("Please enter an adequate Value")
        sys.exit()

    num = region_num + number
    print("Call to :",num)
    #print("now Calling")
    for i in range(60):
        print(".",end=" ")

    print()
    Hello()

def main(args):
    # 지역 번호 설정, Default = 010
    if args.setregion :
        region_num = Set_Region()
    else:
        region_num = '010'
    # 전화 걸기
    Call(region_num)


# Arguments Setting
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--setregion", dest='setregion', action='store_true', help="Set Your Region")
    parser.set_defaults(list=False)
    args = parser.parse_args()
    # This program cannot completely avoid Arguments error
    if len(sys.argv) > 3:
        print ("Too many Arguments!")
        parser.print_help()
        sys.exit(0)
    main(args)