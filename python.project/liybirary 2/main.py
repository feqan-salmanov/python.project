kitapliste = list()

menu = """
[1] Kitab ekle.
[2] Listele.
[q] Cikis.

"""
def kitapekle(kitab,liste):
    liste += [kitab]
    print("Kitabiniz eklendi..")
    input("Ana menuya donmek icinn 'enter' basin.")
def listele(liste):
    for i in kitapliste :
        print("Kitabiniz ------>>>>>>  {}".format(i))
    input("Ana menuya donmek icinn 'enter' basin.")
def cix():
    quit()
while True:
    print(menu)
    secim=input("Seciminiz:")
    if secim=="1":
        kitabadi=input("Kitab adi:")
        kitapekle(kitabadi,kitapliste)
    elif secim=="2":
        listele(kitapliste)
    elif secim== "q" or "Q":
        cix()
    else:
        print("Hatali girdiniz")
        input("Ana menuya donmek icinn 'enter' basin.")


