import turtle
import random
import time

# Pencereyi oluştur
window = turtle.Screen()
window.title("Tosbağa Oyunu")
window.bgcolor("light green")
window.setup(width=800, height=600)

# Kaplumbağayı oluştur
kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.color("green")
kaplumbaga.penup()
kaplumbaga.speed(0)

# Puanı ve puan metni için değişkenler
puan = 0
puan_metni = turtle.Turtle()
puan_metni.penup()
puan_metni.color("black")
puan_metni.hideturtle()
puan_metni.goto(0, 260)
puan_metni.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))

# Kaplumbağayı yeni konuma teleport et ve 1 saniye beklet
def yeni_konuma_teleport_ve_bekle():
    global puan
    kaplumbaga.penup()  # Çizimi kapat
    yeni_x = random.randint(-390, 390)
    yeni_y = random.randint(-290, 290)
    kaplumbaga.goto(yeni_x, yeni_y)
    kaplumbaga.pendown()  # Çizimi tekrar aç
    time.sleep(1)  # 1 saniye beklet
    puan_metni.clear()
    puan_metni.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))

# Tıklamaları dinleyen işlev
def tıklamaları_dinle(x, y):
    global puan
    if -50 < x - kaplumbaga.xcor() < 50 and -50 < y - kaplumbaga.ycor() < 50:
        # Tıklanıldığında puanı artır
        puan += 1

# Tıklamaları dinlemeyi başlat
kaplumbaga.onclick(tıklamaları_dinle)

geri_sayim_suresi = 30
geri_sayim_metni = turtle.Turtle()
geri_sayim_metni.hideturtle()
geri_sayim_metni.goto(0, -260)

# Geri sayım işlevi
def geri_sayim():
    global geri_sayim_suresi
    if geri_sayim_suresi > 0:
        geri_sayim_metni.clear()
        geri_sayim_metni.write("Geri Sayım: {} saniye".format(geri_sayim_suresi), align="center", font=("Courier", 24, "normal"))
        geri_sayim_suresi -= 1
        window.ontimer(geri_sayim, 1000)  # 1 saniye (1000 ms) sonra tekrar çağrılacak
    else:
        geri_sayim_metni.clear()
        geri_sayim_metni.write("Oyun Bitti!", align="center", font=("Courier", 24, "normal"))

# Oyun döngüsü
geri_sayim()

# Oyun süresince devam et
while geri_sayim_suresi > -1:
    # Yeni konuma teleport et ve 1 saniye beklet
    yeni_konuma_teleport_ve_bekle()
    window.update()

# Pencereyi kapat
window.mainloop()