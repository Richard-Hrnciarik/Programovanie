#vlajkamodul

class Vlajka:
    def __init__(self, x, y, sirka, vyska, zvislo, farby):
        self.zvislo = zvislo
        self.farby = farby
        self.x = x
        self.y = y
        self.sirka = sirka
        self.vyska = vyska
        self.obdlzniky = []

    def kresli(self, cnv):
        for i in range(len(self.obdlzniky)):
            cnv.delete(self.obdlzniky[i])        
        n = len(self.farby)
        for i in range(n):
            x = self.x - self.sirka / 2
            y = self.y - self.vyska / 2
            if self.zvislo:
                obdlznik = cnv.create_rectangle(x+i*self.sirka/n, y,
                                                x+(i+1)*self.sirka/n,
                                                y+self.vyska, width=0,
                                                fill=self.farby[i])
                self.obdlzniky.append(obdlznik)
            else:
                obdlznik = cnv.create_rectangle(x, y+i*self.vyska/n,
                                                x+self.sirka,
                                                y+(i+1)*self.vyska/n,
                                                width=0, fill=self.farby[i])
                self.obdlzniky.append(obdlznik)

    def zoom(self, pomer):
        self.sirka *= pomer
        self.vyska *= pomer

    '''def generuj_nahodnu(self, x, y, sirka, vyska, pocet_pruhov):
        farby = ('red', 'green', 'white', 'blue', 'purple', 'yellow')
        for i in range(len(self.obdlzniky)):
            self.cnv.delete(self.obdlzniky[i])        
        for i in range(pocet_pruhov):
            x = self.x - self.sirka / 2
            y = self.y - self.vyska / 2
            if self.zvislo:
                obdlznik = self.cnv.create_rectangle(x+i*self.sirka/pocet_pruhov, y,
                                                x+(i+1)*self.sirka/pocet_pruhov,
                                                y+self.vyska, width=0,
                                                fill = choice(farby))
                self.obdlzniky.append(obdlznik)
            else:
                obdlznik = self.cnv.create_rectangle(x, y+i*self.vyska/pocet_pruhov,
                                                x+self.sirka,
                                                y+(i+1)*self.vyska/pocet_pruhov,
                                                width=0, fill= choice(farby))
                self.obdlzniky.append(obdlznik)'''
        
