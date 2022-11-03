import neopixel
import board
import time
import pwmio
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.03, auto_write=False, pixel_order=neopixel.GRB)

# motorAIN1 = DigitalInOut(board.IO36)
# motorAIN2 = DigitalInOut(board.IO38)
# motorBIN1 = DigitalInOut(board.IO35)
# motorBIN2 = DigitalInOut(board.IO37)

# motorAIN1.direction = Direction.OUTPUT
# motorAIN2.direction = Direction.OUTPUT
# motorBIN1.direction = Direction.OUTPUT
# motorBIN2.direction = Direction.OUTPUT

# Attribution PIN capteur infraRouge #
obstacleCMD = DigitalInOut(board.IO33)
obstacleCMD.direction = Direction.OUTPUT

#Attribution bouton Start #
boutonStart = DigitalInOut(board.IO14)
boutonStart.direction = Direction.OUTPUT

# Attribution par capteurs #
obstacleInput = [AnalogIn(board.IO4), #Gauche
                 AnalogIn(board.IO5), #Centre
                 AnalogIn(board.IO6), #Droite
                 AnalogIn(board.IO7)] #Derriere

# Attribution capteur sous robot (suiveur de ligne) #
lineSensor1 = AnalogIn(board.IO8)
lineSensor2 = AnalogIn(board.IO9)
lineSensor3 = AnalogIn(board.IO10)
lineSensor4 = AnalogIn(board.IO11)
lineSensor5 = AnalogIn(board.IO12)


motorAIN1 = pwmio.PWMOut(board.IO36, frequency = 50)
motorAIN2 = pwmio.PWMOut(board.IO38, frequency = 50)
motorBIN1 = pwmio.PWMOut(board.IO35, frequency = 50)
motorBIN2 = pwmio.PWMOut(board.IO37, frequency = 50)

minduty_cyclePWM = 0
maxduty_cyclePWM = 65535
"""
Si le moteur A et B (1 plus lent que l'autre) inverser si c'est l'inverse des moteurs
POUR AVANCER LE ROBOT DROIT STRICTEMENT
maxduty_cyclePWM_Gauche = 65535 #Gauche
maxduty_cyclePWM_Droit = 60000 #Droit
"""

ValeurMinPWM = 0
ValeurMaxPWM = 100


#Moteur droit recule
# motorAIN1.value = True
# motorAIN2.value = False

# #Moteur gauche recule
# motorBIN1.value = True
# motorBIN2.value = False

#AIN1 = pwmio.PWMOut(board.IO36, frequency = 5000, duty_cycle = 0)


def avancer():
    motorAIN1.duty_cycle = minduty_cyclePWM
    motorAIN2.duty_cycle = maxduty_cyclePWM
    motorBIN1.duty_cycle = minduty_cyclePWM
    motorBIN2.duty_cycle = maxduty_cyclePWM
    
def reculer():
    motorAIN1.duty_cycle = maxduty_cyclePWM
    motorAIN2.duty_cycle = minduty_cyclePWM
    motorBIN1.duty_cycle = maxduty_cyclePWM
    motorBIN2.duty_cycle = minduty_cyclePWM
    
def droite():
    motorAIN1.duty_cycle = maxduty_cyclePWM
    motorAIN2.duty_cycle = minduty_cyclePWM
    motorBIN1.duty_cycle = minduty_cyclePWM
    motorBIN2.duty_cycle = maxduty_cyclePWM
    
def gauche():
    motorAIN1.duty_cycle = minduty_cyclePWM
    motorAIN2.duty_cycle = maxduty_cyclePWM
    motorBIN1.duty_cycle = maxduty_cyclePWM
    motorBIN2.duty_cycle = minduty_cyclePWM
    
def motorStop():
    motorAIN1.duty_cycle = minduty_cyclePWM
    motorAIN2.duty_cycle = minduty_cyclePWM
    motorBIN1.duty_cycle = minduty_cyclePWM
    motorBIN2.duty_cycle = minduty_cyclePWM
    
