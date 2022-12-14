# on rajoute bibliotheque random
import pyxel, random

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(300, 300, title="Josh")

# position initiale du raquette
# (origine des positions : coin haut gauche)
raquette_x = 125
raquette_y = 250
color=6
score= 0
r=3
x= raquette_x + 25
y= raquette_y - (r+1)
balle = False
vb = 5
xx=-vb
yy=-vb
velocity = 5
briquehauteur = 10
briquelargeur= 20
level = 0



#brique
x1=50
x2=75
x3=100
x4=125
x5=150
x6=175
x7=200
x8=225
x9=65
x10=210
y1=60
y2=100
y3=140
y4=80
y5=120
y6=40
y7=160

brique_liste = [ [[x1, y1, 10], [x2, y1, 10], [x3, y1, 10], [x4, y1, 10], [x5, y1, 10], [x6, y1, 10], [x7, y1, 10], [x8, y1, 10] , \
                 [x1, y2, 9], [x2, y2, 9], [x3, y2, 9], [x4, y2, 9], [x5, y2, 9], [x6, y2, 9], [x7, y2, 9], [x8, y2, 9] , \
                 [x1, y3, 8], [x2, y3, 8], [x3, y3, 8], [x4, y3, 8], [x5, y3, 8], [x6, y3, 8], [x7, y3, 8], [x8, y3, 8]], \
                 
                 [[x1, y1, 8], [x2, y1, 9], [x3, y1, 8], [x4, y1, 10], [x5, y1, 10], [x6, y1, 8], [x7, y1, 9], [x8, y1, 8] , \
                 [x1, y2, 9], [x2, y2, 8], [x3, y2, 9], [x4, y2, 10], [x5, y2, 10], [x6, y2, 9], [x7, y2, 8], [x8, y2, 9] , \
                 [x1, y3, 8], [x2, y3, 9], [x3, y3, 8], [x4, y3, 10], [x5, y3, 10], [x6, y3, 8], [x7, y3, 9], [x8, y3, 8]], \
                 
                 [[x1, y1, 9], [x2, y1, 9], [x3, y1, 9], [x4, y1, 10], [x5, y1, 10], [x6, y1, 9], [x7, y1, 9], [x8, y1, 9] , \
                 [x1, y2, 9], [x2, y2, 9], [x3, y2, 10], [x4, y2, 8], [x5, y2, 8], [x6, y2, 10], [x7, y2, 9], [x8, y2, 9] , \
                 [x1, y3, 9], [x2, y3, 9], [x3, y3, 9], [x4, y3, 10], [x5, y3, 10], [x6, y3, 9], [x7, y3, 9], [x8, y3, 9]] , \
                 
                 [[x1, y2, 9], [x2, y4, 8], [x3, y1, 9], [x4, y6, 8], [x5, y6, 8], [x6, y1, 9], [x7, y4, 8], [x8, y2, 9] , \
                 [x2, y5, 8], [x3, y3, 9], [x4, y7, 8], [x5, y7, 8], [x6, y3, 9], [x7, y5, 8], [x8, y2, 9] ,\
                 [x4, y2, 10], [x4, y4, 10], [x4, y5, 10], [x5, y2, 10], [x5, y5, 10], [x5, y4, 10],] , \
                 
                 [[x9, y2, 8], [x2, y4, 8], [x3, y1, 8],  [x6, y1, 8], [x7, y4, 8], [x10, y2, 8] , \
                 [x2, y5, 8], [x3, y3, 8], [x4, y7, 8], [x5, y7, 8], [x6, y3, 8], [x7, y5, 8], \
                 [x4, y4, 8],[x5, y4, 8],] , \
                 
                 [[x1, y6, 10], [x1, y7, 10], [x8, y7, 10],  [x8, y6, 10], ]]


# vies et score
vies = 5
score= 0

