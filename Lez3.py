###Aprire e scrivere in un file chiamato appunti.txt e scritto con UTF-8, è necessario chiudere per salvare 

f = open("appunti.txt", "w", encoding="utf-8")
f.write("prima riga\n")

# il file non è ancora chiuso: proviamo a rileggerlo
print("prima di close:", repr(open("appunti.txt", encoding="utf-8").read()))

f.close()
print("dopo close:  ", repr(open("appunti.txt", encoding="utf-8").read()))

###Un altro modo per scrivere nel file ma senza il problema della dimenticanza di chiusura

try:
    with open("appunti.txt", "w", encoding="utf-8") as f:
        f.write("prima riga\n")
        print("dentro il with, chiuso?", f.closed)
        1 / 0
except ZeroDivisionError:
    print("il programma è andato in errore")

print("fuori dal with, chiuso?", f.closed)

###con "w" cancella tutto e scrive da zero, se il file non esiste lo crea

with open("lista.txt", "w", encoding="utf-8") as f:
    f.write("mele\n")
    f.write("pere\n")

###con "r" legge ma non scrive, se il file esiste già da errore

with open("lista.txt", "r", encoding="utf-8") as f:
    print(f.read())

###con "a" legge scrive aggiungendo in fondo, se il file non esiste lo crea

with open("lista.txt", "a", encoding="utf-8") as f:
    f.write("banane\n")

###con "x" crea e scrive, se il file esiste già da errore

###Gestione file CSV

import csv

with open("modelli.csv", "w", encoding="utf-8", newline="") as f:
    f.write('Marca,Modello,Prezzo\n')
    f.write('Ford,"Fiesta, 5 porte",3074\n')

with open("modelli.csv", "r", encoding="utf-8") as f:
    for riga in f:
        print(riga.strip().split(","))

print("--- con il modulo csv ---")
with open("modelli.csv", "r", encoding="utf-8", newline="") as f:
    for campi in csv.reader(f):
        print(campi)

###csv.reader(f) si comporta come il file: lo metti in un for e ti dà una lista di campi alla volta. next() preleva la prima riga, l'intestazione.

###csv.DictReader usa la prima riga come chiavi e ti restituisce un dizionario per ogni record.

###auto["Price"] si legge da solo. E se domani qualcuno sposta una colonna, il programma continua a funzionare: cerca per nome, non per posizione.

###Esercizio 1: Scrivi salva_appunto(testo) che aggiunge testo in fondo al file appunti.txt, su una riga nuova. Chiamala tre volte, poi rileggi il file e stampa ogni riga preceduta dal suo numero, partendo da 1. Eseguendo il programma due volte, le righe devono diventare sei

def salva_appunto(testo):
    with open("appunti.txt", "a", encoding="utf-8") as f:
        f.write(testo + "\n")

salva_appunto("comprare il libro")
salva_appunto("ripassare i file")
salva_appunto("consegnare su GitHub")

with open("appunti.txt", "r", encoding="utf-8") as f:
    for numero, riga in enumerate(f, start=1):
        print(numero, riga.strip())

###Esercizio 2: Scrivi conta_righe(nome_file) che restituisce due valori: il numero totale di righe e il numero di righe non vuote. Provala su dati/parole.txt e su dati/commedia.txt.

def conta_righe(nome_file):
    righeTotali = 0
    righePiene = 0
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            righeTotali += 1
            if riga.strip != "":
                righePiene += 1
    return righeTotali, righePiene

for nome in ["dati/parole.txt", "dati/commedia.txt"]:
    tot, righePiene = conta_righe(nome)
    print(f"{nome}: {tot} righe, {righePiene} non vuote")

###Esercizio 3 Scrivi parola_piu_lunga(nome_file) che scorre il file e restituisce la parola con più caratteri. Togli la punteggiatura dalle estremità di ogni parola prima di misurarla.

def parola_piu_lunga(nome_file):
    migliore = ""
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            for parola in riga.split():
                pulita = parola.strip(".,;:!?«»''\"")
                if len(pulita) > len(migliore):
                    migliore = pulita
    return migliore

p = parola_piu_lunga("dati/commedia.txt")
print(p, "-", len(p), "lettere")

###Esercizio 4: Scrivi prezzo_medio(nome_file, alimentazione) che legge dati/car_sales_data.csv con csv.DictReader e restituisce il prezzo medio delle sole auto con quel valore nella colonna Fuel type, arrotondato a due decimali. Se nessuna auto corrisponde, restituisci None. Provala con Petrol, Diesel, Hybrid e con un valore inesistente.

def prezzo_medio(nome_file, alimentazione):
    somma = 0
    quantità = 0
    with open(nome_file, "r", encoding = "utf-8", newline = "") as f:
        for auto in csv.DictReader(f):
            if auto["Fuel type"] == alimentazione:
                somma += int(auto["Price"])
                quantità += 1
    if quantità == 0:
        return None
    return round (somma/quantità, 2)

for tipo in ["Petrol", "Diesel", "Hybrid", "Elettrica"]:
    print(tipo, "ha", prezzo_medio("dati/car_sales_data.csv", tipo))
