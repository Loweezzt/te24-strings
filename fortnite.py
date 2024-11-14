print("--------------------------------Du vaknar upp efter en lång natt sömn...-----------------------------------")
print("------------Du ser dig runt och saker ser inte ur som de brukar, du känner inte igen någonting.------------")
print("---------------------Du sliter dig upp ur sängen och går ut mot fonstret och tittar ut---------------------")
print("-----------Du ser att hela din by har [förstörts] inget finns kvar bara dysterhet och ensamhet.------------")
print("-Du ser att hela din by har [förvandlats] till världen av fortnite, du lägger en quick emote för att fira.-")
run = True
choice = input("-----------------------------Vad väljer du att din värld har blivit?---------------------------------------")
available_choices = ("förstörts", "förvandlats")
if "förstörts" in choice:
    print("Du försöker ditt bästa att överleva, med de få resurserna du hittar runt i byn, och ditt ändå mål är att överleva och hitta levande människor som kan hjälpa dig.")
    print("Men tillslut så ger du upp, det var bara du som överlevde, allt annat är förstört.")
    run = False
elif "förvandlats" in choice:
    print("Du drar till Snopp Doggs crib och lägger en fett emote på han, ni skapar nya fortnite gangster party.")
    print("Snopp Dogg säger att han vet vart de [Brudarna] är men han vet också vart man kan köpa [crip walk].")
choice = input("Väljer du det brudarna eller att lära dig crip walk")
availabl_choices = ("Brudarna", "crip walk")
if "Brudarna" in choice:
    print("Du drar till ett ställe som bara Snopp och några andra vet om och det blir en fet fest, du och snopp har flera brudar var runt en")
elif "crip walk" in choice:
    print("Du och Snopp drar till itemshopen och han bjuder på 500 vbucks och du köper crip walk.")
    print("Sedan crip walkar ni hem till honom igen och njuter av resten av kvällen")
else:
    print("Du vaknade från en dröm, och måste forstätta fara till ditt 9-5 jobb.")
dishes = ["Rått kött", "bananer", "mackor"]
drinks = ["Vatten", "Jägermeister 3l", "Ett flak redbull"]


choice = input("Du börjar dra hem till ditt hus, du känner på dig att att du bor i pleasant park men är inte säker men går dit ändå, du ser ett hus som har ditt namn på sig och går in. Vad gör du nu? \n[1]Tittar om du har nått käk med dig \n[2]DU känner dig törstig, titta om du har något med dig. \n[3]Skit! Du ser något på marken vad kan det vara? \n[4]Något dåligt händer tryck inte här \n \n[5]Något dåligt händer tryck inte här \n[6]Sortera din ryggsäck/backbling \n[7]Vakna \n")
if choice == "1":
        print("Detta är käket jag har i ryggan: ")
        print("#-----------------------")
        for dish in dishes:
            print(dish)
elif choice == "2":
        print("Detta är drickorna jag har: ")
        print("#-----------------------")
        for drink in drinks:
            print(drink)
        print("#-----------------------")
elif choice == "3":
        dish = input("You found a: ")
        dishes.append(dish)
elif choice == "4":
        n = dishes.pop(0, )
        print("Ryggan gick sönder du måste kasta ut en måltid")
elif choice == "5":
        n = drinks.pop(0, )
        print("Ryggan gick sönder du måste kasta ut en dricka")    
elif choice == "6":
        dishes.sort()
elif choice == "7":
        run = False
        print("Du vaknade ur din dröm och hör din mamma skricka att du är sen till skolan.")