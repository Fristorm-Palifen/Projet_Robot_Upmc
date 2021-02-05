from Vision import Vision
from Static import Static
from Wall import Wall

#test le fonctionnement de la vision
def testAdd_Objet(vision):
    #ajoute des Wall aux à certaines positions
    print(Static.add_Objet(vision.grille,Wall(),2,3))
    print(Static.add_Objet(vision.grille,Wall(),2,3))
    print(Static.add_Objet(vision.grille,Wall(),3,2))


if __name__ == '__main__':
    v = Vision(10, 10) #grille de 10*10
    try:
        #essaye de
        testAdd_Objet(v) # ajouter les murs
        Static.affiche(v.grille) #affiche la vision
        print("\nTest: Add Objet successful")

    except AssertionError as e:
        print(e)
