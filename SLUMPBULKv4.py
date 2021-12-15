import random
from random import randint

cooking_methods = {
    "nyttigt": {
        "carbs": ["Koka", "Ångkoka", "Blötlägg", "Halstra", "Micra"],
        "proteins": ["Stek", "Koka", "Ugnsbaka", "Micra"],
    },
    "onyttigt": {
        "proteins": ["Grilla", "Marinera och grilla", "Fritera", "Smörstek"],
        "carbs": [
            "Fritera",
            "Koka och lägg på ost",
            "Koka och sautera",
            "Koka i buljong",
        ],
    },
}

proteinlist = []  # lista med alla protein man skriver in
carblist = []  # lista med alla carbs man skriver in
sidelist = []  # lista med alla tillbehör man skriver in
kokbok = {}  # namn på recept -> (protein, carb, side)

print("\033[1m" "Hej och välkommen till slumpbulk!" "\033[0m ")


def main():
    print("Vill du se kokboken, få förslag på recept eller avsluta?")
    svar = input("(kokboken/förslag/avsluta) ")
    if svar == "kokboken":
        print("Här är din kokbok! ")
        textfil()
        print("Skickar tillbaka dig till menyn! \n")
        main()
    elif svar == "förslag":
        sparat = input(
            "Vill du lägga till ingredienser eller få receptförslag direkt? (ingredienser/recept) "
        )
        if sparat == "ingredienser":
            proteinfunktion()
        elif sparat == "recept":
            recept()
        else:
            print("Oops, testa igen")
            main()
    elif svar == "avsluta":
        print("Stänger av...")
        return
    else:
        main()


def textfil():
    f = open("skafferi.txt", "r")
    file_c = f.read()
    print("Dina recept kommer nedan")
    print(" ")
    print(file_c)
    print(" ")
    f.close()
    main()
    klar = input("Skriv klar för att komma till menyn ")
    if klar == "klar":
        main()
    else:
        print("oops, testa igen!")
        textfil()


def proteinfunktion():
    proteininput = input("Vad har du för protein? (klar) ")
    if proteininput == "klar":
        kolhydratfunktion()
        return proteinlist
    else:
        proteinlist.append(proteininput)
        proteinfunktion()
        return proteinlist


def kolhydratfunktion():
    kolhydratinput = input("Vad har du för kolhydrater? (klar) ")
    if kolhydratinput == "klar":
        tillbehörsfunktion()
        return carblist
    else:
        carblist.append(kolhydratinput)
        kolhydratfunktion()
        return carblist


def tillbehörsfunktion():
    tillbehörinput = input("Vad har du för tillbehör? (klar) ")
    if tillbehörinput == "klar":
        göraom()
        return sidelist
    else:
        sidelist.append(tillbehörinput)
        tillbehörsfunktion()
        return sidelist


def göraom():
    ing = input("Har du skrivit i alla dina ingredienser? (ja/nej) ")
    if ing == "ja":
        recept()
    elif ing == "nej":
        print("Vänligen fyll i alla dina ingredienser ")
        proteinfunktion()
    else:
        göraom()


def recept():
    if any([len(l) == 0 for l in [proteinlist, carblist, sidelist]]):
        print("Du behöver fler ingredienser!")
        main()
    else:
        print("Dagens middag")
        recettprotein = random.choice(proteinlist)
        recettcarb = random.choice(carblist)
        recettside = random.choice(sidelist)
        print(f"{recettprotein} {recettcarb} {recettside}")
        svar = input("Är du nöjd med receptet?  (ja/nej) ")
        if svar == "ja":
            print("Härligt att du hittade nåt gott!")
            namnrecept = input("Döp receptet till: ")
            kokbok[namnrecept] = (recettprotein, recettcarb, recettside)
            tillagning(namnrecept)
            return kokbok
        elif svar == "nej":
            recept()
        else:
            recept()


def write_instructions(recipe_name, healthiness):
    end_unhealthy = r"""Servera och njut medans du fortfarande lever"
            !!!!!EXCLAIMER!!!!!
            Slumpbulk inc tar inte ansvar för hjärt- och kärlsjukdomar.
        """
    end_healthy = "Servera och njut av din nyttiga mat"
    random_protein_cooking = random.choice(cooking_methods[healthiness]["proteins"])
    random_carb_cooking = random.choice(cooking_methods[healthiness]["carbs"])
    (protein, carb, side) = kokbok[recipe_name]
    steps = [
        f"Tillagning av {recipe_name} på {healthiness} sätt.",
        f"1. {random_protein_cooking} {protein}",
        f"2. {random_carb_cooking} {carb}",
        f"3. Lägg till {side}",
        end_unhealthy if healthiness == "onyttigt" else end_healthy,
    ]

    with open("skafferi.txt", "a") as f:
        f.write("\n".join(steps))


def tillagning(namnrecept):
    fat = input("Vill du ha receptet onyttigt eller nyttigt? ")
    f = open("skafferi.txt", "a")

    if fat not in ["nyttigt", "onyttigt"]:
        print("Oops, testa igen!")
        tillagning(namnrecept)
    else:
        write_instructions(namnrecept, fat)

    f = open("skafferi.txt", "r")
    file_c = f.read()
    print(file_c)
    f.close()
    print("Receptet är sparat i ditt skafferi, skafferi.txt")
    print("  ")
    main()


main()
