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