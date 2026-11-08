import random
import time
import os
import sys
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
tex = 0
d = 0
iron = 0
oss = 0
while True:
    print("mur-service release V6.1 (OS)")
    v = input("1: sell, 2: check the site, 3: exit, 4: check the cash register, 5: Promo, 6: pet Filya, 7: shop for Filya, antivirus, poison, de (delete everything), 8: create OS: ")
    if v == "1":
        print("what to sell?\n1: samsung\n2: apple\n3: Redmi\n4: Macbook\n5: Alcatel\nos:  ")
        b = input()
        if b == "1":
            d += 12000
            print("you sold Samsung for 12,000 mur money")
            tex += 1
            time.sleep(0.9)
            clear()
        if b == "2":
            d += 50000
            print("you sold Apple for 50,000 mur money")
            tex += 1
            time.sleep(0.9)
            clear()
        if b == '3':
            d += 13000
            print('you sold Redmi for 13,000')
            tex += 1
            time.sleep(0.9)
            clear()
        if b == "4":
            d += 70000
            tex += 1
            print("you sold Macbook for 70,000")
            time.sleep(0.9)
            clear()
        if b == "5":
            d += 4000
            tex += 1
            print("you sold Alcatel for 4,000")
            time.sleep(0.9)
            clear()
        if b == "os":
            if oss >= 1:
                sena = input("price (up to 1000)")
                if sena.isdigit() and 1 <= int(sena) <= 1000:
                    d += int(sena)
                    oss -= 1
            else:
                print("you don't have an OS")
    elif v == "2":
        clear()
        print(f"you have {d}, you're making progress")
    elif v == '3':
        print(f"Bye! You have {d}")
        break
    elif v == '4':
        clear()
        print(f'the cash register has {d}')
    elif v == '5':
        p = input("enter promo code: ")
        if p == "Filya TOP":
            d += 100000
        if p == "one":
            d += 1
        if p == "DeepSeek TOP":
            d += 100000
        if p == "Egor TOP":
            d += 100000
        if p == "Yandex Alice TOP":
            d += 100000
        if p == "Godzik TOP":
            d += 100000
        if p == "Sima TOP":
            d += 100000
    elif v == "report":
        print(f'you have {d} mur money, and {tex} pieces of tech sold, petted Filya {iron} times')  
    elif v == "6":
        clear()
        print("Mur😺")
        time.sleep(0.5)
        print('mur😺')
        time.sleep(0.7)
        iron += 1
        d += 1000
        time.sleep(0.8)
        clear()
    elif v == "7":
       f = input("1: fish 100, 2: mur mint 1% 700, 3: fillet for Filya 1000: ")
       if f == "1":
           if d >= 100:
               d -= 100
               print("you bought a fish\nMurr")
               d += random.randint(100, 200)
               time.sleep(0.7)
               clear()
       elif f == "2":
            if d >= 700:
                d -= 700
                print("you bought mur mint\nMURRRRRRRR\nSHHH\nMeow")
                time.sleep(0.7)
                clear()
       elif f == "3":
            if d >= 1000:
                d -= 1000
                print("you bought a fillet\nmur meoww")
                time.sleep(0.7)
                clear()
    elif v == "antivirus":
        clear()
        for c in range(100):
           time.sleep(0.5)
           print("\033[91mHAhaHahA\033[5m")
           d = float('-inf')
    elif v == "poison":
        for cc in range(100):
            time.sleep(0.1)
            d -= 0.5
            print("-0.5")
    elif v == "de":
        d = 0
        tex = 0
        iron = 0
        print(f"Done {d},{tex},{iron}")
    elif v == "8":
        nameos = input("name: ")
        linuxwindows = input("linux/windows/yours: ")
        print(nameos, linuxwindows)
        oss += 1
    else:
        print('unknown command')
        time.sleep(0.9)
        clear()
#MYR
#SERVICE