HP=100
eHP=100
def fight(HP, eHP):
    import random
    N=1
    while HP > 0 and eHP > 0:
        print('Номер хода:', N)
        roll = random.randint(-2, 10)
        if roll >= 1:
                damage = random.randint(0, 20)
                eHP = eHP - damage
                if eHP > 0:
                    print("У врага осталось ", eHP, " ХП")
                else:
                    eHP=0
                    print("У врага не осталось ХП ")
        else:
                print("Ты промахнулся")
        if eHP > 0:
            eroll= random.randint(-2, 10)
            if eroll >= 1:
                    edamage = random.randint(0, 20)
                    HP = HP - edamage
                    if HP > 0:
                        print("У тебя осталось ", HP, " ХП")
                    else:
                        print("У тебя не осталось ХП")
            else:
                    print("Враг промахнулся")
        else:
            break
        N=N+1
    if HP <= 0:
        print('Ты погиб')
    if eHP <= 0:
        print('Враг погиб')
    return HP
fight(HP, eHP)
