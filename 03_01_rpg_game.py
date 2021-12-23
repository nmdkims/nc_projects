# class Status:
#     def __init__(self, param_name, param_name_chr_class, param_hp, param_ap):
#         print("i am player!", self)
#         self.name = param_name
#         self.chr_class = param_name_chr_class
#         self.hp = param_hp
#         self.ap = param_ap
#
#     def attack(self):
#         print( self.name, "은 공격을 하였다!")
#
#
# class Player(Status):
#     def __init__(self, param_name):
#         print("i am monster!", self)
#         self.name = param_name
#
#     def talk(self):
#         print("안녕하세요, 제이름은",self.name, "입니다")
#
# class Monster(Status):
#     def __init__(self, param_name):
#         print("i am monster!", self)
#         self.name = param_name
#
#     def talk(self):
#         print("안녕하세요, 제이름은",self.name, "입니다")
#
#
#
# player_1 = Player("유재석","전사",50,10)
# player_1.attack()


# We're constructing a class name hero
# Hhealth = Hero Health
import random


class Hero:
    def __init__(self, Hhealth, Hattack, Hluck, Hdefence, Hmagic, Hname):
        self.name = Hname
        self.health = Hhealth
        self.attack = Hattack
        self.luck = Hluck
        self.defence = Hdefence
        self.magic = Hmagic

    # we're gonna get setters and getters
    # These are getters, where we can check the health or attack of the character
    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getLuck(self):
        return self.luck

    def getDefence(self):
        return self.defence

    def getMagic(self):
        return self.magic

    # setters is what we can use to change a variable
    # for example if we want to set a new attack value
    def setHealth(self, newHealth):
        self.health = newHealth

    def setAttack(self, newAttack):
        self.attack = newAttack

    def setLuck(self, newLuck):
        self.luck = newLuck

    def setDefence(self, newDefence):
        self.defence = newDefence

    def setMagic(self, newMagic):
        self.magic = newMagic


class Enemy:
    def __init__(self, Ename, Ehealth, Eattack, Especial, Echance, Edefence):
        self.name = Ename
        self.health = Ehealth
        self.attack = Eattack
        self.luck = Especial
        self.ranged = Echance
        self.defence = Edefence

        # we're gonna get setters and getters

    # These are getters, where we can check the health or attack of the character
    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getSpecial(self):
        return self.special

    def getChance(self):
        return self.Chance

    def getDefence(self):
        return self.defence

        # setters is what we can use to change a variable

    # for example if we want to set a new attack value
    def setHealth(self, newHealth):
        self.health = newHealth

    def setAttack(self, newAttack):
        self.attack = newAttack

    def setSpecial(self, newSpecial):
        self.luck = newSpecial

    def setChance(self, newChance):
        self.ranged = newChance

    def setDefence(self, newDefence):
        self.defence = newDefence


class Boss(Enemy):
    def __init__(self, Ename, Ehealth, Eattack, Especial, Echance, Edefence, BsuperMove):
        # in order to actually inherit the Enemy class we need to use the super method
        super().__init__(Ename, Ehealth, Eattack, Especial, Echance, Edefence)
        self.superMove = BsuperMove


# a = Hero(100, 1, 1, 1, 1, 1, '존')
# b = Boss(1, 2, 3, 4, 5, 6, 1)
# print(a.name)
# print(b.superMove)

print("스파르블로2 레저렉션에 오신 여러분 환영합니다")
print("이 게임은 한명의 용사가 3마리의 고블린 가족을 처치하는 것이 목적인 게임입니다!")
print("다만 게임을 새로 실행할때마다 적과 용사의 능력이 랜덤으로 설정되니 주의하세요!")
print("선량한 고블린 가족을 처치하고 특별한 보상을 받으러 GoGo!")

# class Hero:
#     def __init__(self, Hhealth, Hattack, Hluck, Hdefence, Hmagic, Hname):

Hname = input("용사의 이름을 무엇으로 하시겠습니까?:")
Hhealth = random.randrange(0,100)
Hattack = random.randrange(0,50)
Hluck = random.randrange(0,10)
Hdefence = random.randrange(0,50)
Hmagic = random.randrange(0,30)

input("hero") = Hero(Hhealth, Hattack, Hluck, Hdefence, Hmagic, Hname)

print(hero.getName())
