
name = input("Wat is jouw naam?")

print("Welkom bij de eindopdracht")

print ("We gaan nu beginnen met de eindopracht")

print("Wat zijn jouw favoriete games?") 

def favorite_game(name):
    print("Mijn favoriete games zijn", name)

favorite_game("Super Mario Odyssey")
favorite_game("GTA V")
favorite_game("Fortnite")

print("Was de eindopdracht goed?")
cijfer=input("Geef de eindoprdacht een cijfer")
if int(cijfer) > 6:
    print("Voldoende")
else:
    print("Onvoldoende")


