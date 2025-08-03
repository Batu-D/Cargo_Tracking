from enum import Enum
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import random

class Durum(Enum):
    HAZIRLANIYOR = "Hazırlanıyor"
    YOLDA = "Yolda"
    TESLIM_EDILDI = "Teslim Edildi"

class Takip:
    def __init__(self,takip_no):
        self.takip_no = takip_no
        self.simulasyon_saati = datetime.now()
        self.hareket_gecmisi = []

    def _hareket_ekle(self, durum: Durum):
        self.hareket_gecmisi.append({
            "durum": durum.value,
            "zaman": self.simulasyon_saati.strftime("%Y-%m-%d %H:%M:%S")
        })

    def durum_degistir(self, yeni_durum: Durum):
        ay_arti = random.randint(0, 2)
        gun_arti = random.randint(0, 2)  # 0–2 gün arası
        saat_arti = random.randint(0, 5)  # 0–5 saat arası
        dakika_arti = random.randint(5, 30)  # 5–30 dakika arası
        saniye_arti = random.randint(0, 59)

        self.simulasyon_saati += relativedelta(months=ay_arti)
        self.simulasyon_saati += timedelta(
            days=gun_arti,
            hours=saat_arti,
            minutes=dakika_arti,
            seconds=saniye_arti
        )
        self.durum = yeni_durum
        self._hareket_ekle(yeni_durum)
