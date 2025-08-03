from kargo import *
from paket import *
from musteri import *

def main():
    sistem = Kargo()

    while True:
        print("\n===== Kargo Takip Sistemi =====")
        print("1. Yeni Paket Oluştur")
        print("2. Paket Durumunu Güncelle")
        print("3. Paket Bilgisi Sorgula")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            takip_no = input("Takip No: ")
            agirlik = float(input("Ağırlık (kg): "))

            print("Paket Tipi Seçin:")
            for i, tip in enumerate(PaketTipi, 1):
                print(f"{i}. {tip.value}")
            tip_sec = int(input("Seçim: "))
            tip = list(PaketTipi)[tip_sec - 1]

            print("Müşteri Türü:")
            print("1. Bireysel")
            print("2. Kurumsal")
            musteri_tur = input("Seçim: ")

            if musteri_tur == "1":
                ad = input("Ad: ")
                adres = input("Adres: ")
                telefon = input("Telefon: ")
                musteri = BireyselMusteri(ad, adres, telefon)
            elif musteri_tur == "2":
                temsilci_ad = input("Temsilci Adı: ")
                adres = input("Adres: ")
                telefon = input("Telefon: ")
                vergi_no = input("Vergi No: ")
                firma_adi = input("Firma Adı: ")
                musteri = KurumsalMusteri(temsilci_ad, adres, telefon, vergi_no, firma_adi)
            else:
                print("Geçersiz müşteri türü.")
                continue

            sistem.musteri_ekle(musteri)
            paket = Paket(takip_no, agirlik, tip, musteri)
            sistem.paket_ekle(paket)
            print("Paket ve müşteri başarıyla oluşturuldu.")

        elif secim == "2":
            takip_no = input("Güncellenecek paket takip numarası: ")
            paket = sistem.paket_sorgula(takip_no)
            if paket:
                print("Yeni Durum Seçin:")
                for i, durum in enumerate(Durum, 1):
                    print(f"{i}. {durum.value}")
                sec = int(input("Seçim: "))
                yeni_durum = list(Durum)[sec - 1]
                paket.durum_degistir(yeni_durum)
                print("Durum başarıyla güncellendi.")
            else:
                print("Paket bulunamadı.")

        elif secim == "3":
            takip_no = input("Sorgulanacak takip numarası: ")
            paket = sistem.paket_sorgula(takip_no)
            if paket:
                paket.bilgi_goster()
                print("Müşteri Bilgisi:")
                paket.musteri.show_info()
            else:
                print("Paket bulunamadı.")

        elif secim == "4":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")


if __name__ == "__main__":
    main()
