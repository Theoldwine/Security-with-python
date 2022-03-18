from threading import Thread
import time


def car(speed, driver):
    path = 0
    while path <= 100:

        path += speed
        time.sleep(0.5)
        print('Driver: {} Km/h: {} \n'.format(driver, path))


t_car1 = Thread(target=car, args=[1, 'Ad'])
t_car2 = Thread(target=car, args=[2, "Greg"])

t_car1.start()
t_car2.start()
