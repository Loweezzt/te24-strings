print("--------------------------------Du vaknar upp efter en lång natt sömn...-----------------------------------")
print("------------Du ser dig runt och saker ser inte ur som de brukar, du känner inte igen någonting.------------")
print("---------------------Du sliter dig upp ur sängen och går ut mot fonstret och tittar ut---------------------")
print("-----------Du ser att hela din by har [förstörts] inget finns kvar bara dysterhet och ensamhet.------------")
print("-Du ser att hela din by har [förvandlats] till världen av fortnite, du lägger en quick emote för att fira.-")
choice = input("-----------------------------Vad väljer du att din värld har blivit?---------------------------------------")
available_choices = ("förstörts", "förvandlats")
if "förstörts" in choice:
    print("Du försöker ditt bästa att överleva, med de få resurserna du hittar runt i byn, och ditt ändå mål är att överleva och hitta levande människor som kan hjälpa dig.")
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
