from paket import *
from musteri import *

class Kargo:
    def __init__(self,):
        self.paketler = []
        self.musteriler = []

    def paket_ekle(self,paket: Paket):
        self.paketler.append(paket)
        print(f"Paket eklendi: {paket.takip_no}")

    def musteri_ekle(self,musteri: Musteri):
        self.musteriler.append(musteri)
        print(f"Müşteri eklendi: {musteri.ad}")

    def paket_sorgula(self,takip_no: str):
        for paket in self.paketler:
            if paket.takip_no == takip_no:
                paket.bilgi_goster()
                return paket
        return None

