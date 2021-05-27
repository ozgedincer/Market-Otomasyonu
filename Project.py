from Market import *
urunNesne = SuperMarket()
print("""
Market Uygulamasına Hoşgeldiniz!
1-Ürün Ekle
2-Ürün Sil
3-Stok Sorgula
4-Son Kullanma Tarihi Sorgulama ve Silme
5-Satış Yap
6-İade Al
7-Günlük Yapılan Satış
8-Günlük Alınan İade 
9-Günlük Kar-Zarar Durumu
10-Kapat
""")
while True:
    secim=int(input("Seçim Yapın: "))
    if secim==1:
        urunAdi=input("Ürün Adı : ")
        marka=input("Marka : ")
        fiyat = float(input("Fiyat : "))
        skt=input("Son Kullanma Tarihi : ")
        urunCesidi=input("Ürün Çeşidi : ")
        stok=int(input("Stok : "))
        print("Ürün Eklendi")
    elif secim==2:
        urunAdi = input("Silmek İstediğiniz Ürün Adını Girin : ")
    elif secim==3:
        urunAdi=input("Stoğunu Sorgulamak istediğiniz Ürün Adını Girin : ")
    elif secim==4:
        girdi = input("Hangi Tarihten Öncesini Silmek İstiyorsunuz (Örn:01.01.2021) : ")
    elif secim==5:
        girdi=input("Satılacak Ürün Adı Girin : ")
        print("Fiş Kesiliyor. Ödeme için teşekkürler!")
    elif secim==6:
        girdi=input("İade Edilmek İstenen Ürün Adı Girin : ")
    elif secim==7:
        urunNesne.GunlukYapilanSatis()
    elif secim==8:
        urunNesne.GunlukAlinanIadeSayisi()
    elif secim==9:
        urunNesne.GunlukKarZararHesapla()
    elif secim==10:
        break
    else:
        print("Geçersiz İşlem!")
