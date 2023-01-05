import random
import itertools

numeri = [item for item in range(0,36)]
def estrazione():
    return random.choice(numeri)

def funzioneTot(cassToGua, guaToPun):


    def giornata():
        global puntataMax
        global giorniMax
        global cassa
        global puntataMin
        global andamento
        global guadagno 

        positivo = 0

        while positivo < guadagno:
            vittoria = False
            puntata = puntataMin
            while vittoria == False:
                if puntata > cassa: return -1
                cassa = cassa - puntata
                
                estratto = estrazione()
                if estratto != 0 and estratto%2 == 0:
                    vittoria = True
                    cassa = cassa + puntata*2
                    positivo += puntataMin
                else:
                    puntata = puntata*2
                    if puntata > puntataMax: puntataMax = puntata

