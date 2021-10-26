import random
from random import randint

fatlistprotein = ["Grilla", "Marinera och grilla", "Fritera", "Smörstek"]
goodlistprotein = ["Stek", "Koka", "Ugnsbaka", "Micra"]
fatlistcarb = ["Fritera", "Koka och lägg på ost", "Koka och sautera", "Koka i buljong"]
goodlistcarb = ["Koka", "Ångkoka", "Blötlägg", "Halstra", "Micra"]
proteinlist = [] #lista med alla protein man skriver in
carblist = [] #lista med alla carbs man skriver in
sidelist = [] #lista med alla tillbehör man skriver in
kokbok = {} #namn på recept som nyckel. 
foodlist = [] #namn på recept. Elementen är protein, carb, side för receptet. 
recallaprotein = [] #protein i sparade maträtter i ordning
recallacarb = [] #kolhydrater i sparade maträtter i ordning
recallaside = [] #tillbehör i sparade maträtter i ordning



print("\033[1m" "Hej och välkommen till slumpbulk!" "\033[0m ")



def main():
    print("Vill du se kokboken, få förslag på recept eller avsluta?")
    svar = input("(kokboken/förslag/avsluta) ")
    if svar == "kokboken":
        print("Här är din kokbok! ")
        textfil()
        print("Skickar tillbaka dig till menyn! ")
        print(" ")
        main()
    elif svar == "förslag":
        sparat = input("Vill du lägga till ingredienser eller få receptförslag direkt? (ingredienser/recept) ")
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
    if len(proteinlist+carblist+sidelist) < 3:
        print("Du behöver fler ingredienser!")
        main()
    else:
        print("Dagens middag")
        recettprotein = str((proteinlist[random.randint(0, len(proteinlist)-1)]))
        recettcarb = str((carblist[random.randint(0, len(carblist)-1)]))
        recettside = str((sidelist[random.randint(0, len(sidelist)-1)]))
        print(recettprotein +" " + recettcarb + " " + recettside)
        svar = input("Är du nöjd med receptet?  (ja/nej) ")
        if svar == "ja":
            recallaprotein.append(recettprotein)
            recallacarb.append(recettcarb)
            recallaside.append(recettside)
            print("Härligt att du hittade nåt gott!")
            namnrecept = input("Döp receptet till: ")
            kokbok[str(namnrecept)] = str(recettprotein +" " + recettcarb + " " + recettside)
            foodlist.append(namnrecept)
            tillagning(namnrecept)
            return kokbok
        elif svar == "nej":
            recept()
        else:
            recept()      

def tillagning(namnrecept):
    fat = input("Vill du ha receptet onyttigt eller nyttigt? ")
    if fat == "onyttigt":
        f = open("skafferi.txt", "a")
        f.write(
            "Tillagning av " + namnrecept + " på " + fat + " sätt." + "\n"
            "1. " + fatlistprotein[random.randint(0, 3)]+" " + recallaprotein[foodlist.index(namnrecept)]+"\n"
            "2. " + fatlistcarb[random.randint(0, 3)]+" " + recallacarb[foodlist.index(namnrecept)]+"\n"
            "3. " + "Lägg till " + recallaside[foodlist.index(namnrecept)]+"\n"
            "Servera och njut medans du fortfarande lever"+"\n"
            "!!!!!EXCLAIMER!!!!!"+"\n"
            "Slumpbulk inc tar inte ansvar för hjärt- och kärlsjukdomar."+"\n"
            " " + "\n")
        
        f.close()
        f = open("skafferi.txt", "r")
        file_c = f.read()
        print(file_c)
        f.close()
        print("Receptet är sparat i ditt skafferi, skafferi.txt")
        main() 
    elif fat == "nyttigt":
        f = open("skafferi.txt", "a")
        f.write( 
            "Tillagning av " + namnrecept + " på " + fat + " sätt. " + "\n"
            "1. " + goodlistprotein[random.randint(0, 3)]+" " + recallaprotein[foodlist.index(namnrecept)]+"\n"
            "2. " + goodlistcarb[random.randint(0, 3)]+" " + recallacarb[foodlist.index(namnrecept)]+"\n"
            "3. " + "Lägg till " + recallaside[foodlist.index(namnrecept)]+"\n"
            "Servera och njut av din nyttiga mat"+"\n"
            " " + "\n")
        f.close()
        f = open("skafferi.txt", "r")
        file_c = f.read()
        print(file_c)
        f.close()
        main()
    else:
        print("Oops, testa igen!")
        tillagning(namnrecept)
        

 
main()
