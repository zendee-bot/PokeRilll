import os
from character import polisi,pocong, kuntilanak, kuyang, banispati
from senjata import  ketapel,keris,damagepocong, damagekuntilanak, damagebanispati, damagekuyang, Tombak
from ceritagame import ceritag
from sidefungsi import angkainputulang, angkadariinputsenajata, resetdarah, berantem
cerita=ceritag()


def maingame():
    os.system('cls')
    cerita.pembatass()
    cerita.charinput = input("Masukan Nama dari Karakter kamu : ")
    cerita.pilihsenjata()
    dipake = angkadariinputsenajata()


    if dipake == 1:
            polisii=polisi(name=cerita.charinput,darah=130)
            polisii.gunakan(keris)
    elif dipake == 2:
            polisii=polisi(name=cerita.charinput, darah=110)
            polisii.gunakan(ketapel)
    elif dipake == 3:
            polisii =polisi(name=cerita.charinput, darah=150)
            polisii.gunakan(Tombak)

    Pocong = pocong (name="Pocong", darah=100, senjata=damagepocong)
    Kuntilanak = kuntilanak (name="Kuntilanak", darah=100, senjata=damagekuntilanak)
    Kuyang = kuyang (name="Kuyang", darah=100, senjata=damagekuyang)
    Banaspati = banispati (name="Banaspati", darah=100,senjata=damagebanispati)

    
    cerita.cerita1_1() 
    input("Tekan Enter untuk melanjutkan...")

    cerita.cerita1_2()
    input("Tekan Enter untuk melawan POCONG itu...")


    while Pocong.darah > 0 and polisii.darah > 0:
        berantem(polisii, Pocong)

    if polisii.darah == 0:
        print(f"{polisii.name} telah kalah!")
    else:
        print(f"{Pocong.name} telah dikalahkan!")
        cerita.cerita2_1()
        input("Tekan Enter untuk melanjutkan...")
        
        cerita.cerita2_2()
        input("Tekan Enter untuk melanjutkan...")
        
        cerita.cerita2_3()
        input("Tekan Enter untuk melawan KUNTILANAK itu...")
        resetdarah(polisii)


    while Kuntilanak.darah > 0 and polisii.darah > 0:
        berantem(polisii, Kuntilanak)

    if polisii.darah == 0:
        cerita.kalahh()
        input("Tekan Enter untuk melanjutkan...")
    else:
        print(f"{Kuntilanak.name} telah dikalahkan!")
        cerita.cerita3_1()
        input("Tekan Enter untuk melanjutkan...")
        cerita.cerita3_2()
        input("Tekan Enter untuk melanjutkan...")
        cerita.cerita3_3()
        input("Tekan Enter untuk melanjutakan...")
        cerita.cerita3_4()
        input("Tekan Enter untuk melanjutkan...")
        cerita.cerita3_5()
        input("Tekan Enter untuk melawan KUYANG itu...")
        resetdarah(polisii)
    


    while Kuyang.darah > 0 and polisii.darah > 0:
        berantem(polisii, Kuyang)

    if polisii.darah == 0:
        cerita.kalahh()
        input("Tekan Enter untuk melanjutkan...")
    else:
        print(f"{Kuyang.name} telah dikalahkan!")
        cerita.cerita4_1()
        input("Tekan Enter untuk melanjutkan...")
        cerita.cerita4_2()
        input("Tekan Enter untuk melanjutkan...")
        cerita.cerita4_3()
        input("Tekan Enter untuk melanjutakan...")
        cerita.cerita4_4()
        input("Tekan Enter untuk melanjutkan...")
        cerita.cerita4_5()
        input("Tekan Enter untuk melawan BANASPATI itu...")
        resetdarah(polisii)


    while Banaspati.darah > 0 and polisii.darah > 0:
        berantem(polisii, Banaspati)

    if polisii.darah == 0:
        cerita.kalahh()
        input("Tekan Enter untuk melanjutkan...")
    else:
        print(f"{Banaspati.name} telah dikalahkan!")
        resetdarah(polisii)

    if polisii.darah > 0:
        print(f"{polisii.name} telah mengalahkan semua musuh!")
        cerita.ending1()
        input("Tekan Enter untuk melanjutkan...")
        cerita.ending2()
        input("Tekan Enter untuk melanjutkan...")
        cerita.ending3()
        input("Tekan Enter untuk melanjutakan...")
        cerita.ending4()
        input("Tekan Enter untuk melanjutkan...")
    else:
        print(f"{polisii.name} telah kalah dalam pertarungan!")


os.system('cls')
cerita.judul()
input("Tekan Enter untuk melanjutkan...") 

while True:
    maingame()
    os.system("cls")
    print ("{|=================================|}\n") 
    print("PENGEN MAIN ULANG GA ?\n 1. AKU MAU ULANG BANH..\n 2. UDAHAN AJA")
    ulang = angkainputulang()
    
    if ulang != 1:
        break