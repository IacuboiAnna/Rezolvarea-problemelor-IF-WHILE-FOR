anul=int(input("Introduceti anul:"))
if ((anul>=1000) and (anul<10000)):
    if (anul%12==0):
        print("Anul maimutei")
    if (anul%12==1):
        print("Anul cocosului")
    if (anul%12==2):
        print("Anul cainelui")
    if (anul%12==3):
        print("Anul porcului")
    if (anul%12==4):
        print("Anul sobolanului")
    if (anul%12==5):
        print("Anul boului")
    if (anul%12==6):
        print("Anul tigrului")
    if (anul%12==7):
        print("Anul iepurelui")
    if (anul%12==8):
        print("Anul dragonului")
    if (anul%12==9):
        print("Anul sarpelui")
    if (anul%12==10):
        print("Anul calului")
    if (anul%12==11):
        print("Anul oaiei")
else:
    print("Introduceti un an din patru cifre!")   