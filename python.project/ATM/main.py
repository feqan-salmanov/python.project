print("""

ATM uygulamasına hoş geldiniz.!
(1) Bakiye Sorma
(2) Para Çekme
(3) Para Yatırma
(q) Çıkış

""")

bakiye = 1000

while True:
    islem = input("Lütfen işlem seçiniz: ")
    if islem == "q":
        print("İyi Günler Dileriz..")
        break
    elif (islem == "1"):
        print("Bakiye: {}".format(bakiye))

    elif (islem == "2"):
        tutar = int(input("Ne kadar çekmek istiyorsunuz: "))

        if (bakiye - tutar < 0):
            print("Yetersiz bakiye...")
            continue
        bakiye -= tutar

    elif (islem == "3"):
        tutar = int(input("Ne kadar para yatırmak istiyorsunuz: "))
        bakiye = bakiye + tutar
        print("Yeni bakiyeniz: {}".format(bakiye))
    else:
        print("Geçersiz işlem girdiniz..!")