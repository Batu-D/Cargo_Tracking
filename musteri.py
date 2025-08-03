from paket import *

class Musteri:
    def __init__(self,ad: str,adres: str,telefon: str):
        self.ad = ad
        self.adres = adres
        self.telefon = telefon

    def show_info(self):
        print(f"Müşteri adı: {self.ad}\nMüşteri adresi: {self.adres}\nMüşteri telefonu: {self.telefon}\n ")


class BireyselMusteri(Musteri):
    def __init__(self,ad,adres,telefon):
        super().__init__(ad,adres,telefon)
    def show_info(self):
        print("Bireysel Müşteri:\n")
        super().show_info()

class KurumsalMusteri(Musteri):
    def __init__(self,temsilci_ad,adres,telefon,vergi_no: str,firma_adi: str):
        super().__init__(temsilci_ad,adres,telefon)
        self.vergi_no = vergi_no
        self.firma_adi = firma_adi
    def show_info(self):
        print("Kurumsal Müşteri:\n")
        print(f"Firma adı: {self.firma_adi}\nVergi no: {self.vergi_no}\n")
        super().show_info()


