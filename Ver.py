# Code Writing by Mohamed Amine Guedria
# Guedria.amine@gmail.com
# This code communicates with Arduino and switches the wanted pins on (or off) 
# Pegeleinstellung manuell / automatisch
# Überarbeitung Bernhard Lau -01


import serial
import time
import statistics as S


class AR(object):





    def leise(self): # Pegel für beide Lautsprecher auf Stufe 1

        ArduinoSerial = serial.Serial('COM3', 115200, timeout=.1)  # open the port 3 to communicate with Arduino
        time.sleep(2)
        ArduinoSerial.write(b'D')
        time.sleep(1)



# ---------------------------------------------------------------------------------------- Ende leise

    def manuVerstarken(re, ton):  # Pegeleinstellung manuell

        ArduinoSerial = serial.Serial('COM3', 115200, timeout=.1)  # open the port 3 to communicate with Arduino
        time.sleep(2)



         # check the Resistance and switch on or off the suitable pin
        if (ton == 5):  # Tieftöner

                if (re == 1):
                    ArduinoSerial.write(b'A')  # Tieftöner Pegelstufe 4 send to Arduino
                    time.sleep(1)

                elif (re == 2):
                    ArduinoSerial.write(b'B')  # Tieftöner Pegelstufe 3 send to Arduino
                    time.sleep(1)

                elif (re == 3):
                    ArduinoSerial.write(b'C')  # Tieftöner Pegelstufe 2 send to Arduino
                    time.sleep(1)

                elif (re == 7):
                    ArduinoSerial.write(b'E')  # Tieftöner Pegelstufe 5 send to Arduino
                    time.sleep(1)

                else:  # für re == 4
                    ArduinoSerial.write(b'D')  # Tieftöner Pegelstufe 1 send to Arduino
                    time.sleep(1)  # Ende Tieftöner

        elif ton == 6:  # Hochtöner

                if (re == 1):
                    ArduinoSerial.write(b'a')  # Hochtöner Pegelstufe 4 send to Arduino
                    time.sleep(1)

                elif (re == 2):
                    ArduinoSerial.write(b'b')  # Hochtöner Pegelstufe 3 end to Arduino
                    time.sleep(1)

                elif (re == 3):
                    ArduinoSerial.write(b'c')  # Hochtöner Pegelstufe 2 send to Arduino
                    time.sleep(1)

                elif (re == 7):
                    ArduinoSerial.write(b'e')  # Hochtöner Pegelstufe 5 send to Arduino
                    time.sleep(1)

                else:  # für re == 4
                    ArduinoSerial.write(b'd')  # Hochtöner Pegelstufe 1 send to Arduino
                    time.sleep(1)  # Ende Hochtöner





        print("Arduino=", ArduinoSerial.readlines())
# ---------------------------------------------------------------------------- Ende manuVerstarken

    def autoVerstarken(f):  # Pegeleinstellung automatisch

        ArduinoSerial = serial.Serial('COM3', 115200, timeout=.1)  # open the port 3 to communicate with Arduino
        time.sleep(2)

        # check the frequency and switch on or off the suitable pin
        if (19 < f and f < 35):
            ArduinoSerial.write(b'0')  # send to Arduino

            time.sleep(1)

        elif (36 < f and f < 75):
            ArduinoSerial.write(b'1')  # send to Arduino
            time.sleep(1)

        elif (76 < f and f < 150):
            ArduinoSerial.write(b'2')  # send to Arduino
            time.sleep(1)

        elif (151 < f and f < 250):
            ArduinoSerial.write(b'3')  # send to Arduino
            time.sleep(1)

        elif (251 < f and f < 350):
            ArduinoSerial.write(b'4')  # send to Arduino
            time.sleep(1)


        elif (351 < f and f < 450):

            ArduinoSerial.write(b'5')  # send to Arduino
            time.sleep(1)

        elif (451 < f and f < 550):

            ArduinoSerial.write(b'6')  # send to Arduino
            time.sleep(1)

        elif (551 < f and f < 1250):
            print("je suis la 1000")
            ArduinoSerial.write(b'7')  # send to Arduino
            time.sleep(1)

        elif (1251 < f and f < 1750):
            print("je suis 1500")
            ArduinoSerial.write(b'8')  # send to Arduino
            time.sleep(1)

        elif (1751 < f and f < 2250):
            ArduinoSerial.write(b'9')  # send to Arduino
            time.sleep(1)

        elif (2251 < f and f < 2750):
            ArduinoSerial.write(b'x')  # send to Arduino
            time.sleep(1)

        elif (2751 < f and f < 3001):
            ArduinoSerial.write(b'y')  # send to Arduino
            time.sleep(1)

        else:
            print("!!!!!!!!!! you are out of the range(20-3000 hz) !!!!!!!")

        print("Arduino=", ArduinoSerial.readline())
# ---------------------------------------------------------------------------- Ende autoVerstarken


    def autoVer(c,c2,v,ton):  # Pegeleinstellung automatisch


        ArduinoSerial = serial.Serial('COM3', 115200, timeout=.1)  # open the port 3 to communicate with Arduino
        time.sleep(2)
        maxval=0.1

        listtief = [b'D', b'C', b'B', b'A', b'E']
        listhoch = [b'd', b'c', b'b', b'a', b'e']



        if (ton == 5):
            if len(v) > 0:
                Val = S.median(v)
                if Val < maxval / 100:

                    ArduinoSerial.write(listtief[c])  # Tieftöner Pegelstufe  send to Arduino
                    print("Send -----------------------> ",c,"---",listtief[c])
                    time.sleep(1)



        elif ton == 6:  # Hochtöner

            if len(v) > 0:
                Val = S.median(v)
                if Val < maxval / 100:

                    ArduinoSerial.write(listtief[c2])  # Tieftöner Pegelstufe  send to Arduino
                    time.sleep(1)



