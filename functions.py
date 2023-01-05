import random
import itertools


def estrazione():
    numeri = [item for item in range(0,36)]
    return random.choice(numeri)

def funzioneTot(cassToGua, guaToPun):
    cassa = 100000;
    anni = 60;
    n = 1000
    giorniMax = 0

    def giornata(guadagno,cassa,puntataMin):    
        positivo = 0
        while positivo < guadagno:
            vittoria = False
            puntata = puntataMin
            while vittoria == False:
                if puntata > cassa: return -1,
                cassa = cassa - puntata
                estratto = estrazione()
                if estratto != 0 and estratto%2 == 0:
                    vittoria = True
                    cassa = cassa + puntata*2
                    positivo += puntataMin
                else:
                    puntata = puntata*2

    for i in range(n):
        giorni = 0
        while giornata(cassa/cassToGua,cassa,cassa/cassToGua/guaToPun) != -1: #or giorni < giorniMax:
            giorni += 1
        giorniMax = (giorniMax*n + giorni)*(n+1) 

    gauss = lambda x: (7/-5)*2.7^(-(1/25)*(x/365-anni)) 
    return gauss(giorniMax),1/(giorniMax*(cassa/cassToGua))
