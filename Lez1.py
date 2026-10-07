print("ciao")

###variabili iniziali

nome = "Sara"
eta = 67
media = 6.7
promossa = True

###controllo del tipo di una variabile

print(type(nome), type(eta), type(media), type(promossa))
print(f"{nome} ha {eta} anni e una media del {media}")

print(7 / 2)                
print(7 // 2)               ###divide e approssima all'intero
print(7 % 2)                ###da il resto (in questo caso 1)
print(2 ** 10)              ###due elevato alla decima
print(int("42") + 1)        ###il 42 stringa viene convertito in intero
print("42" + "1")           ###due stringe che si concatenano
print(42 + 1)               

###controllo con if ed else

voto = media
if voto >= 6:
    esito = "sufficiente"
elif voto >= 5:
    esito = "insifficiente lieve"
else:
    esito = "insufficiente grave"

print(esito)
print(type(esito))

###breve ciclo for

for i in range(3):
    print(f"giro {i}")

###lavoro su lista

numeri = [6, 7]
for n in numeri:
    print(n*2)

for n in numeri:
    if n == 6:
        print("trovato il numero dell'aura")

for n in numeri:
    if n == 6:
        break               ###termina
        print("trovato il numero dell'aura")

for n in numeri:
    if n == 6:
        continue            ###salta
        print("trovato il numero dell'aura")

###funzione calcolo area rettangolo

def area_rettangolo(base, altezza):
    return base * altezza

print(area_rettangolo(6, 7))

###restituire più di un valore

def dividi(a, b):
    if b == 0:
        return None, "divisione per zero"
    return a // b, "ok"      ###altrimenti

risultato, stato = dividi(67, 7)
print(risultato, stato)      ###i risultati vengono asseganti a due variabili così nominate

risultato, stato = dividi(10, 0)
print(risultato, stato)      ###secondo caso quando b è zero

###return non è print, visualizza qualocsa a schermo e basta

def saluta(nome, saluto="Ciao"):        ###ciao è un valore saluto di default
    return f"{saluto}, {nome}!"

print(saluta("Luca"))                   
print(saluta("Sara", "Buongiorno"))
print(saluta(saluto="Salve", nome="Marco"))

totale = 0.0
for _ in range(10):
    totale += 0.1

print(totale)                           ###darà 0.9999999999999999
print(totale == 1.0)                    ###controlla se il valore totale è 1.0 (false)
print(round(totale, 10) == 1.0)         ###controlla se il valore totale arrotondato è 1.0 (true) - il 10 è il numero di cifre dopo la virgola da mantenere

###Dieci volte 0.1 non fa 1.0. Non è un difetto di Python: è come i numeri con la virgola vengono rappresentati in binario. 
###0.1 in base 2 è periodico, esattamente come 1/3 in base 10: da qualche parte va troncato.

###esercizi aura

###esercizio 1:Scrivi una funzione celsius_a_fahrenheit(gradi) che restituisce i gradi Fahrenheit. La formula è F = C × 9/5 + 32
def celsius_a_fahrenheit(gradi):
    return gradi * 9 / 5 + 32
for celsius in [0, 25, 100]:
    print(f"{celsius}°C corrispondono a {celsius_a_fahrenheit(celsius)}°F")

###esercizio 2:Scrivi e_pari(n) che restituisce True se n è pari. Usa l'operatore %. Poi stampa i numeri pari da 1 a 20 usando la tua funzione
def e_pari(n):
    return n % 2 == 0
for n in range(1, 21):
    if e_pari(n):
        print(n)

###esercizio 3:Scrivi media(voti) che riceve una lista di numeri e restituisce la media. Attenzione al caso della lista vuota: non deve andare in errore.
def media(voti):
    if len(voti)==0:
        return None
    return sum(voti) / len(voti)
    ###esempio
print(media([6, 7, 8]))

###esercizio 4:In una gita ci sono n studenti e ogni pullman porta 53 persone. Scrivi pullman_necessari(n) che restituisce quanti pullman servono. Provala con 53, 54 e 106. Il caso da non sbagliare è il secondo.

def pullman_necessari(n):
    pieni = n // 53
    if n % 53 > 0:
        return pieni + 1
    return pieni
for n in [53, 54, 106]:
    print(f"per {n} studenti presenti sono necessari {pullman_necessari(n)} pullman")

###esercizio 5:Scrivi statistiche(voti) che restituisce tre valori: minimo, massimo e media. Se la lista è vuota, restituisci None, None, None. Chiamala così: minimo, massimo, med = statistiche([6, 9, 7, 5])
def statistiche(voti):
    if len(voti) == 0:
        return None, None, None
    return min(voti), max(voti), sum(voti) / len(voti)

minimo, massimo, med = statistiche([6, 9, 7, 5])
###esempio 1
print(f"min {minimo}, max {massimo}, media del {med}")
###esempio 2
print(statistiche([]))