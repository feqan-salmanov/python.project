faqan_hesap = {

    "ad": "FEGAN",
    "hesapNo": "10142018",
    "bakiye": 3000,
    "ekHesap": 2000,
}

ELDARHesap = {

    "ad": "ELDAR",
    "hesapNo": "02042019",
    "bakiye": 2000,
    "ekHesap": 1000,
}


def para_cek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap["bakiye"] = hesap["bakiye"] - miktar
        print("Paranızı Alabilirsiniz.")
        print("======================================")
        print("BAKİYE BİLGİSİ: ")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if (toplam >= miktar):
            print(f"Ana hesaptaki Bakiyeniz Yetersiz: = {hesap['bakiye']}")
            ekHesapKullanimi = input("Ek Hesap Kullanılsın mı (e/h): ")

            if ekHesapKullanimi == "e":

                ekHesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKullanilacakMiktar
                print("Paranızı Alabilirsiniz.")
                print("======================================")
                print("BAKİYE BİLGİSİ: ")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print("Bakiyeniz Yetersiz!")
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(
        f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL Bulunmaktadır.\nEk hesap limitinizde ise {hesap['ekHesap']} TL Bulunmaktadır. ")


def bakiyeEkle(hesap):
    print(f"Merhaba {hesap['ad']}")
    eMiktar =input("Hesabınıza yatıralacak bakiye miktarını giriniz: ")
    sonBakiye = hesap['bakiye'] + eMiktar
    print(f"{hesap['hesapNo']} nolu hesabınıza {eMiktar} TL Eklenmiştir.")
    print("======================================")
    print(f"Güncel Bakiyeniz: {sonBakiye}")


def ekHesap(hesap):
    print(f"Merhaba {hesap['ad']}")
    eBakiye = int(input("Ek Hesabınıza yatıralacak bakiye miktarını giriniz: "))
    lastBakiye = hesap['bakiye'] + eBakiye
    print(f"{hesap['hesapNo']} nolu Ek Hesabınıza {eBakiye} TL Eklenmiştir.")
    print("======================================")
    print(f"Güncel Ek Bakiyeniz: {lastBakiye}")


print("======================================")

para_cek(faqan_hesap, 3000)  # 1. para çekme işlemi

print("======================================")

para_cek(ELDARHesap, 2000)  # 2. para çekme işlemi

print("======================================")

bakiyeEkle(faqan_hesap)

print("======================================")

ekHesap(ELDARHesap)

print("======================================")
