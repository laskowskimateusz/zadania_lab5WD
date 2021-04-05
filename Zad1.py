class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print("\nRodzaj - {}\nDlugosc - {}\nSzerokosc - {}".format(self.rodzaj, self.dlugosc, self.szerokosc))


class Ubrania(Material):
    def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo):
        super().__init__(rodzaj, dlugosc, szerokosc)
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        print("\nRodzaj - {}\nDlugosc - {}\nSzerokosc - {}".format(self.rodzaj, self.dlugosc, self.szerokosc))
        print("Rozmiar - {}\nKolor - {}\nDla kogo - {}".format(self.rozmiar, self.kolor, self.dla_kogo))


class Sweter(Ubrania):
    def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo, rodzaj_swetra):
        super().__init__(rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo)
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        print("\nRodzaj - {}\nDlugosc - {}\nSzerokosc - {}".format(self.rodzaj, self.dlugosc, self.szerokosc))
        print("Rozmiar - {}\nKolor - {}\nDla kogo - {}\nRodzaj".format(self.rozmiar, self.kolor, self.dla_kogo))
        print("Rodzaj swetra - {}".format(self.rodzaj_swetra))


test1 = Sweter("test", 20, 40, 'M', "Czerwony", "Mama", "Inny")
test1.wyswietl_nazwe()
test1.wyswietl_dane()

test2 = Ubrania("test2", 30, 60, 'L', "Czarny", "Tata")
test2.wyswietl_nazwe()
test2.wyswietl_dane()
