import board
import time
import elio

while elio.boutonStart.value == True:
    print(elio.boutonStart.value)

# Décompte de 5secondes avant le départ
elio.timeStart()

while True:

    # Si le robot capte par l'intermédiaire de capteurs sous le robot 
    if (elio.lineSensor1.value and elio.lineSensor2.value and elio.lineSensor3.value and elio.lineSensor4.value and elio.lineSensor5.value) > 50000 : # and elio.lineSensor1.value > 50000 and elio.lineSensor1.value > 50000 and elio.lineSensor1.value > 50000 and elio.lineSensor1.value > 50000 :
        
        elio.pixels[0] = (0,255,0)
        elio.pixels.show()
        elio.vitesseMoteur('Droite', 100, 'Recule')
        elio.vitesseMoteur('Gauche', 100, 'Recule')
        time.sleep(0.2)
        elio.vitesseMoteur('Droite', 100, 'Avance')
        elio.vitesseMoteur('Gauche', 100, 'Recule')
        time.sleep(0.32)

    print(elio.lineSensor1.value, elio.lineSensor2.value, elio.lineSensor3.value, elio.lineSensor4.value, elio.lineSensor5.value)

    # Si le robot capte un obstacle à moins de la valeur X
    # Alors pour chaque obstacle devant chaque capteur (plusieurs cas)
    if elio.obstacle(1) > 200: #Centre
        
        elio.pixels[0] = (0, 0, 255)
        elio.pixels.show()
        elio.vitesseMoteur('Droite', 100, 'Avance')
        elio.vitesseMoteur('Gauche', 100, 'Avance')

    elif elio.obstacle(0) > 600: #Gauche
        
        elio.pixels[0] = (240, 195, 0)
        elio.pixels.show()
        elio.vitesseMoteur('Droite', 100, 'Avance')
        elio.vitesseMoteur('Gauche', 100, 'Avance')
         
    elif elio.obstacle(2) > 600: #Droit

        elio.pixels[0] = (108, 2, 119)
        elio.pixels.show()
        elio.vitesseMoteur('Droite', 100, 'Avance')
        elio.vitesseMoteur('Gauche', 100, 'Avance')

    elif elio.obstacle(3) > 1000: #Derriere

        elio.pixels[0] = (0, 255, 255)
        elio.pixels.show()
        elio.vitesseMoteur('Droite', 100, 'Recule')
        elio.vitesseMoteur('Gauche', 100, 'Recule')

    # Sinon si le robot ne capte rien sur tous ses capteurs latéraux à moins de la valeur X, alors il tourne en rond dès le début
    else:
        
        elio.obstacleCMD.value = True
       
        if elio.obstacle(1) < 1000:
            
            elio.pixels[0] = (255, 0, 0)
            elio.pixels.show()
            elio.vitesseMoteur('Droite', 40, 'Recule')
            elio.vitesseMoteur('Gauche', 40, 'Avance')