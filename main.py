import random
import functions
import matplotlib.pyplot as plt

cassaIniziale = float(input('inserisci il denaro nel conto: '))
guadagno = float(input('inserisci la cifra massima di guadagno: '))
puntataMin = float(input('inserisci la puntata minima: '))

anno = 365
puntataMax = 0
giorniMax = anno*10
cassa = cassaIniziale
andamento = []

def giornata():
    global puntataMax
    global giorniMax
    global cassa
    global puntataMin
    global andamento
    
    positivo = 0

    while positivo < guadagno:
        vittoria = False
        puntata = puntataMin
        while vittoria == False:
            if puntata > cassa: return -1
            cassa = cassa - puntata
            
            estratto = functions.estrazione()
            if estratto != 0 and estratto%2 == 0:
                vittoria = True
                cassa = cassa + puntata*2
                positivo += puntataMin
            else:
                puntata = puntata*2
                if puntata > puntataMax: puntataMax = puntata
    
            
giorni = 0;

while giornata() != -1: #or giorni < giorniMax:
    giorni += 1
    andamento.append(cassa)
giorniMax = giorni

x = [item for item in range(0, giorniMax)]

if cassa < cassaIniziale:
    print('hai perso dopo ' + str(giorni) + ' giorni, la puntata massima è stata: ' + str(puntataMax))
else:
    print('hai guadagnato ' + str(cassa - cassaIniziale) + ' in' + str(giorni) + ' giorni')

plt.plot(x,andamento)
plt.show()




