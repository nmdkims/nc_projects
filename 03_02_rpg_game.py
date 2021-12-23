# 스파르블로2 레져렉션 만들기
import random


class Object:
    """Super Class"""

    def __init__(self, Oname, Ohp, Odamage):
        self.name = Oname
        self.hp = Ohp
        self.damage = Odamage

    def death_check(self):
        if self.hp == 0:
            return 0
        else:
            return 1

    def show_info(self, Object):
        if not Object == 0:
            print(f'{self.name}        {self.hp}       {self.damage}')

    def attack(self, Target):
        Target.hp -= self.damage
        print(f'{self.name}이(가){Target.name}을 공격했습니다')
        if Target.hp <= 0:
            Target.hp = 0
        print(f'{Target.name}의 남은 체력은 {Target.hp}')


class monster(Object):
    def __init__(self, Oname, Ohp, Odamage):
        super().__init__(Oname, Ohp, Odamage)

    def wait(self):
        print(f'{self.name}이(가) 대기했습니다.')

    def heal(self):
        self.hp += 10
        print(f'{self.name}이(가) 자신의 체력을 10만큼 회복했다.')


class player(Object):
    def __init__(self, Oname, Ohp, Odamage):
        super().__init__(Oname, Ohp, Odamage)

    def magic(self, Object):
        Object.hp -= 50
        print(f'{self.name}이(가){Object.name}를 마법으로 공격했습니다')
        if Object.hp <= 0:
            Object.hp = 0
        print(f'{Object.name}의 남은 체력은 {Object.hp}')


def gameover(a, b, c, d):
    if a == 0:
        print("-----------------용사는 잠들었습니다 ---------------")
        print("---------------------Game Over-------------------")
        return 1

    elif b == 0 and c == 0 and d == 0:
        print("--------------악의 무리를 소탕하였습니다--------------")
        return 1


def showstatus():
    player.show_info(player.death_check())
    monster1.show_info(monster1.death_check())
    monster2.show_info(monster2.death_check())
    monster3.show_info(monster3.death_check())


def player_turn(player, monster1, monster2, monster3):
    print("--------------플레이어 턴입니다 --------------")
    showstatus()
    attack = input("공격 방법을 선택해주세요! '공격' 또는 '마법' : ")
    target = input("어떤 몬스터를 공격하시겠습니까?! '미니고블린' '고블린' '슈퍼고블린' : ")

    if attack == '마법':
        if target == '미니고블린':
            player.magic(monster1)
        elif target == '고블린':
            player.magic(monster2)
        elif target == '슈퍼고블린':
            player.magic(monster3)
        else:
            print('타겟 설정이 잘못되어 공격 기회를 잃어버렸습니다.')

    elif attack == '공격':
        if target == '미니고블린':
            player.attack(monster1)
        elif target == '고블린':
            player.attack(monster2)
        elif target == '슈퍼고블린':
            player.attack(monster3)
        else:
            print('타겟 설정이 잘못되어 공격 기회를 잃어버렸습니다.')
    else:
        print('공격 방법을 잘못 설정하여 기회를 잃어버렸습니다.')


def monster_turn(player, monster1, monster2, monster3):
    print("--------------몬스터의 턴입니다 --------------")
    showstatus()
    if monster1.hp != 0:
        monster_random_action(player, monster1)
    if monster2.hp != 0:
        monster_random_action(player, monster2)
    if monster3.hp != 0:
        monster_random_action(player, monster3)


def monster_random_action(player, monster):
    rs = random.randrange(0, 3)
    if rs == 0:
        monster.wait()
    elif rs == 1:
        monster.heal()
    elif rs == 2:
        monster.attack(player)


# 몬스터 설정
mini_goble = monster("미니고블린", 10, 10)
goble = monster("고블린", 30, 30)
super_goble = monster("슈퍼고블린", 50, 50)

# 용사 설정
player1 = player("전사", 100, 10)

sequence = random.randrange(0, 2)

while True:
    monster1 = mini_goble
    monster2 = goble
    monster3 = super_goble
    player = player1

    if gameover(player.death_check(), monster1.death_check(), monster2.death_check(), monster3.death_check()) == 1:
        break

    if sequence == 0:
        player_turn(player, monster1, monster2, monster3)
        sequence = 1
    elif sequence == 1:
        monster_turn(player, monster1, monster2, monster3)
        sequence = 0
