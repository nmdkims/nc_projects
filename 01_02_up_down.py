import random


def input_check():
    input_number = input("숫자를 입력하세요:")
    P = int(input_number)
    if P < 0 or P > 100:
        print('범위를 벗어났습니다. 0 ~ 100까지의 숫자중 입력하세요')
        P = input_check()
        return P
    else:
        return P


print("업/다운 게임입니다. 0~100까지의 숫자중 하나를 맞춰보세요. 기회는 5번 주어집니다")
C = random.randrange(0, 100)
cnt = 0


while 1:
    try:
        P = input_check()

    except:
        # i = i - 1
        print("숫자만 입력 가능합니다.")

    else:
        cnt = cnt + 1

        if P == C:
            print('성공')
            break

        elif cnt == 5:
            print(f'랜덤 숫자는:{C}')
            print('실패')
            break

        elif P < C:
            print('UP')

        elif P > C:
            print('DOWN')
