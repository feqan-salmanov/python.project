rehber={
    "kisiler":{
        "kisi adi":"fagan",
        "kisi soy isim":"salmanov",
        "ev numarasi":"51551515151515",
        "sirket numarisi":"54465131645",
        "cep numarasi":"5465132165132",
        "location":"28 may HAYDAR ALIYEV prospekti"
    }
}
kisiismi = input("Kisinin ismi:")
kisininbilgisi = input("Bilgini giriniz:")
if kisiismi in rehber.keys():
    flag = True
else:
    flag = False
if flag:
    print(rehber.get(kisiismi).get(kisininbilgisi,"Kullanici bilgisi bulunmadi.."))
else:
    print("Kullanici bilgisi bulunmadi..")