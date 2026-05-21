####################################################
# Thing 03 - 21.05.2026
#
# WHAT I LEARNED:
#   - while True runs forever until break stops it
#   - everything that should repeat must be inside the loop
#
####################################################

while True:
    print("===Alamut===")
    print("1 = Backup starten")
    print("2 = Status anzeigen")
    print("3 = Beenden")
    input_raw = input("bitte eine zahl eingeben:")
    input_as_int = int(input_raw)
    if input_as_int == 1:
        print("gäbe es ein programm würde es nun laufen :)")
    elif input_as_int == 2:
        print("status alles ist hell")
    elif input_as_int == 3:
        break
    else:
        print("leider habe ich die eingabe nicht verstanden bitte nur zahlen 1-3")
