import guess as Nummerspel
import Galgje as Galgje

print("==================WELKOM IN DE NANO GAMESTATION==================")
print("                         kies een spel")
print("                         1: Galgje")
print("                         2: Nummerspel")
keuze = input("")
if keuze == "1":
    Galgje()
elif keuze == "2":
    Nummerspel()
