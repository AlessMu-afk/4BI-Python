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