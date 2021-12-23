a = int(input())
while a > 100 or a <= 0:
    if a <= 100 and a >= 1:
        break
    else:
        while a > 100 or a <= 0:
              print('다시 입력해주세요')
              a = int(input())

p = 50
up = 100
down = 0
print(p)
while 1:

    if(p == a):
        print('성공')
        break
    else:
        c = input()
        if (c == str('up') and a > p):
            down = p
            p = int((up+p)/2)
            print(p)
        elif(c == str('down') and a < p):
            up = p
            p = int((down+p)/2)
            print(p)
        elif(p == a):
            print('성공')
            break
        else:
            print('잘못답하셨습니다. 다시 입력해주세요')
    # elif (input() == str('down')):
    #     p = (max_int - min_int)/2-p
    #
    #     print(p)
    # else:
    #     print('다시 입력하세요')