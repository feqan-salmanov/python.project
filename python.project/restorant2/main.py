import os
masalar = dict()
for i in range(10):
    masalar[i] = 0
def hesabekle():
    masano=int(input("Masa no :"))
    gecerli=masalar[masano]
    eklenecek=int(input("Eklenecek miktar:"))
    toplam=gecerli+eklenecek
    masalar[masano]=toplam
def hesabsil():
    masano=int(input("Masa no :"))
    gecerli=masalar[masano]
    cixilacax=int(input("Cixilcax miktar:"))
    toplam=gecerli-cixilacax
    masalar[masano]=toplam
def hesabkontrol(dosya_adi):
    try:
        dosya=open(dosya_adi)
        veriler=dosya.read()
        veriler=veriler.split("/n")
        veriler.pop()
        dosya.close()
        flag=True
    except FileNotFoundError:
        dosya=open(dosya_adi,"w")
        dosya.close()
        flag=False
    if flag:
        for i in enumerate(veriler):
            masalar[i[0]]=int(i[1])
    else:
        pass

def main():
    hesabkontrol("dosya.txt")
    while True:
        os.system("cls")
        print("""
        [1] Masalar
        [2] Hesaba elave et
        [3] Hesebdan cix 
        [4] Proqramdan cixis
        """)
        islem=input("Istifade yolu secin :")
        if islem=="1":
            for i in range(10):
                print("Masa {} un hesab {}".format(i, masalar[i]))
            print("Proqram basa catmisdir ger qayitmag ucun entere basin !!!. ")
            input()
        elif islem=="2":
            hesabekle()
            print("Proqram basa catmisdir ger qayitmag ucun entere basin !!!. ")
            input()
        elif islem=="3":
            hesabsil()
            print("Proqram basa catmisdir ger qayitmag ucun entere basin !!!. ")
            input()
        elif islem=="4":
            quit()
            print("Cixilir...")

main()