def raquette_deplacement(x, y):
    """d??placement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 240) :
            x = x + velocity
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > -20) :
            x = x - velocity

    return x, y


def balle_deplacement():
    global x, y, xx, yy, vies, balle , score , brique_liste , brique, vb, level, velocity
    x += xx
    y += yy
    # Bord gauche

    if x <= r and xx <0:
        xx = -xx
    # Plafond
    elif y <= r and yy <0:
        yy = -yy
    # bord droit
    elif x >= 300-r and xx >0:
        xx = -xx
    # dessus raquette
    elif y >= raquette_y-r and y <= raquette_y+r+20 and x >= raquette_x-r and x <= raquette_x+50+r and yy > 0:
        yy = -yy
    # raquette gauche
    elif x >= raquette_x-50-r and x <= raquette_x+r and y >= raquette_y - r and y <= raquette_y + 40 - r and pyxel.pget(x+xx, y+yy) == 2 and yy > 0:
        yy = -yy
    # raquette droite
    elif x >= raquette_x+50-r and x <= raquette_x+100+r and y >= raquette_y - r and y <= raquette_y + 40 - r and pyxel.pget(x+xx, y+yy) == 2 and yy > 0 :
        yy = -yy
    # bas
    elif y >= 300+r :
        balle=False
        xx=-abs(xx)
        yy=-abs(yy)
        vies = vies-1
        pyxel.text(100,200, 'Une vie de moins !', 7)

    # brique 
    for brique in brique_liste[level] :
        ch = True
        bx = brique[0]
        by = brique[1]
        if y >= by + briquehauteur - r and y <= by + briquehauteur + r and x >= bx - r and x <= bx + briquelargeur + r \
        or y >= by - r and y <= by + r and x >= bx - r and x <= bx + briquelargeur + r \
        or y >= by - r and y <= by + briquehauteur + r and x >= bx - r + briquelargeur and x <= bx + r + briquelargeur \
        or y >= by - r and y <= by + briquehauteur + r and x >= bx - r and x <= bx + r :
            yy = -yy
            score += 10
            if brique[2] == 8 :
                brique_liste[level].remove(brique)
                if len(brique_liste[level]) % 6 == 0 :
                    if xx < 0: 
                      xx -= 1
                      velocity += 1
                    else: 
                      xx += 1
                      velocity += 1
                    if yy < 0: 
                      yy -= 1
                      velocity += 1
                    else: 
                      yy += 1
                      velocity += 1

                if len(brique_liste[level]) == 0 :
                    level+=1
                    xx= -vb
                    yy= -vb
                    velocity = 5
                    balle= False
            else  :
                if ch == True :
                    brique[2] -= 1
                    ch = False


# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise ?? jour des variables (30 fois par seconde)"""

    global raquette_x, raquette_y, x, y, balle, brique_liste, vies , x0 , y0 , xx , yy, level, velocity

    # mise ?? jour de la position du raquette
    raquette_x, raquette_y = raquette_deplacement(raquette_x, raquette_y)
    
    if pyxel.btnr(pyxel.KEY_SPACE):
        balle = True

    if balle is False:
        x = raquette_x + 25
        y = raquette_y - (r+1) 
    else:
        balle_deplacement()

# =========================================================
# == DRAW
# =========================================================
def draw():
    """cr??ation des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # si le raquette possede des vies le jeu continue
    if level == 6 :
        pyxel.text(150,150, 'VICTOIRE!', 7)

    elif vies > 0:    
        global cox, coy , brique_liste, brique_debut, o
        # raquette 
        pyxel.rect(raquette_x, raquette_y, 50, 20, 2)
        pyxel.tri(raquette_x, raquette_y, raquette_x, raquette_y+20, raquette_x-50,raquette_y+20,2) 
        pyxel.tri(raquette_x+50, raquette_y, raquette_x+50, raquette_y+20, raquette_x+100,raquette_y+20,2) 
        pyxel.rect(raquette_x-50, raquette_y+20, 150, 5, 2)

        #balle
        pyxel.circ(x,y,r,color)
        
        pyxel.text(250,10, 'Score: %d' % score, 7)
        pyxel.text(250,20, 'Vies: %d' % vies, 7)
        pyxel.text(130,10, 'Niveau %d' % (level+1), 7)
        pyxel.text(130,20, 'Vitesse %d' % abs(xx), 7)
        
        if balle == False :
            pyxel.text(40,200, 'Espace pour lancer fleches droite gauche pour deplacer' , 7)
            pyxel.text(40,220, '5 niveaux disponibles !            3 types de briques !' , 10)


        # briques
        for brique in brique_liste[level] :
            pyxel.rect(brique[0],brique[1], briquelargeur, briquehauteur, brique[2])
            
    # sinon: GAME OVER
    else:

        pyxel.text(130,150, 'GAME OVER', 7)

pyxel.run(update, draw)
