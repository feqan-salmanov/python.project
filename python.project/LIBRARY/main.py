import os
kitablist = list()

menu = """
[1] Kitab ekle.
[2] Kitab al.
[3] Kitablari listele.
[q] Cixis

"""
def kitabekle(kitab:tuple,liste:list):
    liste.append(kitab)
    print("Kitab eklendi")
    input("Ana menuya donmek icin 'enter' tusuna basiin..")
    input()
def kontrol(kitab,liste):
    if kitab in liste:
        return True
    else:
        return  False
def kitabal(kitab:tuple,liste:list):
   if kontrol(kitab,liste):
       liste.remove(kitab)
       print("Kitabi aldiniz..")
       input("Ana menuya donmek icin 'enter' tusuna basiin..")
       input()
   else:
       print("Bu kitab movcut deyil..")
def kitabli(liste):
    for i in liste:
        print("Kitab adi :{} --------->>>>>> Yazr :{}".format(i[0],i[1]))

while True:
    os.system("cls")
    print(menu)
    secim = input("Seciminiz :")
    if secim == "1":
        kitap_adi = input("Kitab ismi :")
        kitab_yazar = input("Yazar:")
        kitab = (kitap_adi,kitab_yazar)
        kitabekle(kitab,kitablist)
    elif secim == "2":
        kitap_adi = input("Kitab ismi :")
        kitab_yazar = input("Yazar:")
        kitab = (kitap_adi, kitab_yazar)
        kitabal(kitab, kitablist)
    elif secim == "3":
        kitabli(kitablist)
    elif secim == "q" or secim == "Q":
        pass
    else:
        print("Yanlis secim....")
        input("Ana menuya donmek icin 'enter' tusuna basiin..")