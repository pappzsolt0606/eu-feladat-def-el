class Eu:
    def __init__(self,sor):
        orszag,datum = sor.strip().split(";")
        self.orszag = orszag
        self.datum = datum
        self.ev = int(datum[0:4])
        self.honap = datum[5:7]
        self.nap = datum[8:10]

def get_list():
    lista = []
    with open("EUcsatlakozas.txt", encoding = "latin2") as f:
        for sor in f:
            lista.append(Eu(sor))
    return lista

def harmadik(lista):
    a = 0
    for sor in lista:
        a = a+1
    return a


def negyedik(lista):
    a = 0
    for sor in lista:
        if sor.ev == 2007:
            a = a+1
    return a

def otodik(lista):
    a = ""
    for sor in lista:
        if sor.orszag == "Magyarország":
            a = sor.datum
    return a

def hatodik(lista):
    a = False
    for sor in lista:
        if sor.honap == "05":
            a = True
    return a


def hetedik(lista):
    a = 0
    orszag = ""
    for sor in lista:
        if sor.ev > a:
            a = sor.ev
            orszag = sor.orszag
    return orszag

    
def nyolcadik(lista):
    a = ""
    stat = dict()
    for sor in lista:
        ev = sor.ev
        stat[ev] = stat.get(ev,0) + 1
    for ev,darab in stat.items():
        a = a + f"        {ev} - {darab}\n"
    return a
        
