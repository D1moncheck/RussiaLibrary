import random

def petya(city):
    msg = random.choice(('Петя копает метеориты в ', 'Петя бьёт крапиву в ', 'Петя открыл бизнес в ', 'Петя вычисляет Васю по айпи в ')) + city
    print(msg)

def vasya(item):
    msg = random.choice(('Вася бежит на медведя с ', 'Вася заводит шоху ', 'Вася взломал дневник.ру ', 'Вася вломил провайдеру ')) + item
    print(msg)

def ded(fish):
    msg = random.choice(('Дед рыбачит на ', 'Дед зажарил ', 'Дед схавал ', 'Дед вырубил ')) + fish
    print(msg)

def babushka():
    msg = random.choice(('Никаких аргументов, бабушка всегда права!', 'От интернетов тупым станешь! - © Бабушка', 'Внучок, как зайти в одноклассники без интернета?', 'Бежимпокупать 50 килограмм гречи!'))
    print(msg)

def gopnik():
    msg = random.choice(('Есть мобила позвонить? - © Гопник', 'Закинь пару соток на баланс по братски - © Гопник', 'Семки есть? - © Гопник', 'Чё ты нам тут затираешь? - © Гопник'))
    print(msg)
