# on rajoute random
import pyxel, random

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(300, 300, title="Josh")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 125
vaisseau_y = 250
color=6
colorb = 10
score= 0
cox = 50
coy = 100
r=3
x= vaisseau_x + 25
y= vaisseau_y - (r+1)
balle = False
vb = score/4+5
xx=-vb
yy=-vb
velocity = 5

# vies et score
vies = 3
score= 0


# initialisation des ennemis
brique_liste = []
rang = [r for r in range(0,61,20)]
placement  = [p for p in range(40,221,40)]


def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 240) :
            x = x + velocity
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > -20) :
            x = x - velocity

    return x, y


def balle_deplacement():
    global x, y, xx, yy, vies, balle , score
    x += xx
    y += yy
    
    # Bord gauche
    if x <= r:
        xx = -xx
    # Plafond
    elif y <= r :
        yy = -yy
    # bord droit
    elif x >= 300-r :
        xx = -xx
    # dessus raquette
    elif y >= vaisseau_y-r and y <= vaisseau_y+r and x >= vaisseau_x-r and x <= vaisseau_x+50+r :
        yy = -yy
        score+=10
    # raquette gauche
    elif x >= vaisseau_x-50-r and x <= vaisseau_x+r and y >= vaisseau_y - r and y <= vaisseau_y + 20 - r and pyxel.pget(x+xx, y+yy) == 2 :
        yy = -yy
        score+=20
    # raquette droite
    elif x >= vaisseau_x+50-r and x <= vaisseau_x+100+r and y >= vaisseau_y - r and y <= vaisseau_y + 20 - r and pyxel.pget(x+xx, y+yy) == 2 :
        yy = -yy
        score+=30
    # bas
    elif y >= 300+r :
        balle=False
        xx=-vb
        yy=-vb
        vies = vies-1
        pyxel.text(vaisseau_x,vaisseau_y+10, 'Une vie de moins !', 7)
    # brique 
    elif pyxel.pget(x+xx, y+yy) == 10 :
            yy = -yy
            pyxel.fill(x+xx, y+yy, 9 )
    elif pyxel.pget(x+xx, y+yy) == 9 :
            yy = -yy
            pyxel.fill(x+xx, y+yy, 8 )
    elif pyxel.pget(x+xx, y+yy) == 8 :
            yy = -yy
            pyxel.fill(x+xx, y+yy, 0 )
            score += 20
        
   
        
        
        
def brique_creation(ennemis_liste):
    """création aléatoire des ennemis"""

    # un ennemi par seconde
    for i in rang :
        for a in placement :
            ennemis_liste.append([random.randint(40, 221), 10+i])
    return ennemis_liste





def brique_suppression():
    """disparition d'un ennemi et d'un tir si contact"""

    #for ennemi in ennemis_liste:
        #for tir in tirs_liste:
            #if ennemi[0] <= tir[0]+1 and ennemi[0]+8 >= tir[0] and ennemi[1]+8 >= tir[1]:
                #ennemis_liste.remove(ennemi)
                

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, x, y, balle, brique_liste, vies

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    
    if pyxel.btnr(pyxel.KEY_SPACE):
        balle = True

    if balle is False:
        x = vaisseau_x + 25
        y = vaisseau_y - (r+1)
    else:
        balle_deplacement()

    # creation des ennemis
    brique_liste = brique_creation(brique_liste)


    # suppression des ennemis et tirs si contact
    brique_suppression()

    # suppression du vaisseau et ennemi si contact
    

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # si le vaisseau possede des vies le jeu continue
    if vies > 0:    
        global cox, coy
        # vaisseau 
        pyxel.rect(vaisseau_x, vaisseau_y, 50, 20, 2)
        pyxel.tri(vaisseau_x, vaisseau_y, vaisseau_x, vaisseau_y+20, vaisseau_x-50,vaisseau_y+20,2) 
        pyxel.tri(vaisseau_x+50, vaisseau_y, vaisseau_x+50, vaisseau_y+20, vaisseau_x+100,vaisseau_y+20,2) 
        pyxel.rect(vaisseau_x-50, vaisseau_y+20, 150, 5, 2)

        # tirs
        pyxel.circ(x,y,r,color)
        
        pyxel.text(250,10, 'Score: %d' % score, 7)

        pyxel.text(250,20, 'Vies: %d' % vies, 7)

        # briques
        #for brique in brique_liste:
        #for u in range(8) :
            #pyxel.rect(cox,coy, 20, 10, colorb)
            #cox += 25
            
    # sinon: GAME OVER
    else:

        pyxel.text(50,64, 'GAME OVER', 7)

pyxel.run(update, draw)