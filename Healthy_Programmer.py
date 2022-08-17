from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()} \n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exeecise = time()
    watersecs = 40*60
    eyessecs = 30*60
    exsecs = 45*60
    print("Welcome to Healthy Programmer...")

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm. ")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            print("Eye Exercise time. Enter 'doneeyes' to stop the alarm. ")
            musiconloop('eye.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exeecise > exsecs:
            print("Physical Activity time. Enter 'donephy' to stop the alarm. ")
            musiconloop('exercise.mp3', 'donephy')
            init_exeecise = time()
            log_now("Physical Activity Done at")