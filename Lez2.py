###le liste sono ordinate e modificabili e possono contenere variabili di tipi diversi

voti = [6, 8, 5, 8, 7]
voti.append(9)                              ###append() aggiunge un elemento alla fine della lista.
voti.insert(0, 4)                           ###insert(indice, valore) inserisce un elemento nella posizione indicata
print(voti)                                 ###è una funzione (NON un metodo) perchè non richiama alcun oggetto

print(voti[0], voti[-1])                    ###si stampa primo ed ultimo numero
print(voti[1:4])                            ###si prendono in considerazione gli elementi dall'indice 1 al 4 (escludendo il 4)

voti.sort()                                 ###riordina la lista sul posto in ordine crescente e restituisce None
print(voti)

print(len(voti), 8 in voti)                 ###len conta quanti elementi ci sono nella lista, poi controlla se il numero 8 è presente

###Se scrivi voti = voti.sort() perdi la lista e ti ritrovi con None. Lo stesso vale per reverse(), append() e insert()
###Se ti serve una copia ordinata senza toccare l'originale, usa sorted(voti)

###set, un insieme che contiene solo elementi unici

presenze = ["Luca", "Sara", "Marco", "Luca", "Sara"]
unici = set(presenze)                       ###trasforma la lista in un insieme, eliminando i duplicato

print(len(presenze), "voci registrate")     ###stampa le presenze contate in "presenze"

print(len(unici), "persone diverse")        ###stampa le persone contate in "unici"
print(sorted(unici))                      
###operazioni insiemistiche

informatica = {"Luca", "Sara", "Marco"}
sistemi = {"Sara", "Giulia"}

print(sorted(informatica | sistemi))
print(sorted(informatica & sistemi))
print(sorted(informatica - sistemi))

###Unione	|	Chi c'è in almeno uno dei due gruppi
###Intersezione	  &    Chi c'è in tutti e due
###Differenza	-	Chi c'è nel primo e non nel secondo
###Differenza simmetrica    ^	 Chi c'è in uno solo dei due

###tuple è come liste ma non modificabili

week = ("lun", "mar", "mer", "gio", "ven")

print(week)
print(week[0], week[-1])
print(len(week))

###Senza virgola le parentesi sono solo parentesi di calcolo e ottieni un numero. È la virgola a fare la tupla, non le parentesi
###uno = (5)
###uno_vero = (5,)

###con try si può tentare un'operazione rischiosa che genererebbe errore, il blocco except intercetta questo errore bloccando il crash del programma e stampa la descrizione dell'errore 

try:
    week[0] = "dom"
except TypeError as errore:
    print("TypeError:", errore)     

###dizionari, coppie chiave-valore dove si ricerca per nome, cercando le chiavi

capitali = {"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}

print(capitali["Italia"])                 ###stampa il valore della chiave
###riga 67
print(len(capitali))                        ###Restituisce il numero totale di elementi presenti nel dizionario

capitali["Germania"] = "Berlino"            ###modifica
del capitali["Spagna"]                      ###elimina
print(capitali)

###ciclo per stampare ciò che c'è nel dizionario

for paese, citta in capitali.items():
    print(paese, "->", citta)

print(list(capitali.keys()))                ###stampare solo valore
print(list(capitali.values()))              ###stampare solo le chiavi

###leggere una chiave che non c'è con le parentesi quadre fa crollare il programma
###il metodo get() fa la stessa cosa senza far esplodere niente: se la chiave manca restituisce None, oppure il valore che gli indichi tu

###Lista []                 La sequenza conta e i dati cambiano: voti in ordine di interrogazione, righe di un file - duplicati - modificabile
###Set {}                   Ti interessa solo chi c'è: eliminare doppioni, confrontare due gruppi - non accetta duplicati - modificabili
###Tupla ()                 I dati non devono cambiare, o ti servono come chiave: coordinate, giorni della settimana - duplicati - non modificabili
###Dizionario {k: v}        Cerchi per nome e non per posizione: voto di uno studente, capitale di un paese - chiavi non accettate duplicate - modificabili

###esercizi aura

###esercizio 1:Scrivi conta_unici(nomi) che riceve una lista di nomi, anche ripetuti, e restituisce quante persone diverse contiene. Provala su ["Luca", "Sara", "Marco", "Luca", "Giulia", "Sara", "Luca"]
def conta_unici(nomi):
    return len(set(nomi))

lista = ["Luca", "Sara", "Marco", "Luca", "Giulia", "Sara", "Luca"]
print("ci sono", conta_unici(lista), "persone diverse")

###esercizio 2:Parti dal dizionario {"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}. Scrivi capitale(paese) che restituisce la capitale, e la stringa "paese non in elenco" se il paese non c'è.

capitali = {"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}

def capitale(paese):
    return capitali.get(paese, "Paese non presente")

print(capitale("Italia"))
print(capitale("sixseven"))

###esercizio 3:Scrivi sufficienze(voti) che riceve una lista di voti e restituisce una nuova lista con i soli voti maggiori o uguali a 6, nell'ordine originale. Usa una list comprehension, non un ciclo.

def sufficienze(voti):
    return [voto for voto in voti if voto >= 6]

print(sufficienze([4, 7, 5, 8, 6, 3]))
print(sufficienze([]))

###esercizio 4:Scrivi senza_duplicati(elementi) che elimina i doppioni mantenendo l'ordine di prima comparsa. Su ["Sara", "Luca", "Sara", "Marco", "Luca", "Giulia"] deve restituire ['Sara', 'Luca', 'Marco', 'Giulia'].

def senza_duplicati(elementi):
    visti = set()
    risultato = []
    for e in elementi:
        if e not in visti:
            visti.add(e)
            risultato.append(e)
    return risultato

nomi = ["Sara", "Luca", "Sara", "Marco", "Luca", "Giulia"]
print(senza_duplicati(nomi))
print(sorted(set(nomi)))

###esercizio 5:Scrivi conta_parole(frase) che restituisce quante volte compare ogni parola. Ignora le maiuscole. Poi stampa la parola più frequente e il suo conteggio. Provala su "il gatto dorme il cane dorme il topo corre". La struttura da usare devi sceglierla tu.

def conta_parole(frase):
    conteggio = {}
    for parola in frase.lower().split():
        conteggio[parola] = conteggio. get(parola, 0) + 1
    return conteggio

frase = "sixseven sixseven sixseven"
risultato = conta_parole(frase)
print(risultato)

piu_frequente = max(risultato, key=risultato.get)
print(piu_frequente, risultato[piu_frequente])