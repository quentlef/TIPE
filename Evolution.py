import random as rd

class Herbivore:
    type = 'Herbivore'
    def __init__(self, name):
        self.name = ''
        self.etat = 'vivant'
    def change_etat(self, etat):
        self.etat = etat
    def change_nom(self, name):
        self.name = name
        
Liste_Creature = []
C1 = Herbivore('') 
C2 = Herbivore('')
C3 = Herbivore('') 
C4 = Herbivore('') 
C5 = Herbivore('') 
C6 = Herbivore('') 

def initialisationCreature(n):
    Liste_Creature = []
    for i in range(n):
        nom = ("Creature {0}".format(i))
        Liste_Creature.append(nom)
       
    return Liste_Creature






        
    
        
        
def initMap(n):
    L = []
    for i in range(n):
        L.append(n*["Vide"])
    return L

'''
action de manger, la créature gagne un point 
T = Terre: case normal, rien ne se passe 
E = Eau: case de warning, envoie une alerte à la créature 
EM = Eau moyennement profonde, les créatures meurt si elle font moins de 1 m
EP = Eau profonde, les créature meurt dans tous les cas 
H = Herbe, les créature herbivore peuvent s'arrêter sur cette case pour manger 
P = seul les créture avec la compétence escalade peuvent y passer 
'''


def randomMap(Map):
    n = len(Map)
    for i in range(n):
        for j in range(n):
            random = rd.random()
            if 0 <= random <0.20 :
                Map[i][j] = 'T'
            elif 0.20<= random < 0.40 :
                Map[i][j] = 'E'
            elif 0.40 <= random < 0.90:
                Map[i][j] = 'H'
            elif 0.90 <= random <= 1:
                Map[i][j] = 'P'
            else:
                print("marche pas")  
    return Map

def AfficheMap(Map):
    for i in range(len(Map)):
        print(Map[i])

def check_etat():
    return

from tkinter import * 


def affiche():
    Map = randomMap(initMap(10))
    print(Map)
    fenetre = Tk()
    Bgcolour = ""
    p = PanedWindow(fenetre, orient=HORIZONTAL)
    p.pack(side=TOP, expand=Y, fill=BOTH, pady=0, padx=0)
    n = len(Map)
    for i in range(n):
        for j in range(n):
            if Map[i][j] == 'H':
                Bgcolour = 'green'    
            elif Map[i][j] == 'E':
                Bgcolour = 'blue'
            elif Map[i][j] == 'P':
                Bgcolour = 'grey'
            elif Map[i][j] == 'T' :
                Bgcolour = "#A5A52A"
            else:
                Bgcolour = 'red'
                
            p.add(Label(p, text=Map[i][j], background=Bgcolour, anchor=CENTER, relief=RAISED))
    '''    
    p.add(Label(p, text='Volet 2', background=Map[1][2], anchor=CENTER) )
    p.add(Label(p, text='Volet 3', background='red', anchor=CENTER) )
    '''
    p.pack()
    
    fenetre.mainloop()