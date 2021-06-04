import sqlite3
class Urun():
    def __init__(self,uAdi,marka,fiyat,skt,uCesidi,stok):
        self.uAdi=uAdi
        self.marka=marka
        self.fiyat=fiyat
        self.skt=skt
        self.uCesidi=uCesidi
        self.stok=stok
    
    def __str__(self):
        return self.stok
    
class SuperMarket():
    def __init__(self):
        self.VeritabaninaBaglan()
        self.ilkGiris=True
        self.gunlukToplamMusteri=0
        self.toplamfiyat=0
        self.toplamCiro=0
        self.gunlukToplamIade=0

    def VeritabaninaBaglan(self):
        self.baglanti = sqlite3.connect("veriler.db")
        self.cursor=self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS veriler(UrunAdi TEXT,Marka TEXT,Fiyat REAL,SKT TEXT,UrunCesidi TEXT,Stok INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()  
    
    def VeritabaniBaglantisiniKes(self):
        self.baglanti.close()

    def UrunEkle(self,urunNesnesi):
        sorgu = "INSERT INTO veriler VALUES(?,?,?,?,?,?)"
        self.cursor.execute(sorgu,(urunNesnesi.uAdi,urunNesnesi.marka,urunNesnesi.fiyat,urunNesnesi.skt,urunNesnesi.uCesidi,urunNesnesi.stok))
        self.baglanti.commit()
    
    def UrunSil(self,isim):
        sorgu2="SELECT * FROM veriler WHERE UrunAdi = ?"
        self.cursor.execute(sorgu2,(isim,))
        silinecekUrunler=self.cursor.fetchall()
        if (len(silinecekUrunler)==0):
            print("Böyle bir ürün bulunmuyor.")
        else:
            print("Ürün Silindi!")
        sorgu = "DELETE FROM veriler WHERE UrunAdi = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()
    
    def UrunAdinaGoreStokSorgula(self,isim):
        sorgu = "SELECT * FROM veriler WHERE UrunAdi = ?"
        self.cursor.execute(sorgu,(isim,))
        urunler=self.cursor.fetchall()
        if (len(urunler)==0):
            print("Stokta böyle bir ürün bulunmuyor.")
        else:
            toplamurun=0
            for i in urunler:
                toplamurun +=i[5]
            print(toplamurun)
    
    def TarihiGecenleriSil(self,isim):
        sorgu = "DELETE FROM veriler WHERE UrunAdi = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

    def SonKullanmaTarihiGecenleriSil(self,tarih):
        sorgu = "SELECT * FROM veriler"
        self.cursor.execute(sorgu)
        butunurunler = self.cursor.fetchall()

        if (len(butunurunler)==0):
            print("Stokta hiçbir ürün bulunmuyor.")
        else:
            for i in butunurunler:
                sktlistesi = i[3].split(".")
                tarihlistesi = tarih.split(".")

                if (tarihlistesi[2]>sktlistesi[2]):
                    self.TarihiGecenleriSil(i[0])
                elif (tarihlistesi[2]==sktlistesi[2] and tarihlistesi[1]>sktlistesi[1]):
                    self.TarihiGecenleriSil(i[0])
                elif(tarihlistesi[2]==sktlistesi[2] and tarihlistesi[1]==sktlistesi[1] and tarihlistesi[0]>sktlistesi[0]):
                    self.TarihiGecenleriSil(i[0])

    def SatisYap(self,isim):
        self.satisisim=isim
        sorgu = "SELECT * FROM veriler WHERE UrunAdi = ?"
        self.cursor.execute(sorgu,(isim,))
        urun=self.cursor.fetchall()
        if(len(urun)==0):
            print("Bu ürün bulunmuyor.")
        else:
            if (self.ilkGiris):
                self.urunstok=urun[0][5]     #
            self.urunstok -= 1
            
            self.toplamfiyat +=urun[0][2]

            print("Ürün Sepetinize Eklendi!")
            self.ilkGiris=False

    def FisKes(self):
        sorgu="UPDATE veriler SET Stok = ? WHERE UrunAdi = ?"
        self.cursor.execute(sorgu,(self.urunstok,self.satisisim))
        self.baglanti.commit()
        print("Toplam Tutar : {} TL".format(self.toplamfiyat))
        self.gunlukToplamMusteri +=1
        self.toplamCiro+=self.toplamfiyat

        self.ilkGiris=True
        self.toplamfiyat=0

    def GunlukCiroHesapla(self):
        if (self.toplamCiro>0):
            print("-----------")
            print("Kârdasınız!")
        elif(self.toplamCiro<0):
            print("-------------")
            print("Zarardasınız!")
        print("Günlük Toplam Cironuz : {} TL".format(self.toplamCiro))

    def IadeAl(self,isim):
        sorgu="SELECT * FROM veriler WHERE UrunAdi = ?"
        self.cursor.execute(sorgu,(isim,))
        urunler = self.cursor.fetchall()
        stok = urunler[0][5]
        stok +=1
        self.toplamCiro-=urunler[0][2]
        sorgu2="UPDATE veriler SET Stok = ? WHERE UrunAdi = ?"
        self.cursor.execute(sorgu2,(stok,isim))
        self.baglanti.commit()
        print("İade Alındı! Teşekkürler.")
        self.gunlukToplamIade+=1

    def GunlukAlinanIadeSayisi(self):
        print("Bugün Toplam {} İade Aldınız.".format(self.gunlukToplamIade))

    def KasayiKapat(self):
        baglanti2=sqlite3.connect("gunlukVeriler.db")
        cursor2=baglanti2.cursor()
        sorgu ="CREATE TABLE IF NOT EXISTS gunlukVeriler(GunlukToplamMusteri INT,GunlukToplamCiro INT,GunlukToplamIade INT)"
        cursor2.execute(sorgu)
        baglanti2.commit()
        sorgu2="INSERT INTO gunlukVeriler VALUES(?,?,?)"
        cursor2.execute(sorgu2,(self.gunlukToplamMusteri,self.toplamCiro,self.gunlukToplamIade))
        baglanti2.commit()

        self.gunlukToplamMusteri=0
        self.toplamCiro=0
        self.gunlukToplamIade=0
