import random
import functions

cassa = input('inserisci il denaro nel conto: ')
guadagno = input('inserisci la cifra massima di guadagno: ')
puntataMin = input('inserisci la puntata minima: ')

anno = 365
positivo = 0
puntataMax = 0

while positivo != guadagno:
    vittoria = False
    puntata = puntataMin
    while vittoria == False:
        if puntata > cassa: break
        cassa = cassa - puntata
        estratto = functions.estrazione()
        if estratto != 0 and estratto%2 == 0:
            vittoria = True
            cassa = cassa + puntata*2
            positivo += puntataMin
        else:
            puntata = puntata*2
            if puntata > puntataMax: puntataMax = puntata
            






