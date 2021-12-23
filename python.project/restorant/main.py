masalar=dict()
for i in range(10):
    masalar[i]=0
def hesabekle():
    masano=int(input("Masa nomresi gir :"))
    hazirki=masalar[masano]
    elave=int(input("Elave edilecek pul:"))
    toplam=hazirki+elave
    masalar[masano]=toplam
def hesabsil():
    masano=int(input("Masa nomresi gir :"))
    hazirki=masalar[masano]
    sil=int(input("Elave edilecek pul:"))
    toplam=hazirki-sil
    masalar[masano]=toplam
def mine():
    while True:
        print("""
        [1] Masalar Goster
        [2] Hesab elave et
        [3] Hesab sil
        [4] Quit
        """)
        islem = input("Islem secin :")
        if islem == "1":
            for i in range(10):
                print("Masa  {} ucun islem {}".format(i,masalar[i]))
            print("Proqram basa catdi geri qayitmax ucun entere basin")
            input()
        elif islem == "2":
            hesabekle()
            print("Proqram basa catdi geri qayitmax ucun entere basin")
            input()
        elif islem == "3":
            hesabsil()
            print("Proqram basa catdi geri qayitmax ucun entere basin")
            input()
        elif islem == "4":
            quit()
mine()



