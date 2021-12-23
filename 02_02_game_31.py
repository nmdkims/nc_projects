# 베스킨라빈스31 인공지능 만들기
import random


def must_win(num, must, mode):
    if mode == 2 and num == 0:
        must_num = 2
        mode = 3
        return (must_num, mode)
    elif mode != 3:
        if num < 2:
            must_num = 2 - num
            mode = 3
            return (must_num, mode)
        elif 2 < num < 6:
            must_num = 6 - num
            mode = 3
            return (must_num, mode)
        elif 6 < num < 10:
            must_num = 10 - num
            mode = 3
            return (must_num, mode)
        elif 10 < num < 14:
            must_num = 14 - num
            mode = 3
            return (must_num, mode)
        elif 14 < num < 18:
            must_num = 18 - num
            mode = 3
            return (must_num, mode)
        elif 18 < num < 22:
            must_num = 22 - num
            mode = 3
            return (must_num, mode)
        elif 22 < num < 26:
            must_num = 26 - num
            mode = 3
            return (must_num, mode)
        elif 26 < num < 30:
            must_num = 30 - num
            mode = 3
            return (must_num, mode)
        else:
            must_num = int(random.randrange(1, 4))
            return (must_num, mode)


    elif mode == 3 and num > 0:
        must_num = 4 - must

        return (must_num, mode)
    else:
        must_num = int(random.randrange(1, 4))
        return (must_num, mode)


def computer_choice(num, must, mode):
    try:
        computerchoice, mode = must_win(num, must, mode)
    except:
        print('컴퓨터가 머리쓰는 중입니다. 랜덤함수라 이리로 들어올 일은 없습니다')
    else:
        if 31 < num + computerchoice:
            print('31 넘지 않는 수로 재계산 중입니다')
            computerchoice, mode = computer_choice(num, must, mode)
            return (computerchoice, mode)
        else:
            return (computerchoice, mode)


def user_choice(num):
    try:
        userchoice = int(input("숫자 몇개를 부르시겠습니까? 1~3까지 가능 :"))
    except:
        print('숫자를 입력해주세요')
        userchoice = user_choice(num)
        return userchoice

    else:
        if 31 < num + userchoice:
            print('31을 초과하였습니다. 다시 불러주세요')
            userchoice = user_choice(num)
            return userchoice

        elif 0 < userchoice < 4:
            return userchoice

        elif userchoice > 3 or userchoice < 1:
            print('1~3의 숫자를 입력해주세요')
            userchoice = user_choice(num)
            return userchoice

        else:
            print('알수없는 오류')


sequence = int(random.randrange(1, 3))
num = 0
win = 0
must = 0
mode = 0

if sequence == 1:
    print('플레이가 먼저 진행합니다')
    mode = 1

elif sequence == 2:
    print('컴퓨터가 먼저 진행합니다')
    mode = 2

while num < 31:
    active = 0
    count = 0
    sequence += 1
    # print(f'반복횟수 : {num}')

    if sequence % 2 != 0:
        count, mode = computer_choice(num, must, mode)
        must = 0
        while active < count:
            active += 1
            num += 1
            print(f'컴퓨터 : {num}')
            win = 1

    else:
        count = user_choice(num)
        must = count
        # print(f'값확인 : {count}')
        while active < count:
            active += 1
            num += 1
            print(f'플레이어 : {num}')
            win = 2

if win == 1:
    print('플레이어 승리')

elif win == 2:
    print('컴퓨터 승리')
