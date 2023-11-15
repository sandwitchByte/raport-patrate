import math

precizieNumar = '{:.{}f}'
formatTabel ='{:>15}' * 6   # specificatori de format
                            # informatie suplimentara la
                            # https://docs.python.org/3/library/string.html#formatspec

# functiile utilizate pentru calcule
def arie(lungime, latime):
    return lungime * latime

def perimetru(lungime, latime):
    return 2 * (lungime + latime)

def raport(lungime, latime):
    # formula raportului calculat
    r = perimetru(lungime, latime)/ (math.sqrt(arie(lungime, latime))) 
    r = precizieNumar.format(r, 4) # setarea preciziei
    return r

with open('date.txt', 'r') as file: # aici se citesc dimensiunile care
                                    # trebuie prelucrate
    print('Rezulatate :')
    print(formatTabel.format('nr', 'latime', 'lungime', 'arie', 'perimetru', 'raportul n'))
    print() # inceputul tabelului
    i = 1

    for line in file: 
        dimensiuni = line.split()
        lungime = float(dimensiuni[0]) # convertiri de tip
        latime = float(dimensiuni[1])
        N = raport(lungime, latime)

        # afisarea rezultatelor sub forma de tabel
        a = precizieNumar.format(arie(lungime, latime), 4)
        p = precizieNumar.format(perimetru(lungime, latime), 2)
        print(formatTabel.format(i, latime, lungime, a, p, N))
        i = i + 1
     # rezultatele se afiseaza la ecran



