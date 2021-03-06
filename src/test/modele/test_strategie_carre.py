from threading import Thread

try:
    from controller.wrapper import Wrapper
    from view.affichage import Affichage
    from utils.tools import Point
    from model.arene import Arene
    from model.robot import Robot
    from controller.controleur import Controleur
    from controller.strategies import Carre, Unitaire

except ImportError:
    from pathlib import Path
    import sys

    root_dir = Path(__file__).parent.parent.parent.absolute()
    sys.path.insert(0, str(root_dir))

    from controller.wrapper import Wrapper
    from view.affichage import Affichage
    from utils.tools import Point
    from model.arene import Arene
    from model.robot import Robot
    from controller.controleur import Controleur
    from controller.strategies import Carre, Unitaire


arene = Arene()
centre = Point(500, 500)

robot = Robot(centre, arene)
arene.set_robot(robot)

robot.servo_rotate(90)

affichage = Affichage(arene)
controleur = Controleur()

robot = Wrapper(robot)


def f(): return robot.get_distance() < 50


carre = Unitaire(Carre(robot, 100, 300, 0, 50), f)

controleur.add_strategie(carre)
controleur.select_strategie(0)

FPS = 60.

thread_controleur = Thread(target=controleur.boucle, args=(FPS,))
thread_modele = Thread(target=arene.boucle, args=(FPS,))
thread_affichage = Thread(target=affichage.boucle, args=(FPS,))

thread_controleur.start()
thread_modele.start()
thread_affichage.start()
