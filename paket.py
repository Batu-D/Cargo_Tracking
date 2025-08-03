from enum import Enum
from musteri import *
from takip import Takip, Durum


class PaketTipi(Enum):
    EVRAK = "Evrak"
    KOLI = "Koli"
    KIRILABILIR = "Kırılabilir"

class Paket(Takip):
    def __init__(self, takip_no: str, agirlik: float,tip :PaketTipi, musteri):
        super().__init__(takip_no)
        self.agirlik = agirlik
        self.tip = tip
        self.durum: Durum = Durum.HAZIRLANIYOR
        self.musteri = musteri
        self._hareket_ekle(self.durum)

    def bilgi_goster(self):
        print(f"Takip No: {self.takip_no}")
        print(f"Ağırlık: {self.agirlik} kg")
        print(f"Tip: {self.tip.value}")
        print(f"Durum: {self.durum.value}")
        print("Hareket Geçmişi:")
        for hareket in self.hareket_gecmisi:
            print(f" - {hareket['zaman']} : {hareket['durum']}\n")