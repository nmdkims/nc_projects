def input_check():
    input_number = input("숫자를 하나 입력하세요 범위는 0~100 컴퓨터가 찾게 될것입니다 : ")
    P = int(input_number)
    if P < 0 or P > 100:
        print('범위를 벗어났습니다. 0 ~ 100까지의 숫자중 입력하세요')
        P = input_check()
        return P
    else:
        return P


active = 1
cnt = 0
max = 100
min = 0
C = 50
try:
    P = input_check()

except:

    print("숫자만 입력 가능합니다.")

else:
    while active:

        print(f'{C} 인가요?')

        if P == C:
            print('성공')
            break
        else:
            check_up_down = input(":")
            if check_up_down == '업' or check_up_down == '다운':
                if P < C and check_up_down == '다운':
                    max = C
                    C = int((min + C) / 2)
                    print('DOWN')

                elif P > C and check_up_down == '업':
                    min = C
                    C = int((max + C) / 2)
                    print('UP')
                else:
                    print('You 라이어 다시 알려주세요')

            else:
                print('업/다운으로 입력해주세요')
