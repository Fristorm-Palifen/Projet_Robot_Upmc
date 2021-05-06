import os

try:
    import cv2
except:
    os.system("bash ./install.sh")

from threading import Thread
from utils.config import Config
from controller.controleur import Controleur
from controller.strategies import SuivreBalise
from controller.wrapper import Wrapper

controleur = Controleur()

# protection du config
config = Config()

mode = config.get_mode()

FPS = config.get_fps()

if (mode):  # Mode Simu
    print("Simu on")

    from view.affichage import Affichage
    from model.robot import Robot
    from model.arene import Arene
    from utils.tools import Point
    from model.obstacles import Balise

    import random
    from datetime import datetime
    random.seed(datetime.now())

    arene = Arene()

    balise = Balise(Point(280, 300), Point(380, 400))
    arene.set_balise(balise)

    robot = Robot(Point(230, 300), arene)
    robot.down()
    arene.set_robot(robot)

    affichage = Affichage(arene)

    wrapper = Wrapper(robot)
    strat = SuivreBalise(wrapper, 300)

    controleur.add_startegie(strat)
    controleur.select_startegie(0)

    thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
    thread_modele = Thread(target=arene.boucle, args=(FPS,))
    thread_affichage = Thread(target=affichage.boucle, args=(FPS,))

    thread_controleur.start()
    thread_modele.start()
    thread_affichage.start()

    try:
        while True:
            continue
    except:
        print("Fin de l'execution")
        controleur.stop()
        arene.stop()
        affichage.stop()


else:  # mode REEL
    print("simu off")

    try:
        from robot2I013 import Robot2I013
        robot = Robot2I013()
    except ImportError:
        from irl.mockup import Robot2I013Mockup
        robot = Robot2I013Mockup()

    wrapper = Wrapper(robot)
    strat = SuivreBalise(wrapper, 300)

    controleur.add_startegie(strat)
    controleur.select_startegie(0)

    thread_controleur = Thread(target=controleur.boucle, args=(FPS,))

    thread_controleur.start()

    try:
        while True:
            continue
    except:
        print("Fin de l'execution")
        controleur.stop()
