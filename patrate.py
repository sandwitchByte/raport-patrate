import math

def raport(lungime, latime):

    perimetru = 2 * (lungime + latime)
    arie =  lungime * latime
    r = perimetru / (math.sqrt(arie))
    r = '{:.{}f}'.format(r, 4)
    return r

with open('date.txt', 'r') as file:
    for line in file:

        dimensiuni = line.split()
        lungime = float(dimensiuni[0])
        latime = float(dimensiuni[1])

        print(raport(lungime, latime), '\n')



