# Напишите программу с использованием механизмов многопоточности, которая создает два потока-рыцаря.
# Каждый рыцарь должен иметь имя (name) и умение(skill). Умение рыцаря определяет, сколько времени потребуется рыцарю,
# чтобы выполнить свою защитную миссию для королевства.
# Враги будут нападать в количестве 100 человек. Каждый день рыцарь может ослабить вражеское войско на skill-человек.
# Если у рыцаря skill равен 20, то защищать крепость он будет 5 дней (5 секунд в программе).
# Чем выше умение, тем быстрее рыцарь защитит королевство.
import threading
import time


def battle(knight, days, enemies):
    print(f"{knight.name}, на нас напали!")
    for day in range(1, days + 1):
        print(f"{knight.name}, сражается {day} день(дня)..., осталось {enemies} воинов.")
        enemies -= knight.skill
        if enemies <= 0:
            print(f"{knight.name} одержал победу спустя {day} {'день' if day == 1 else 'дней'}!")
            break
        time.sleep(1)
    else:
        print("Битва закончилась!")


class Knight(threading.Thread):
    def __init__(self, name, skill):
        threading.Thread.__init__(self)
        self.name = name
        self.skill = skill

    def run(self):
        days = 100 // self.skill
        enemies = 100
        battle(self, days, enemies)


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Все битвы закончились!")