print("""
[1] Toplma
[2] Cixma
[3] Bolme
[4] Vurma
[5] Quvvet
[6] Cixis
""")
giris = input("Seciminiz :")

if giris == "1":
    x = input("No-1 :")
    x = int(x)
    y = input("No-2 :")
    y = int(y)
    print("Cavabiniz :",x+y)
elif giris == "2":
    x = input("No-1 :")
    x = int(x)
    y = input("No-2 :")
    y = int(y)
    print("Cavabiniz :",x-y)
elif giris == "3":
    x = input("No-1 :")
    x = int(x)
    y = input("No-2 :")
    y = int(y)
    if y==0:
        print("Sifira bolmek olmaz ...")
        print("Cixilir")
        quit()
    else:
        print("Cavabiniz:",x/y)

elif giris == "4":
    x = input("No-1 :")
    x = int(x)
    y = input("No-2 :")
    y = int(y)
    print("Cavabiniz :",x*y)
elif giris == "5":
    x = input("No-1 :")
    x = int(x)
    y = input("No-2 :")
    y = int(y)
    print("Cavabiniz :", x**y)
elif giris == "6" :
    print("Cixilir....")
    quit()
else:
    print("Xetali giris ....")


