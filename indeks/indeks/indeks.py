print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Sissestage eesnimi:")
print(f"{nimi}, oi kui ilus nimi!")
a= int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
if a== 1:
    while True:
        try:

            pikkus=float(input("Pikkus:"))
            mass=float(input("Mass:"))
            indeks=mass /(0.01*pikkus)**2
            if pikkus>0 and mass>0:
                print(f"{nimi}Sinu keha indeks on {indeks}")
                print("Pikkus ja mass sisetanud ja indeks on leidnud")
                if indeks>= 0 and indeks<16:
                    print("Tervise ohtlik alakaal")
                elif indeks>=16 and indeks<19:
                    print("Alakaal")
                elif indeks>=19 and indeks<25:
                    print("Normaalkaal")
                elif indeks>=25 and indeks<30:
                    print("Ülekaal")
                elif indeks>=30 and indeks<35:
                    print("Rasvumine")
                elif indeks>=35 and indeks<40:
                    print("Tugev rasvumine")
                elif indeks>=40:
                    print("Tervisele ohtlik rasvumine")
                print("")
                print(f"Kohtumiseni, {nimi}! Igavesti Sinu, Python")
            break
        except:
            print("on vaja andmed> kui 0")    
else:            
     print("Kahju! See on väga kasulik info")
