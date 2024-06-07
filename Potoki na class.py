# Напишите программу с использованием механизмов многопоточности, которая создает два потока-рыцаря.
# Каждый рыцарь должен иметь имя (name) и умение(skill). Умение рыцаря определяет, сколько времени потребуется рыцарю,
# чтобы выполнить свою защитную миссию для королевства.
# Враги будут нападать в количестве 100 человек. Каждый день рыцарь может ослабить вражеское войско на skill-человек.
# Если у рыцаря skill равен 20, то защищать крепость он будет 5 дней (5 секунд в программе).
# Чем выше умение, тем быстрее рыцарь защитит королевство.
import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, skill):
        threading.Thread.__init__(self)
        self.name = name
        self.skill = skill

    def run(self):
        days = 100 // self.skill
        enemies = 100
        battle(self)


def battle(knight):
    enemies = 100
    print(f"{knight.name}, на нас напали!")
    days = 0
    while enemies > 0:
        days += 1
        enemies -= knight.skill
        remaining_enemies = max(enemies, 0)
        print(f"{knight.name}, сражается {days} день(дня)..., осталось {remaining_enemies} воинов.")
        if remaining_enemies == 0:
            print(f"{knight.name} одержал победу спустя {days} {'день' if days == 1 else 'дней'}!")
        time.sleep(1)
    if enemies > 0:
        print("Битва закончилась!")


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Все битвы закончились!")

# def battle(knight):
#     enemies = 100
#     print(f"{knight.name}, на нас напали!")
#     days = 0
#     while enemies > 0:
#         days += 1
#         enemies -= knight.skill
#         remaining_enemies = max(enemies, 0)
#         print(f"{knight.name}, сражается {days} день(дня)..., осталось {remaining_enemies} воинов.")
#         if remaining_enemies == 0:
#             print(f"{knight.name} одержал победу спустя {days} {'день' if days == 1 else 'дней'}!")
#         time.sleep(1)
#     if enemies > 0:
#         print("Битва закончилась!")