def mapping(valeurEntree): #rajouter maxduty_cyclePWM pour avancer droit strictement
    valeurSortie = ((valeurEntree / ValeurMaxPWM) * maxduty_cyclePWM)
    return (int(valeurSortie))

def vitesseMoteur(positionMoteur, vitesseDemandee, sensDemande):
    #moteur1 gauche
    #moteur2 droite
    #vitesse entre 0 et 100
    #sens Avancer 0
    #sens reculer 1
    
    vitessePWM = mapping(vitesseDemandee) #rajouter en param maxduty_cyclePWM_Gauche ou Droit pour avancer droit strictement
    
    """
    if positionMoteur == 1 and sensDemandee == 0:
        motorAIN1.duty_cycle = vitessePWM
        motorAIN2.duty_cycle = 0
        
    elif positionMoteur == 2 and sensDemandee == 0:
        motorBIN1.duty_cycle = vitessePWM
        motorBIN2.duty_cycle = 0
        
    elif positionMoteur == 1 and sensDemandee == 1:
        motorAIN1.duty_cycle = 0
        motorAIN2.duty_cycle = vitessePWM
        
    elif positionMoteur == 2 and sensDemandee == 1:
        motorAIN1.duty_cycle = 0
        motorAIN2.duty_cycle = vitessePWM
    """
    
    if positionMoteur == 'Gauche':
        if sensDemande == 'Avance':
            motorBIN1.duty_cycle = minduty_cyclePWM
            motorBIN2.duty_cycle = mapping(vitesseDemandee) #rajouter en param maxduty_cyclePWM_Gauche pour avancer droit strictement
        elif sensDemande == 'Recule':
            motorBIN1.duty_cycle = mapping(vitesseDemandee) #rajouter en param maxduty_cyclePWM_Gauche pour avancer droit strictement
            motorBIN2.duty_cycle = minduty_cyclePWM
        else :
            motorStop()
    
    elif positionMoteur == 'Droite':
        if sensDemande == 'Avance':
            motorAIN1.duty_cycle = minduty_cyclePWM
            motorAIN2.duty_cycle = mapping(vitesseDemandee) #rajouter en param maxduty_cyclePWM_Droit pour avancer droit strictement
        elif sensDemande == 'Recule':
            motorAIN1.duty_cycle = mapping(vitesseDemandee) #rajouter en param maxduty_cyclePWM_Droit pour avancer droit strictement
            motorAIN2.duty_cycle = minduty_cyclePWM
        else :
            motorStop()
    
    else :
        motorStop()
            
    return()
    
"""
def esquiveCentre(val1):
    
    if obstacle > val1:
        motorStop()
        time.sleep(0.15)
        gauche()
        time.sleep(0.15)
        
def esquiveDerriere(val1):
    
    if obstacleDerriere.value > val1:
        motorStop()
        time.sleep(0.15)
   
    return()
"""

# Fonction de détection d'obstacle #
def obstacle(obstaclePosition): #(obstacleCentre):
    
    obstaclePosition = obstaclePosition
    
    ledAmbient = 0
    ledObstacle = 0
    diff = 0
    
    # Mesure de la luminosite ambiante
    obstacleCMD.value = False
#     time.sleep(0.2) 
    ledAmbient = obstacleInput[obstaclePosition].value
    print('Valeur-1 capteur : ', obstacleInput[obstaclePosition].value)
    
    # Mesure des IR
    obstacleCMD.value = True
#     time.sleep(0.2)
    ledObstacle = obstacleInput[obstaclePosition].value
    print('Valeur-2 capteur : ', obstacleInput[obstaclePosition].value)
    
    diff = ledObstacle - ledAmbient
#     print('Difference : ', diff)
    
    return(diff)

def timeStart():
    pixels[0] = (255,255,0)
    pixels.show()
    time.sleep(1)
    pixels[0] = (255,0,0)
    pixels.show()
    time.sleep(1)
    pixels[0] = (255,0,255)
    pixels.show()
    time.sleep(1)
    pixels[0] = (0,255,0)
    pixels.show()
    time.sleep(1)
    pixels[0] = (0,255,255)
    pixels.show()
    time.sleep(1)