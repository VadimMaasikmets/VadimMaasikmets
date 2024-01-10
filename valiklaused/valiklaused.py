from random import *


a=randint(-100,200)
if a%2==0:
    print("Juhuslik av on",a)
    print(a,"-paaris arv")

if a>0:
    print(a, "suurem kui 0")
else:
    print(a,"väiksem kui 0 või võrdne 0-ga")

#<0,>100 ei soobi, 0-59-"2",60-75-"3",76-90-"4",91-100-"5"
if a<0 or a>100:
    print("Viga")
elif a>=0 and a<=59:
    print("hind 2")
elif a>=60 and a<=75:
    print("hind 3")
elif a>=76 and a<=90:
    print("hind 4")
else:
    print("hind 5")



#1
name= input("sissestage eesnimi: ")
age = int(input("vanus: "))
if name.upper()== "JUKU":
    if age <=1 and age >6:
        print("pilet on tasuta")
    elif age >=6 and age <14:
        print("lastepilet")
    elif age >=15 and age <=65:
        print("täispilet")
    elif age >65:
        print("sooduspilet")
    elif age <0 and age >100:
        print("viga")
    print("Lähme kinno")
else:
    print("sorry, ainult Juku läheb kinno")

#2
print("Kirjutage teie nimed")
a= input("nimi 1: ")
b= input("nimi 2: ")
if a.upper()=="A" and b.upper()=="B" or a.upper()=="B" and b.upper()=="A":
    print("Pinginaabrid")
else:
    print("Nad ei ole naabrid")
#3
pikkus= float(input("sisesta toa pikkus meetrites: "))
laius= float(input("sisesta toa laius meetrites: "))
ppindala= pikkus * laius
print(f"toa põranda pindala: {ppindala} ruutmeetrit.")
remont= input("kas soovite teha remonti (jah/ei)?").lower()
if remont== "jah":
    ruutmeetri= float(input("sisesta ruutmeetri põranda hind: "))
    koguhind= ppindala * ruutmeetri
    print(f"põranda vahetamise koguhind: {koguhind} eurot.")
else:
    print("Tänan. Edu teile.")
#4
alghind= float(input("sisesta alghind: "))
if alghind > 700:
    soodustus = 0.3 * alghind
    soodustusega= alghind - soodustus
    print(f"30% soodustusega hind: {soodustusega}")
else:
    print("alghind ei ole surrem kui 700, soodustust ei kohaldata.")
#5
temp= float(input("sisesta temperatuur kraadides: "))
if temp > 18:
    print("temperatuur on üle kaheksateistkümne kraadi, see on soovitatav toassoojus talvel.")
else:
    print("temperatuur ei ole üle kaheksateistkümne kraadi.")
#6
pikkus= float(input("sisesta oma pikkus meetrites: "))
lpiik= 1.60
ppiik= 1.80
if pikkus < lpiik:
    print("Sa oled lühike")
elif lpiik <= pikkus <= ppiik:
    print("sa oled keskmise pikkusega")
else:
    print("sa oled pikk")
#7