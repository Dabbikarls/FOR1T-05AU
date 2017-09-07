
#07/09/2017
#Davíð Freyr Karlsson

val = 0

print("1. Liður ")
print("2. Liður ")
print("3. Liður ")
print("4. Liður ")
print("5. Liður ")
val = int(input("Hvaða lið viltu keyra? "))



#Lidur 1
if val == 1:
    print("ATH Ekki má slá inn sömu tölu tvisvar!")
    tala1 = int(input("Sláðu inn heiltölu"))
    tala2 = int(input("Sláðu inn heiltölu"))
    tala3 = int(input("Sláðu inn heiltölu"))

    if tala1 < tala2 and tala1 > tala3 or tala1 > tala2 and tala1 < tala3:
        print(tala1,"er í miðjunni")
    elif tala2 < tala1 and tala2 > tala3 or tala2 > tala1 and tala2 < tala3:
        print(tala2,"er í miðjunni")
    elif tala3 < tala2 and tala3 > tala1 or tala3 > tala2 and tala3 < tala1:
        print(tala3,"er í miðjunni")
    else:
        print("Þú sláðir inn sömu tölu tvisvar sinnum"),

#Liður2
elif val == 2:
    val2 = 0
    print("1. Tomma í Sentimetra ")
    print("2. Sentimetri í Tommu ")
    val2 = int(input("Hvað viltu breyta. "))
    if val2 == 1:
       tommur = float(input("Sláðu inn tommur"))
       print(tommur * 2.54)
    elif val2 == 2:
        cm = float(input("Sláðu inn sentimetra "))
        print(cm / 2.54)
    else:
        print("Ekki hægt að framkvæma þessa skipun ")
#Liður3
elif val == 3:
    manudur = int(input("Skrifaðu tölu mánaðars"))
    if manudur >= 1 and manudur <= 3:
        print("Nú er dagin tekið að lengja ")
    elif manudur >= 4 and manudur <= 5:
        print("Vorið er komið og grundirnar gróa ")
    elif manudur >= 6 and manudur <= 8:
        print("Núna er sumarið komið með blóm í haga ")
    elif manudur >= 9 and manudur <= 10:
        print("Núna er haustið gengið í garð ")
    elif manudur >= 11 and manudur <= 12:
        print("Núna styttist í jólin ")
    else:
        print("Rangur Innsláttur!")
#Liður4
if val == 4:
    nafn = int(input("Hvað heitir þú? "))
    kyn = int(input("Hvort kk eða kvk? "))
