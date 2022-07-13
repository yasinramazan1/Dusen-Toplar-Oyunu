import pygame
import random # Topların yer, renk ve hızını rastgele belirlemek için import edildi.
import time # Oyunun süresini takiip etmek için kullanıldı.
import os # Dosya kontrolü için kullanıldı.
t = time.perf_counter() # Başlama zamanını tutar, oyunu sonlandırmak için kullanılır.
pygame.init() # pygame'in başlangıç işlemlerini yapar.
xmax = 500 # Oyun penceresinin eni (pixel olarak)
ymax =500 # Oyun penceresinin yüksekliği (pixel olarak)
maxSure = 60 # Oyun süresi (saniye türünden)
ycap = 15 # Topların pixel türünden yarıçapı
yinele = True
tanemax = 10 # Oyundaki top sayısı
taneler = [] # Her bir topun koordinat, hız, renk gibi bilgilerini tutar.
renk = (0, 255, 0) # Siyah arkaplan
beyaz = (255, 255, 255)
kirmizi = (255, 0 , 0)
yesil = (0, 255, 0)
mavi = (0, 0, 255)
renkler = []
hizlar = (1, 3, 7, 13)
renkler.append(beyaz)
renkler.append(kirmizi)
renkler.append(yesil)
renkler.append(mavi)
def taneEkle(): # Listeye yeni toplar ekleme fonksiyonu
    while len(taneler)<tanemax:
        x = random.randint(0, xmax-1)
        y = 0
        r = random.randint(0, 3)
        h = hizlar[r]
        taneler.append((x, y, r, h))
def bravo(): # Oyunda yeni rekor olursa bu fonksiyon çağırılır.
    alkis() # Alkış efekti yapan fonksiyon
    text1 = font.render("bravo!", True, beyaz) # render() metodu ile yazı blokları hazırlanır.
    text2 = font.render("yeni rekorun:", True, beyaz)
    text3 = font.render(str(puan), True, beyaz)
    h1 = text1.get_height() # get.height() metodu ile her satırın toplam yüksekliği alınır.
    h2 = text2.get_height()
    h3 = text3.get_height()
    h = h1+h2+h3+20
    y0=(ymax-h)//2 # Yazı bloğunu pencereye düşey olarak ortalama 
    pencere.blit(text1, 
        ((xmax-text1.get_width())//2, y0))
    pencere.blit(text2,
        ((xmax-text2.get_width())//2, y0+h1+10))
    pencere.blit(text3,
        ((xmax-text2.get_width())//2, y0+h2+h2+20))
def plop():
    pygame.mixer_music.load("suDamlasıSesi.mp3")
    pygame.mixer_music.play(0)
def alkis():
    pygame.mixer_music.load("alkisSesi.mp3")
    pygame.mixer_music.play()
def kaydet(puan): # Elde edilen toplam puanı kaydeden fonksiyon
    if os._exists("dusenToplar_puan.txt"):
        with open("dusenToplar_puan.txt", "r") as d:
            s = d.readline()
            if int(s)<puan:
                bravo()
                with open("dusenToplar_puan.txt", "w") as d:
                    d.write(str(puan))
    else:
        bravo()
        with open("dusenToplar_puan.txt", "w") as d:
            d.write(str(puan))
pencere=pygame.display.set_mode((xmax, ymax))
pygame.display.set_caption("Düşen Toplar") # Oyun penceresinin ismini düzenler.
tiktak = pygame.time.Clock()
font = pygame.font.SysFont("Calibri", 48) # Oyundaki skorun yazı stilini ve boyutunu değiştirir.
puan = 0
kaydedildi = False
taneEkle()
while yinele:
    for olay in pygame.event.get(): # Tuş ve mouse olaylarını liste halinde geri döndürür.
        if olay.type==pygame.QUIT:
            yinele = False
        if olay.type==pygame.KEYDOWN:
            if olay.key==pygame.K_ESCAPE:
                yinele = False
                break
        if olay.type==pygame.MOUSEBUTTONDOWN:
            mx,my = olay.pos
            for tane in range(len(taneler)):
                (x, y, r, h) = taneler[tane]
                if (mx+ycap>x) and (mx-ycap<x) and (my+ycap>y) and (my-ycap<y):
                    plop()
                    puan+=h*h
                    taneler.pop(tane)
                    taneEkle()
        if time.perf_counter()-t>maxSure:
            if not kaydedildi:
                kaydet(puan)
                kaydedildi = True
            continue
        pencere.fill("purple") # Oyun alanının arka plan rengini ayarlar.
        for tane in range(len(taneler)):
            (x, y, r, h) = taneler[tane]
            y+=h
            if y>ymax+ycap*2:
                taneler.pop(tane)
                taneEkle()
                continue
            taneler[tane] = (x, y, r, h)
            renk = renkler[r]
            pygame.draw.circle(pencere, renk, [x, y], ycap, 0)
        text = font.render(str(puan), True, beyaz)
        pencere.blit(text,
                    ((xmax-text.get_width())//2, ymax-text.get_height()))
        pygame.display.flip() # Pencere görüntüsünün yeniden düzenlenmesini sağlar.
        tiktak.tick(10) 
pygame.quit()
quit()