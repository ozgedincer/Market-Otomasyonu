from Market import *
urunNesne = SuperMarket()
print("""
Market Uygulamasına Hoşgeldiniz!
1. ÜRÜN EKLE
2. ÜRÜN SİL
3. ÜRÜN STOĞU SORGULA
4. SON KULLANMA TARİHİ GEÇENLERİ KALDIR
5. SATIŞ YAP
6. İADE AL
7.GÜNLÜK TOPLAM YAPILAN SATIŞ
8.GÜNLÜK TOPLAM ALINAN İADE SAYISI
9.KASAYI KAPAT
""")
while True:
    secim=int(input("Seçim Yapın : "))
    if (secim==1):
        urunAdi=input("Ürün Adı : ")
        marka=input("Marka : ")
        fiyat = float(input("Fiyat : "))
        skt=input("Son Kullanma Tarihi : ")
        urunCesidi=input("Ürün Çeşidi : ")
        stok=int(input("Stok : "))
        urun=Urun(urunAdi,marka,fiyat,skt,urunCesidi,stok)    
        urunNesne.UrunEkle(urun)  
        print("Ürün Eklendi!")
    elif (secim==2):
        urunAdi = input("Silmek İstediğiniz Ürün Adını Girin : ")
        urunNesne.UrunSil(urunAdi)
    elif (secim==3):
        urunAdi=input("Sorgulamak istediğiniz ürün adını girin : ")
        urunNesne.UrunAdinaGoreStokSorgula(urunAdi)
    elif (secim==4):
        girdi = input("Hangi Tarihten Öncesini Silmek İstiyorsunuz : ")
        urunNesne.SonKullanmaTarihiGecenleriSil(girdi)
    elif (secim==5):
        while True:
            girdi=input("Ürün Adı Girin (iptal : i | fiş : f): ")
            if (girdi=="i"):
                urunNesne.ilkGiris=True    
                break
            elif (girdi=="f"):
                print("Fiş Kesiliyor. Ödeme için teşekkürler!")
                urunNesne.FisKes()
                break
            else:
                urunNesne.SatisYap(girdi)
    elif (secim==6):
        girdi=input("İade etmek istediğiniz ürünün adını girin : ")
        urunNesne.IadeAl(girdi)
    elif (secim==7):
        urunNesne.GunlukAlinanIadeSayisi()
    elif (secim==8):
        urunNesne.GunlukCiroHesapla()
    elif (secim==9):
        urunNesne.KasayiKapat()
        urunNesne.VeritabaniBaglantisiniKes()
        print("Şimdi Çıkıyoruz Daha Sonra Görüşürüz :)")
        break
    else:
        print("Geçersiz İşlem Tekrar Deneyin!")
