import random
import colorama
from colorama import Fore, Back ,Style
colorama.init(autoreset=True)

saldo_attuale = int(0)

# pc parts lists
cpu_list = ["intel core i7","intel core i9","intel core i5","amd ryzen 7","amd ryzen 9","amd ryzen 5"]
gpu_list = ["rtx 3060","amd radeon 9070xt","rtx 4080","amd radeon 9060xt","rtx 5090"]
ram_list = ["8gb","16gb","32gb","64gb","96gb","128gb"]
ram_type = ["ddr4","ddr5"]
problem_type = ["thermal problem (lot heat)","not posting (no display)","infected ssd (a virus)","slow pc (pc taking 1min for startup)"]

# random pc build
print(random.choice(cpu_list))
print(random.choice(gpu_list))
print(random.choice(ram_list))
print(random.choice(ram_type))
print("----------------------")
print(Fore.GREEN + "The Problem Is")
problema_attuale = (random.choice(problem_type))
print(problema_attuale)

# problem solving
print("----------------------")
print(Fore.RED + "you can:replace thermal phaste,change components,change ssd,swap from hdd to ssd")
risposta_utente = input("what are you gonna do").lower()

if problema_attuale == "thermal problem (lot heat)" and risposta_utente == "replace thermal phaste":
    saldo_attuale = saldo_attuale + 10
    print(f"Corretto! Il cliente ti ha pagato. Saldo attuale: {saldo_attuale}$")

elif problema_attuale == "not posting (no display)" and risposta_utente == "change components":
    saldo_attuale = saldo_attuale + 10
    print(f"Corretto! Il cliente ti ha pagato. Saldo attuale: {saldo_attuale}$")

elif problema_attuale == "infected ssd (a virus)" and risposta_utente == "change ssd":
    saldo_attuale = saldo_attuale + 10
    print(f"Corretto! Il cliente ti ha pagato. Saldo attuale: {saldo_attuale}$")

elif problema_attuale == "slow pc (pc taking 1min for startup)" and risposta_utente == "swap from hdd to ssd":
    saldo_attuale = saldo_attuale + 10
    print(f"Corretto! Il cliente ti ha pagato. Saldo attuale: {saldo_attuale}$")

else:
    print(Fore.RED + "Sbagliato il cliente non paga +0.")

    