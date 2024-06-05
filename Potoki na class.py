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
        days = 90 // self.skill
        enemies = 90
        battle(self, days, enemies)


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Все битвы закончились!")