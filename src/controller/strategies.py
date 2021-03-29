from math import pi
from abc import abstractmethod


class Strategie:

    def __init__(self, robot):
        self.robot = robot
        self.is_stop = False
        self.is_start = False

    def start(self):
        self.is_stop = False
        self.is_start = True

    def stop(self):
        self.is_stop = True
        self.is_start = False

    @abstractmethod
    def run(self):
        pass


class Avancer(Strategie):

    def __init__(self, robot, distance, vitesse):

        super().__init__(robot)
        self.distance = distance
        self.distance_parcouru = 0
        self.vitesse = vitesse

    def start(self):
        super().start()
        self.robot.offset_motor_encoder(
            self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, 0)
        self.robot.set_motor_dps(
            self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, 0)

    def run(self):

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        diff = self.robot.get_motor_position()[0]

        k = diff // 360
        r = diff % 360

        print(self.distance_parcouru)
        self.distance_parcouru += k * pi * self.robot.WHEEL_DIAMETER + \
            (r * pi * self.robot.WHEEL_DIAMETER) / 360

        # print(self.distance_parcouru)
        if self.distance_parcouru >= self.distance or self.robot.vision.check_collisions():
            self.robot.stop()
            self.stop()
            print("Arret de avancer")
            return

        self.robot.set_motor_dps(
            self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, self.vitesse)


class Tourner(Strategie):

    def __init__(self, robot, angle, orientation):
        super().__init__(robot)
        self.angle = angle
        self.angle_parcouru = 0
        self.orientation = orientation

    def start(self):
        super().start()
        self.robot.offset_motor_encoder(
            self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, 0)

        if self.orientation == 0:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,  0)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, self.angle)
        else:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,  self.angle)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, 0)

    def run(self):

        if self.is_stop:
            return

        if not self.is_start:
            self.start()

        # Calcule de l'angle_parcouru

        if self.robot.vision.check_collisions():
            self.robot.stop()
            self.stop()
            print("Arret de tourner")
            return

        if self.orientation == 0:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,  0)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, self.angle)
        else:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,  self.angle)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, 0)


"""
class Carre(Strategie):

    def __init__(...):
        self.avancer = Avancer()
        self.tourner = Tourner()
        self.cur = 0
        self.nb = 0 

    def run

    if self.is_stop:
        return

    if nb == NB_arret
        self.stop()
        retunt

    id self.cur = 0 
    ---> a

    else --->


    cur <-> switch
"""
