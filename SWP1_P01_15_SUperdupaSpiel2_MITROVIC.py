import time 
import os
import sys
import pygame

sleep_time = 0                     #Time wird eingefügt um Zeit einzufügen

relativerpfad_outro = 'Musik\\Endmusik.mp3'
absoluterpfad_outro = os.path.abspath(os.path.join(sys.path[0], relativerpfad_outro))
def outro():
    pygame.init()
    pygame.mixer.music.load(absoluterpfad_outro)
    pygame.mixer.music.play()  # Startzeitpunkt in Sekunden angeben


##########Final Quelle: https://pixabay.com/de/music/search/genre/epische%20klassik/
relativerpfad_finalt = 'Musik\\final-Training.mp3'
absoluterpfad_finalt = os.path.abspath(os.path.join(sys.path[0], relativerpfad_finalt))
def finalfightmusik():
    pygame.init()
    pygame.mixer.music.load(absoluterpfad_finalt)
    pygame.mixer.music.play(start=5)  # Startzeitpunkt in Sekunden angeben
    time.sleep(7)
    pygame.mixer.music.stop()
    pygame.quit()

relativerpfad_finalfight = 'Musik\\final-fight.mp3'
absoluterpfad_finalfight = os.path.abspath(os.path.join(sys.path[0], relativerpfad_finalfight))
def finaltrainingmusik():
    pygame.init()
    pygame.mixer.music.load(absoluterpfad_finalfight)
    pygame.mixer.music.play(start=5)  # Startzeitpunkt in Sekunden angeben
    time.sleep(7)
    pygame.mixer.music.stop()
    pygame.quit()
##########Final


relativerpfad_MusikinTaverne = 'Musik\\gongive.mp3'
absoluterpfad_MusikinTaverne = os.path.abspath(os.path.join(sys.path[0], relativerpfad_MusikinTaverne))
def MusikinTaverne():                                        #quelle: https://youtu.be/fGx6K90TmCI
    pygame.init()

    pygame.mixer.music.load(absoluterpfad_MusikinTaverne) # Pfad zur Musikdatei angeben
    pygame.mixer.music.play()

    time.sleep(219) 

    pygame.mixer.music.stop()
    pygame.quit()

relativerpfad_playPARTYMusik = 'Musik\\PartyMusik.mp3'
absoluterpfad_playPARTYMusik = os.path.abspath(os.path.join(sys.path[0], relativerpfad_playPARTYMusik))
def playPARTYMusik():                   #quelle: https://www.youtube.com/watch?v=OPf0YbXqDm0
    pygame.init()

    pygame.mixer.music.load(absoluterpfad_playPARTYMusik) # Pfad zur Musikdatei angeben
    pygame.mixer.music.play()

    time.sleep(270)

    pygame.mixer.music.stop()
    pygame.quit()

relativerpfad_playbarMusik = 'Musik\\Musik.mp3'
absoluterpfad_playbarMusik = os.path.abspath(os.path.join(sys.path[0], relativerpfad_playbarMusik))
def playbarMusik():                 #Quelle: Star wars Episode IV
    pygame.init()

    # Paket Sys für relativen pfad
    pygame.mixer.music.load(absoluterpfad_playbarMusik) # Pfad zur Musikdatei angeben
    pygame.mixer.music.play()

    # Musik für 5 Sekunden abspielen
    pygame.time.delay(11000)

    pygame.mixer.music.stop()
    pygame.quit()

relativerpfad_FotovonKind = 'Foto\\FotovonKind.jpg'
absoluterpfad_FotovonKind = os.path.abspath(os.path.join(sys.path[0], relativerpfad_FotovonKind))
def print_Fotovonkind():
    # Quelle: geeksforgeeks.org/python-display-images-with-pygame/
    pygame.init()
    scrn = pygame.display.set_mode((750, 600))
    pygame.display.set_caption('Foto von Kind')
    Fotovonkind = pygame.image.load(absoluterpfad_FotovonKind).convert() # Stichwort: Relativer Pfad!
    scrn.blit(Fotovonkind, (0, 0))
    pygame.display.flip()
    status = True
    while status:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                status = False
    pygame.quit()

Code = []
Cash = 0


def clear():
    os.system('cls ')

Techniken = []
Inventar = []                                           #Inventar und Status werden erstellt
Status = [100,0,]                                       #Leben, Angriff,
                                                


Bernhardshop = 'Geschlossen'

HerculesSchwert = 'Das Schwert des Hercules(Tötet jeden gegener instant)[75.000]'
Whiskey = 'Whiskey[50]'
Trank_2 = 'Trank*2(Verdoppelt alle Werte)[650]'
HermesSchuhe = 'Die Schuhe des Hermes(Nie wieder Damage)[100.000]'
SamuraiSchwert = 'Das Schwert der Samurai(+700ATK)[350]'
Umkehr_Trank = 'Umkehr Trank(Dreht dein HP & ATK um)[300]'
Waren = [HerculesSchwert, Whiskey, Trank_2, HermesSchuhe, SamuraiSchwert, Umkehr_Trank]

Produkte = ['Das Schwert des Hercules', 
            'Whiskey', 'Trank*2', 'Die Schuhe des Hermes', 'Das Schwert der Samurai', 'Umkehr Trank']

def Werte():                                           #Status ausgabe
    clear()
    print('HP', Status[0])
    print('ATK', Status[1])
    input()

def Monolog():                                          #Monolog wird definieret
        return '*Monolog beginnt/endet*'

def Abfrage():                                                      #Wichtgiste Optionen werden definiert
    print('I Inventar öffnen')
    print('S Status öffnen')
    if Bernhardshop == 'offen':
        print('L Shop öffnen')

def WarenP ():
    print('\n'.join(Waren))

def Shop():        
    global Cash
    clear()
    print('Willkomen im Shop')
    print('Bernhard: Was willst du haben ')
    print('Gib das ein was nicht in einer eigenen Klammer steht')
    print(f'Du hast {Cash} Kronen ')
    WarenP()
    eingabe = input()
    if eingabe in Produkte and eingabe == 'Das Schwert des Hercules':
        if Cash >= 75000:
            Produkte.remove(eingabe)
            Waren.remove (HerculesSchwert)
            Cash = Cash - 75000
            Inventar.append(HerculesSchwert)
            input(f'Du hast {eingabe} für 75.000 Kronen gekauft')
        else:
            print('Du hast kein Geld dafür')
            time.sleep(sleep_time)
    elif eingabe in Produkte and eingabe == 'Whiskey':
        if Cash >= 50:
            Produkte.remove(eingabe)
            Waren.remove (Whiskey)
            Cash = Cash - 50
            Inventar.append(Whiskey)
            input(f'Du hast {eingabe} für 50 Kronen gekauft')
        else:
            print('Du hast kein Geld dafür')
            time.sleep(sleep_time)
    elif eingabe in Produkte and eingabe == 'Trank*2':
        if Cash >= 650:
            Produkte.remove(eingabe)
            Waren.remove (Trank_2)
            Cash = Cash - 650
            Inventar.append(Trank_2)
            input(f'Du hast {eingabe} für 650 Kronen gekauft')
        else:
            print('Du hast kein Geld dafür')
    elif eingabe in Produkte and eingabe == 'Die Schuhe des Hermes':
        if Cash >= 100000:
            Produkte.remove(eingabe)
            Waren.remove (HermesSchuhe)
            Cash = Cash - 100000
            Inventar.append(HermesSchuhe)
            input(f'Du hast {eingabe} für 100.000 Kronen gekauft')
        else:
            print('Du hast kein Geld dafür')
    elif eingabe in Produkte and eingabe == 'Das Schwert der Samurai':
        if Cash >= 350:
            Produkte.remove(eingabe)
            Waren.remove (SamuraiSchwert)
            Cash = Cash - 350
            Inventar.append(SamuraiSchwert)
            Techniken.append('Schwert')
            input(f'Du hast {eingabe} für 350 Kronen gekauft')
        else:
            print('Du hast kein Geld dafür')
    elif eingabe in Produkte and eingabe == 'Umkehr Trank':
        if Cash >= 300:
            Produkte.remove(eingabe)
            Waren.remove (Umkehr_Trank)
            Cash = Cash - 300
            Inventar.append(Umkehr_Trank)
            input(f'Du hast {eingabe} für 300 Kronen gekauft')
        else:
            print('Du hast kein Geld dafür')
    else:
        print('Das was sie eingegeben haben gibt es nicht zu verkaufen')
        time.sleep(sleep_time)


def InventarP ():
    print('\n'.join(Inventar))


HerculesSchwertausgerüstet = 'Nein'
SamuraiSchwertausgerüstet = 'Nein'
Schwertausgerüstet = 'Nein'
Schuheausgerüstet = 'Nein'
HermesSchuheausgerüstet = 'Nein'
Brustpanzerausgerüstet = 'Nein'

def Inventory():                                              #Inventar aufrufen wird defieniert
    global inventareingabe
    global Schwertausgerüstet
    global HerculesSchwertausgerüstet
    global SamuraiSchwertausgerüstet
    global Schuheausgerüstet
    global vorwert
    global HermesSchuheausgerüstet
    global Brustpanzerausgerüstet
    while True:    
        clear()
        if len(Inventar) == 0:
            print('[Du hast Momentan nichts im Inventar]')
        else:
            InventarP()
        if Schwertausgerüstet == 'Ja':
            print('F Um das Schwert abzulegen')
        if Schuheausgerüstet == 'Ja':
            print('G Um die Schuhe abzulegen')
        if Brustpanzerausgerüstet == 'Ja':
            print ('O Um den Brustpanzer abzulegen')
        print('Gib ein was du nutzen willst')
        print('Falls du nichts tun willst/kannst drück Enter')
        inventareingabe = input()
        
        if inventareingabe == 'G' and Schuheausgerüstet == 'Ja':
            clear()
            if HermesSchuheausgerüstet == 'Ja':
                Inventar.append(HermesSchuhe)
                Schuheausgerüstet = 'Nein'
                HermesSchuheausgerüstet = 'Nein'
            print('Du hast deine Schuhe verstaut')
            time.sleep (sleep_time*2)
        
        elif inventareingabe == 'O' and Brustpanzerausgerüstet == 'Ja':
            clear()
            Inventar.append('Kampf Brustpanzer [+100HP]')
            Brustpanzerausgerüstet = 'Nein'
            Status[0] -= 100
            print('Dein HP sinkt um 100')
            print('Du hast dein Brustpanzer verstaut')
            time.sleep (sleep_time*2)
        
        elif inventareingabe == 'F' and Schwertausgerüstet == 'Ja':
            clear()
            print('Du hast das Schwert in dein Inventar gelegt')
            Schwertausgerüstet = 'Nein'
            if HerculesSchwertausgerüstet == 'Ja':
                Inventar.append(HerculesSchwert)
                Status[1] = vorwert
                HerculesSchwertausgerüstet = 'Nein'
                print('Dein ATK wird zu dem Wert den er vorher hatte') 
            elif SamuraiSchwertausgerüstet == 'Ja':
                Inventar.append(SamuraiSchwert)
                Techniken.remove('Schwert')
                Status[1] -= 700
                SamuraiSchwertausgerüstet = 'Nein'
                print('Dein ATK sinkt um 700')    
            print('Du hast dein Schwert abgelegt')
            time.sleep (sleep_time*2)

        if inventareingabe in Inventar and inventareingabe == 'Glock':
            print('Die Glock wird automatisch ausgerüstet')
            time.sleep (sleep_time)
        elif inventareingabe in Inventar and inventareingabe == 'Trank':
            Status[0] = Status[0]*8
            Inventar.remove('Trank')
            clear()
            print('Du hast den Trank getrunken')
            time.sleep (sleep_time)
            print('Dein HP wert wird 8 mal so hoch')
            time.sleep (sleep_time*2)
            
        elif inventareingabe == 'Das Schwert des Hercules'and HerculesSchwert in Inventar:
            if Schwertausgerüstet == 'Ja':
                print('Du kannst nicht zwei Schwerter ausrüsten')
                time.sleep (sleep_time*2)
            else:
                vorwert = Status[1]
                Status[1] = 'Unlimited'
                Inventar.remove(HerculesSchwert)
                clear()
                print('Du hast das Schwert ausgerüstet')
                HerculesSchwertausgerüstet = 'Ja'
                Schwertausgerüstet = 'Ja'
                time.sleep (sleep_time*2)
            
        elif inventareingabe == 'Whiskey'and Whiskey in Inventar:
            Inventar.remove(Whiskey)
            clear()
            print('Der Whiskey war geil')
            time.sleep (sleep_time*2)

        elif inventareingabe == 'Trank*2'and Trank_2 in Inventar:
            Inventar.remove(Trank_2)
            clear()
            print('Deine Werte werden alle verdoppelt')
            Status[0] = Status[0]*2
            Status[1] = Status[1]*2
            time.sleep (sleep_time*2)
        
        elif inventareingabe == 'Die Schuhe des Hermes'and HermesSchuhe in Inventar:
            HermesSchuheausgerüstet = 'Ja'
            Inventar.remove(HermesSchuhe)
            clear()
            print('Du kannst nun kein Schaden erleiden')
            Schuheausgerüstet = 'Ja'
            time.sleep (sleep_time*2)
        
        elif inventareingabe == 'Das Schwert der Samurai'and SamuraiSchwert in Inventar:
            if Schwertausgerüstet == 'Ja':
                print('Du kannst nicht zwei Schwerter ausrüsten'  )
                time.sleep (sleep_time*2)
            else:
                Inventar.remove(SamuraiSchwert)
                vorwert = Status[1]
                Status[1] += 700
                clear()
                print('Dein ATK steigt um 700')
                Schwertausgerüstet = 'Ja'
                SamuraiSchwertausgerüstet = 'Ja'
                time.sleep (sleep_time*2)
        elif inventareingabe == 'Umkehr Trank':
            x = 0
            x = Status[1]
            Status[1] = Status[0]
            Status[0] = x
            Inventar.remove(Umkehr_Trank)
            print('Du hast deine Werte verdreht')
            time.sleep(sleep_time*2)
        
        elif inventareingabe == 'Kampf Brustpanzer'and 'Kampf Brustpanzer [+100HP]' in Inventar:
            Inventar.remove('Kampf Brustpanzer [+100HP]')
            clear()
            print('Du hast den Brustpanzer ausgerüstet')
            Status[0] += 100
            Brustpanzerausgerüstet = 'Ja'
            time.sleep (sleep_time*2)

        elif inventareingabe == '':
            break

Bernhardbar = 'Nein'
nachgeschrien = 'Nein'

def ENDEGELENDE():
    clear()
    Inventar[:] = []
    Status[:] = [100,0]
    Techniken[:] = []
    global nachgeschrien
    nachgeschrien = 'Nein'
    global Bernhardbar
    Bernhardbar = 'Nein'
    global Brustpanzerausgerüstet
    Brustpanzerausgerüstet = 'Nein'
    global Schuheausgerüstet
    Schuheausgerüstet = 'Nein'
    global HerculesSchwertausgerüstet
    HerculesSchwertausgerüstet = 'Nein'
    global SamuraiSchwertausgerüstet
    SamuraiSchwertausgerüstet = 'Nein'
    global Schwertausgerüstet
    Schwertausgerüstet = 'Nein'
    global Bernhardshop
    Bernhardshop = 'Geschlossen'
    global Bernhardkenngelernt
    Bernhardkenngelernt = 'Nein'
    global Raum1
    Raum1 = 'nicht erledigt'
    global Spinne
    Spinne = 'Nicht Tot'
    global Raum2
    Raum2 = 'nicht erledigt'
    global Raum3
    Raum3 = 'nicht erledigt'   
    while True:
        eingabe = input('Du hast das Spiel Durchgespielt. Vielleicht solltest du es nochmal versuchen und paar geheimnisse entdecken \nWenn du nochmal spielen willst gib ein A. \nWenn du nich mehr Magst gib ein B. \n')
        if eingabe == 'A':
            pygame.mixer.music.stop()
            break
        elif eingabe == 'B': 
            sys.exit()
    if eingabe == 'A':
            Start()
        
def Tot():                                                    #Tot wird definiert
    clear()
    Inventar[:] = []
    Status[:] = [100,0]
    Techniken[:] = []
    global nachgeschrien
    nachgeschrien = 'Nein'
    global Bernhardbar
    Bernhardbar = 'Nein'
    global Brustpanzerausgerüstet
    Brustpanzerausgerüstet = 'Nein'
    global Schuheausgerüstet
    Schuheausgerüstet = 'Nein'
    global HerculesSchwertausgerüstet
    HerculesSchwertausgerüstet = 'Nein'
    global SamuraiSchwertausgerüstet
    SamuraiSchwertausgerüstet = 'Nein'
    global Schwertausgerüstet
    Schwertausgerüstet = 'Nein'
    global Bernhardshop
    Bernhardshop = 'Geschlossen'
    global Bernhardkenngelernt
    Bernhardkenngelernt = 'Nein'
    global Raum1
    Raum1 = 'nicht erledigt'
    global Spinne
    Spinne = 'Nicht Tot'
    global Raum2
    Raum2 = 'nicht erledigt'
    global Raum3
    Raum3 = 'nicht erledigt'   
    while True:
        eingabe = input('Du bist GESTORBEN \nWenn du nochmal spielen willst gib ein A. \nWenn du nich mehr Magst gib ein B. \n')
        if eingabe == 'A':
            break
        elif eingabe == 'B': 
            sys.exit()
    if eingabe == 'A':
        Start()


def Start ():
    clear()
    print('_(ʕ•́ᴥ•̀ʔ)_')                                      #Das Logo
    print(' \__|__/')
    print('    |   ')
    print('   / \  ')
    print('  /   \  ')
    print(' ')

    input('Drücken sie Enter um aufzuwachen')      #Eingabe zum Starten

    print(Monolog())                                               #Prolog Text anfang
    time.sleep (sleep_time)
    print ('Wo bin ich ? Was ist das hier?')
    print(Monolog())
    time.sleep (sleep_time)
    print ('*Du schaust dich um*')
    time.sleep (sleep_time)
    print ('*Du erkennst ein Tattoo an deinem linken Arm*')
    time.sleep (sleep_time)
    print(Monolog())
    time.sleep (sleep_time)
    print ('Es sieht so als würde ein Teil fehlen? Komisch.')
    time.sleep (sleep_time)
    print(Monolog())

    print ('Was Machst du jetzt?') 
    time.sleep(sleep_time)                                                 #Prolog Text Ende
            
            
    K1()

         

def K1 ():                                                                                                 #Erstes Kapitel wird definiert
    while True:
        clear()
        print('Du siehst links eine Schlucht, rechts einen Fluss, vor dir gehts tiefer in den Wald')
        print ('Was Machst du jetzt?') 
        time.sleep(0.5)
        print('A Gerade aus in den Wald \nB Nach rechts Zum Fluss \nC Nach links in zur Schlucht')
        Abfrage()
        eingabe = input()
        if eingabe == ('I'):
            Inventory()
        elif eingabe == ('S'):
            Werte()
        elif eingabe == 'B':
            break
        elif eingabe == 'C':
            break
        elif eingabe == 'A':
            break
        # elif eingabe == 'L':
        #     Shop()

    if eingabe == 'A':
        clear()
        print('Du Gehst weiter in den Wald')
        time.sleep(sleep_time)
        print('Du siehst 2 Dinge.') 
        time.sleep(sleep_time+0.5)
        print('Du siehst eine Brücke. \nDu siehst ein Haus.')
        time.sleep(sleep_time)
        K2()
    elif eingabe == 'B':
        K1k2()
    elif eingabe == 'C':
        K1k3()

def K1k2 ():                                                                                    #abzweigunG definieren
    while True:
        clear()
        print('Du Siehst einen Fluss ')
        print('Was möchtest du jetzt tun?')
        print('A Zurück gehen \nB Das Wasser Trinken \nC Ins den Fluss springen')
        Abfrage()
        eingabe = input()
        if eingabe == ('I'):
            Inventory()
        elif eingabe == ('S'):
            Werte()
        elif eingabe == 'D':
            Inventar.append('Knarre')
        elif eingabe == 'B':
            break
        elif eingabe == 'C':
            break
        elif eingabe == 'A':
            break
            

    if eingabe == 'A':
        K1()
    elif eingabe == 'B':
        Status[0] += 10
        print('Das Wasser hat gut geschmeckt. Du kriegst 10 HP Plus')
        time.sleep(2)
        print('*Dir wird schwindelig*')
        Monolog()
        time.sleep(sleep_time/1.5)
        print('Was zum fi...')
        time.sleep(sleep_time/1.5*0.5)
        Monolog()
        time.sleep(sleep_time/1.5)
        print('*du fällst Tot um*')
        time.sleep(sleep_time/1.5)
        Tot()
    elif eingabe == 'C':
        print('*Du hälst den Strom des Wassers nicht aus und gehst Unter*')
        time.sleep(1.5)
        Tot()
        
def K1k3() :                                                                                        #Zweite abzweigung wird definiert
    global nachgeschrien
    while True: 
        clear()
        print('Du siehst die Schlucht etwas besser')
        time.sleep(1)
        if nachgeschrien == 'Ja':
            print('Was willst du jetzt machen?')
            print('Er hört dich mit Sicherheit nicht, vielleicht solltest du zu ihm rüber? Aber wie?')
            print('A zurück gehen \nC in die Schlucht springen')
            eingabe = input('')
            Abfrage()
            if eingabe == ('I'):
                Inventory()
            elif eingabe == ('S'):
                Werte()
            elif eingabe == 'C':
                break
            elif eingabe == 'A':
                break
        else:
            print('und erkennst auf der anderen Seite der Schlucht')
            print('einen Kleinen Stand worin eine Person Steht.')
            print('Auf dem Stand steht Fett "Wolfgangs Schrott."')
            print('Was willst du jetzt machen? \nDu könntest nach ihm schreien aber ob er dich hört?')
            eingabe = input('A zurück gehen \nB nach ihm schreien \nC in die Schlucht springen\n')
            Abfrage()
            if eingabe == ('I'):
                Inventory()
            elif eingabe == ('S'):
                Werte()
            elif eingabe == 'B':
                nachgeschrien = 'Ja'
            elif eingabe == 'C':
                break
            elif eingabe == 'A':
                break
    if eingabe == 'A':
        K1()
    elif eingabe == 'C':
        Tot()


def K2():                                                                           #Das 2.te Kapitel wird definiert
    while True:
        clear()
        print('Was machst du jetzt?')
        print('A In das Haus gehen \nB Über die Brücke gehen \nC Zurück gehen')
        Abfrage()
        eingabe = input()
        if eingabe == ('I'):
            Inventory()
        elif eingabe == ('S'):
            Werte()
        elif eingabe == 'B':
            break
        elif eingabe == 'C':
            break
        elif eingabe == 'A':
            break
    if eingabe == 'A':
        K3geschichte()
    elif eingabe == 'B':
        K2k2Geschichte()
    elif eingabe == 'C':
        K1()

def K2k2Geschichte():
    clear()
    print('Du Brücke ist Wackelig')
    print('Du gehst über sie')
    print('Du bist auf der anderen Seite')
    print('Da ist nix außer einem kleinem Stand')
    K2k2()
    
def K2k2():                                                                             #Die Kapitel Möglichkeit von Kapitel 2 wird weiterentwickelt
    while True: 
        clear()
        print('Was machst du jetzt?')
        print('A Du gehst zurück \nB Zum Stand gehen')
        Abfrage()
        eingabe = input()
        if eingabe == ('I'):
            Inventory()
        elif eingabe == ('S'):
            Werte()
        elif eingabe == 'B':
            break
        elif eingabe == 'A':
            break
    if eingabe == 'A':
        K2()
    elif eingabe == 'B':
        K2k2m2()

Bernhardkenngelernt = 'Nein'                                                         #eingestellt ob man bernhard schon kennengelernt hat, wichtig damit man dynamische entscheidungen treffen kann                                                          

def K2k2m2():
    global Bernhardkenngelernt
    clear()
    if Bernhardkenngelernt == 'Ja':
        print('Du hast schon mit dem Händler gesprochen')
        time.sleep(sleep_time)
        print('Du hast nichts mehr zu tun')
        time.sleep(sleep_time)
        K2k2()
                                                                            #Die Kapitel Möglichkeit von Kapitel 2 möglichkeit 2 wird weiterentwickelt
    else:
        print('Im Stand befindet sich ein Händler')
        time.sleep(sleep_time)
        while True:
            Eingabekennenlernenbernhard = input('Möchtest du mit ihm reden ? \nA ja \nB nein \n')                                           
            if Eingabekennenlernenbernhard == 'A':
                break
            if Eingabekennenlernenbernhard == 'B':
                break
        clear()    
        if Eingabekennenlernenbernhard == 'A':
            print('Fremder: Hey, na du. Willkommen bei Wolfgangs Schrott.')
            time.sleep(sleep_time)
            print('Du: Hallo, wer bist du?')
            time.sleep(sleep_time)
            print('Fremder: Ich bin Bernhard, Bernhard Ratschiener.')
            time.sleep(sleep_time)
            while True:
                eingabe = input('A Wieso hast du einen Stand hier im nirgendwo? \nB Wo bin ich? \nC gehen \n')
                if eingabe == 'A':
                    clear()
                    print('Du: Wieso hast du einen Stand hier im nirgendwo.')
                    time.sleep(sleep_time)
                    print('Bernhard: Der Stand gehört eigentlich nicht mir.')
                    time.sleep(sleep_time)
                    print('Bernhard: Das war der Stand meines Bruders, Wolfgang.')
                    time.sleep(sleep_time)
                    print('Bernhard: Ich war Lehrer an einer Schule, eigentlich bin ich ja Informatiker.')
                    time.sleep(sleep_time)
                    print('Bernhard: Mein Bruder verschwand vor 3 Jahren.')
                    time.sleep(sleep_time)
                    print('Bernhard: Deswegen wollte ich ihn aufsuchen. ')
                    time.sleep(sleep_time*1.5)
                    print('Bernhard: Er war nirgends zu finden.')
                    time.sleep(sleep_time)
                    print('*Bernhards miene verzieht sich')
                    time.sleep(sleep_time*1.5)
                    print('*Bernhard Lächelt wieder*')
                    time.sleep(sleep_time)
                    print('Bernhard: Seitdem Halte ich den Stand hier intakt.')
                    time.sleep(sleep_time)
                    print('Du: Du redest aber schon viel.')
                    time.sleep(sleep_time)
                    print('*Bernhard guckt beleidigt*')
                    time.sleep(sleep_time)
                    print('Du: Tut mir Leid wegen deinem Bruder.')
                    time.sleep(sleep_time)
                    print('*Bernhard Lächelt noch mehr als vorher*')
                    Bernhardkenngelernt = 'Ja'
                elif eingabe == 'B':
                    clear()
                    print('Du: Wo bin ich hier ?')
                    time.sleep(sleep_time)
                    print('Bernhard: Du Befindst dich in Joshumatera.')
                    time.sleep(sleep_time)
                    print('Bernhard: Eine Wunderbare Welt, eine von vier.')
                    print('Bernhard: Ich persönlich bin aus Svartalfheim, genauer einem Dorf namens Floridsdorf.')
                    time.sleep(sleep_time)
                    print('Bernhard: Wir Zwergen sind zwar klein und fett, aber wir sind auch sehr Intelligent.')
                    time.sleep(sleep_time)
                    print('Du: Ich unterbrich dich mal, genug jetzt von dir.')
                    time.sleep(sleep_time)
                    print('Du: Jetzt erzähl mal von Joshumeirgendwas.')
                    time.sleep(sleep_time)
                    print('Bernhard: Natürlich tut mir leid.')
                    time.sleep(sleep_time*0.5)
                    print('Bernhard: In Joshumatera ist das unendlich möglich.')
                    time.sleep(sleep_time)
                    print('Bernhard: Ich stamme zwar von Svartalfheim.')
                    print('Bernhard: aber ich zog in jungen jahren hier her, vorallem wegen Kandor.')
                    while True:
                        time.sleep(sleep_time)
                        print('A Was ist Kandor? B Nix sagen')
                        eingabe = input()
                        if eingabe == 'A':
                            clear()
                            print('Bernhard: Kandor ist eine Stadt, Die Stadt.')
                            print('Bernhard: In dieser Stadt ist alles Möglich, naja es war alles Möglich.')
                            time.sleep(sleep_time)
                            print('Du: Was soll das heißen?')
                            time.sleep(sleep_time)
                            print('Bernhard: Es gab einen Krieg, Kandor wurde Zerstört und auch alle seine übereste.')
                            time.sleep(sleep_time)
                            print('Bernhard: In Kandor gabe es alles, in dieser Stadt war nunmal alles möglich')
                            time.sleep(sleep_time/1.5*0.5)
                            print('*Bernhards verzieht sich kurz*')
                            time.sleep(sleep_time)
                            break
                        elif eingabe == 'B':
                            break
                    clear()
                    time.sleep(sleep_time)
                    print('Bernhard: in jedem fall bin ich jetzt hier.')
                    time.sleep(sleep_time)
                    print('Bernhard: Ich bin jetzt so ziemlich Glücklich.')
                    Bernhardkenngelernt = 'Ja'
                elif eingabe == 'C':
                    break
            if eingabe == 'C':
                K2k2m2()   
        elif Eingabekennenlernenbernhard == 'B':
            K2k2()

def K3geschichte ():                                                                                #Geschichte von k3 wird defieniert
    clear()
    print('Das Haus ist alt und ranzig.')
    time.sleep(sleep_time)
    print('Du siehst ein Foto auf der Kücheninsel. ')
    time.sleep(sleep_time)
    print('Du siehst eine veranzte Couch, man kann aber drauf schlafen.')
    time.sleep(sleep_time)
    print('Du siehst noch einen Kühlschrank')
    time.sleep(sleep_time)
    K3()

def K3 ():                                                                                          #K3 wird definiert
    while True:
        clear()
        if 'Glock' in Inventar :
            print('Was willst du machen? \nA Auf der Couch schlafen \nB Das Foto ansehen \nD rausgehen')
            Abfrage()
            eingabe = input()
            if eingabe == 'B':
                break
            elif eingabe == 'A':
                break
            elif eingabe == 'D':
                break
            elif eingabe == ('I'):
                Inventory()
            elif eingabe == ('S'):
                Werte()
        
        else:
            print('Was willst du machen? \nA Auf der Couch schlafen \nB Das Foto ansehen \nC Den Kühlschrank dursuchen \nD rausgehen')
            Abfrage()
            eingabe = input()
            if eingabe == 'B':
                break
            elif eingabe == 'C':
                break
            elif eingabe == 'A':
                break
            elif eingabe == 'D':
                break
            elif eingabe == ('I'):
                Inventory()
            elif eingabe == ('S'):
                Werte()
    
    if eingabe == 'A':
        K4geschichte()
    elif eingabe == 'B':
        print_Fotovonkind()
        input('Drück Enter um zurück zu gehen')
        K3()
    elif eingabe == 'C':
        while True:
            print('In dem Kühlschrank ist eine Glock.')
            time.sleep(sleep_time)
            print('Willst du sie mitnehmen ? \nA Ja \nB Nein')
            eingabe = input()
            if eingabe == 'A':
                Inventar.append('Glock')
                K3ohneWaffe()
            elif eingabe == 'B':
                K3()
    elif eingabe == 'D':
        K2()

def K3ohneWaffe():                                                                                          #K3 Funktion wenn die Waffe genommen wurde
    while True:
        clear()
        print('Was willst du machen? \nA auf der Couch schlafen \nB Das Foto ansehen \nD rausgehen')
        Abfrage()
        eingabe = input()
        if eingabe == 'B':
            break
        elif eingabe == 'C':
            break
        elif eingabe == 'A':
            break
        elif eingabe == 'D':
            break
        elif eingabe == ('I'):
            Inventory()
        elif eingabe == ('S'):
            Werte()
    if eingabe == 'A':
        K4geschichte()
    elif eingabe == 'B':
        print_Fotovonkind()
        input('Drück Enter um zurück zu gehen')
        K3()
    elif eingabe == 'D':
        K2()

def K4geschichte():                                                                                 #K4 Geschichte wird definiert
    clear()
    print('*Du schläfst ein*')
    time.sleep(sleep_time)
    print('Du hörst wie sich die Tür öffnet und schließt')
    time.sleep(sleep_time)
    print('*Du wachst auf*')
    time.sleep(sleep_time)
    print('Fremde: Na hallo mein Süßer')
    time.sleep(sleep_time)
    print('Du: Wer bist du?')
    time.sleep(sleep_time)
    print('Fremde: Ich? Wer ich bin. Haha. Das hat dich nicht zu interessieren.')
    time.sleep(sleep_time)
    print('Du: Sagen sie mir wer sie sind!')
    time.sleep(sleep_time)
    print('Fremde: Na zwing mich doch.')
    time.sleep(sleep_time)
    K4()

def K4():                                                                               #K4 wird definiert
    while True:
        clear()
        print('Willst du kämpfen? \nA Ja \nB Nein')
        Kampfeingabe = input()
        if Kampfeingabe == 'A':
            break
        elif Kampfeingabe == 'B':
            break   
    if Kampfeingabe == 'A':
        if 'Glock' in Inventar:
            Inventar[0] == 'Glock'
            print('Du zückst deine Glock')
            time.sleep(sleep_time)
            print('Du Zielst auf Sie und drückst ab')
            time.sleep(sleep_time)
            print('Deine Waffe löst sich in rauch auf')
            Inventar.pop (0)
            time.sleep(sleep_time)
            print('Na, na ,na')
            time.sleep(sleep_time)
            print('So leicht wird es nicht')
            time.sleep(sleep_time)
            K4kampf()
        else:    
            K4kampf()

    elif Kampfeingabe == 'B':
        print('Die Frau schnipst')
        time.sleep(sleep_time)
        print('Du Implodierst und zerfetzt von innen heraus')
        time.sleep(sleep_time)
        Tot()

def K4kampf():                                                                                      #Der Kampf wird definiert der geschieht allerdings in text nd aktion
    clear()
    print('Du läufst auf die Frau zu')
    time.sleep(sleep_time)
    print('Du schlägst zwar mit voller Kraft, aber sie manövriert dich aus.')
    time.sleep(sleep_time)
    print('Die Frau schnippst')
    time.sleep(sleep_time)
    print('Du Befindest dich in der Luft')
    time.sleep(sleep_time)
    print('Du fällst mit einer unglaublichen Geschwindigkeit')
    time.sleep(sleep_time)
    print('Du knallst auf dem Boden')
    time.sleep(sleep_time)
    print('Es tut aber nicht weh, es ist wie wenn man auf ein Trampolin fällt.')
    time.sleep(sleep_time)
    print('Du befindest dich auf einer Wiese')
    time.sleep(sleep_time)
    print('Die Fremde Person fängt wieder an mit dir zu reden')
    time.sleep(sleep_time)
    print('Fremde: Ich bin enttäuscht ich dachte immer du wärst ein starker Duelant')
    time.sleep(sleep_time)
    print('Du: Hör mal zu alte, ich weiß nicht wer du bist.')
    time.sleep(sleep_time)
    print('Du: Zur Hölle nochmal, ich weiß nicht mal mehr wer ich bin!')
    time.sleep(sleep_time)
    print('Fremde: Ist das so? Nun, dein Name ist Nero.')
    time.sleep(sleep_time)
    print('Fremde: Jetzt weißt du wer du bist, Jetzt KÄMPF!')
    time.sleep(sleep_time)
    print('Du läufst auf sie drauf')
    time.sleep(sleep_time)
    print('Du kriegst ein Flashback')
    time.sleep(sleep_time)
    print('Tausend Bildern donnern auf dein Kopf, so sehr dass es weh tut')
    time.sleep(sleep_time)
    print('Du brichst zussamen und fällst zu Boden')
    time.sleep(sleep_time)
    print('Du flüsterst: Bruder')
    time.sleep(sleep_time)
    print('Fremde: Dein Bruder war eine Kakerlake MEHR NICHT.')
    time.sleep(sleep_time)
    print('Du: Sei LEISE!')
    print('Du schleuderst einen Feuerball gegen sie')
    time.sleep(sleep_time)
    print('Die Frau wird weggeschleuddert')
    time.sleep(sleep_time)
    print('Die Fremde Kehrt zurück und sieht sehr angepisst aus')
    time.sleep(sleep_time)
    print('Sie will angreifen')
    time.sleep(sleep_time)
    print('Doch bist wirst plötzlich wegteleportiert')
    time.sleep(sleep_time)
    K5Geschichte()
    
def K5Geschichte():                                                                                                     #K5Geschichte wird definiert
    clear()
    print('Du wachst auf')
    time.sleep(sleep_time)
    while True:
        clear()
        print('Du bist vor einem Wirtshaus.')
        time.sleep(sleep_time)
        print('Was machst du jetzt')
        print('A reingehen \nB sich umsehen ob man noch was findet')
        Abfrage()
        eingabe = input()
        if eingabe == 'A':
            break
        elif eingabe == 'B':
            break
        elif eingabe == ('I'):
            Inventory()
        elif eingabe == ('S'):
            Werte()
    if eingabe == 'A':
        K5Geschichte2()
    elif eingabe == 'B':
        K6()

def K5Geschichte2():                                                                                            #Noch mehr Geschichte für K5
    clear()
    print('Laute Musik ertönt')
    playbarMusik()
    clear()
    print('Das Wirthaus ist voller Leute')
    time.sleep(sleep_time)
    print('Barkeeper: Hey Nero, Bro lang nicht gesehen wie läufts?')
    time.sleep(sleep_time)
    print('Du: Tut mir leid, aber wer bist du?')
    time.sleep(sleep_time)
    print('Barkeeper: Scheißen man, du musst ja ordentlich auf den Kopf gefallen sein.')
    time.sleep(sleep_time)
    print('Barkeeper: Ich bin Kelvin ich und du haben mal einen Wette abgeschlossen.')
    time.sleep(sleep_time)
    print('Kelvin: Seitdem kriegst du bei mir Free Drinks für den Rest deines Lebens.')
    time.sleep(sleep_time)
    print('Du: Das sagst du mir? Nicht sehr profitabel von dir gedacht.')
    print('Du: Egal jetzt, Gib mir ein paar drinks ich könnte was gebrauchen.')
    time.sleep(sleep_time)
    print('Kelvin: Für dich immer.')
    time.sleep(sleep_time)
    print('Nero kriegt einen guten Whyskey in die Hand gedrückt, und fängt sich ein großes Lächeln ein ')
    time.sleep(sleep_time)
    print('Du: JUHUUUUUUUUUUU PARTYYYYYY')
    time.sleep(sleep_time)
    while True:
        clear()
        eingabe = input('A Party mitfeiern(kann danach nicht übersprungen werden) \nB überspringen \n')
        if eingabe == 'B':
            break
        elif eingabe == 'A':
            break
    if eingabe == 'A':
        playPARTYMusik()
    K5Geschichte3()

def K5Geschichte3():                                                                                #Noch mehr Geschichte für K5
    clear()
    print('Es ist morgen')
    time.sleep(sleep_time)
    print('Nero ist komplett verkatert')
    time.sleep(sleep_time)
    print('Kelvin: Guten Morgen mein Zuckerberli.')
    time.sleep(sleep_time)
    print('Du: Boah man Kelvin, mein Kopf brummt.')
    print('Du: Was willst du von mir?')
    time.sleep(sleep_time)
    print('Kelvin: Da du gestern mir klar gemacht hast dass du absolut keine Ahnung mehr hast wer du bist, müssen wie Trainieren.')
    time.sleep(sleep_time)
    print('Du: Warum das denn?')
    time.sleep(sleep_time)
    print('Kelvin: Gestern hast du mit deinem Feuerball Melvins arsch abgefakelt, und auch Tinas drittes Bein.') 
    time.sleep(sleep_time)
    print('Kelvin: Genauso musste der Billiard Tisch leiden')
    time.sleep(sleep_time)
    print('Du: Das kann ja mal passieren, na gut von mir aus aber nur ausnahmsweise.')
    time.sleep(sleep_time)
    clear()
    print('Ihr begebt euch zu einem Trainingsgelände unter der Bar')
    time.sleep(sleep_time)
    print('Kelvin: Ok, also First of, du besitzt gewisse Techniken du die Meistern kannst.')
    time.sleep(sleep_time)
    print('Du: Was den für Techniken?')
    time.sleep(sleep_time)
    print('Kelvin: Naja, es gibt so einiges was man erlernen kann.')
    time.sleep(sleep_time)
    print('Kelvin: Aber um klein anzufangen, der Feuerball wäre ein guter anfang.')
    time.sleep(sleep_time)
    print('Du: Also ich bin ready.')
    time.sleep(sleep_time)
    print('Kelvin: Ok Nun Folgendes, konzentrier dich, schau auf die Puppe und feuere mit voller Kraft.')
    time.sleep(sleep_time)
    print('Kelvin: Allerdings musst du deine Negativen und sehr hasserfüllten Emotionen verwenden.')
    time.sleep(sleep_time)
    K5()

def K5():                                                                                           #K5 wird definiert
    while True:
        clear()
        print('Was willst du tun?')
        print('A Den Feurball auf die Puppe abfeuern \nB warten \nC Weggehen')
        Abfrage()
        eingabe = input()
        if eingabe == 'C':
            break
        elif eingabe == 'A':
            break
        elif eingabe == ('I'):
            Inventory()
        elif eingabe == ('S'):
            Werte()
        elif eingabe == 'B':
            clear()
            print('Kelvin: Worauf wartest du? Mach jetzt!')
            time.sleep(sleep_time)
            print('Du: Na gut, stress nicht.')
            time.sleep(sleep_time)
    if eingabe == 'A':
        clear()
        print('Du verbrennst du Pupe')
        Techniken.append('Feuerball')
        Status[1] += 500
        time.sleep(sleep_time)
        print('Du hast eine neue Techniken erlernt -Feuerball-')
        time.sleep(sleep_time)
        print('Die Technik -Feuerball- verstärkt dein ATK um 500')
        time.sleep(sleep_time)
        print('Kelvin: Das sollte vorerst reichen, Die anderen Fähigkeiten wirst du auch noch lernen.')
        time.sleep(sleep_time)
        print('Du: Wann?')
        time.sleep(sleep_time)
        print('Kelvin: Das ergibt sich schon.')
        time.sleep(sleep_time)
        print('Du: Ich geh dann mal bisschen den Wald erkunden.')
        time.sleep(sleep_time)
        print('Du: Ich muss diese Frau finden.')
        time.sleep(sleep_time)
        print('Kelvin: Na gut, stirb mir nur nicht weg, viel Spaß.')
        time.sleep(sleep_time)
        K6()
    elif eingabe =='C':
        clear()
        print('Kelvin: Ehrlich du willst ohne Training raus?')
        time.sleep(sleep_time)
        print('Du: Joa wird eh easy')
        time.sleep(sleep_time)
        print('Du: Ich geh dann mal bisschen den Wald erkunden.')
        time.sleep(sleep_time)
        print('Kelvin: Viel Spaß.')
        K6()

def K6():
    clear()
    print('Du findest dich in dem Wald wieder')
    time.sleep(sleep_time)
    print('Du bewunderst schöne Blumen im Wald. Doch du Hörst aufeinmal ein lautes Monster schreien.')
    time.sleep(sleep_time)
    print('Ein Riesieger Troll taucht auf')
    time.sleep(sleep_time)
    print('Er greif dich an')
    if 'Feuerball' in Techniken:                                                                                ########################Ratschiener wegen den Techniken Fragen###################
        print('Du brennst ein Fettes Loch in den Troll. Dein Feurball war 1200° Heiß:')
        time.sleep(sleep_time)
        K7Geschichte()
    else:
        print('Der nimmt dich in die Hand und schleudert dich herum.')
        time.sleep(sleep_time)
        print('Er nimmt dich, haut dich auf den Boden und setzt sich auf dich.')
        print('Du erstickst an den Fürzen vom Troll')
        time.sleep(sleep_time*2)
        Tot()

def Taverne():                                                                                                          #Taverne wird definiert
    global Bernhardbar
    clear()
    print('Musik startet')
    playbarMusik()
    print('Kelvin: Hey, Na was gibts ?')
    count_alcohol = 0
    while True:
        clear()
        print('Was willst du machen?')
        if Bernhardbar == 'Ja':
            print('A Musik hören \nB Ein schlückchen Trinken \nC mit Bernhard reden \nD Gehen')
            Abfrage()
        else:
            print('A Musik hören \nB Ein schlückchen Trinken \nC Gehen')
            Abfrage()
        eingabe=input()
        if Bernhardbar == 'Ja' :
            if eingabe == 'A':
                clear()
                print('Musik startet')
                MusikinTaverne()
                print('Die Musik war Geil')
                time.sleep(sleep_time)
            elif eingabe == 'B':
                print('Dir hat es geschmeckt aber der Alkohol wirkt nicht')
                time.sleep(sleep_time)                                                        ##########Ko Gehen##############
                count_alcohol += 1
            elif eingabe == 'C':
                print('Bernhard: Los, erlege den Drachen. Ich glaub an dich')
                time.sleep(sleep_time)
            elif eingabe == 'D':
                break
            elif eingabe == ('I'):
                Inventory()
            elif eingabe == ('S'):
                Werte()
        else:
            if eingabe == 'A':
                MusikinTaverne()
                print('Die Musik war Geil')
                time.sleep(sleep_time)
            elif eingabe == 'B':
                print('Dir hat es geschmeckt aber der Alkohol wirkt nicht')
                time.sleep(sleep_time)                                                        ##########Ko Gehen##############
                count_alcohol += 1
            elif eingabe == 'C':
                break
            elif eingabe == ('I'):
                Inventory()
            elif eingabe == ('S'):
                Werte()

        
        if count_alcohol > 5:
            print('Du bist Knockout gegangen')
            time.sleep(sleep_time)
            print('Du musst jetzt warten bis du wieder aufwachst')
            time.sleep(sleep_time)
            schlaf = 0
            while True:
                clear()
                print('Du schläfst noch')
                time.sleep(1)
                schlaf += 1
                if schlaf >= 5:
                    break
            print('Du bist wieder wach')
            print('Jetzt kannst du wieder auf die Kake hauen')
            count_alcohol = 0
            time.sleep(sleep_time)
            clear()

    if eingabe == 'C':
        print ('Du gehst wieder zurück')
        time.sleep(sleep_time)
    if eingabe == 'D':
        print ('Du gehst wieder zurück')
        time.sleep(sleep_time)


def K7Geschichte():                                                                                                 #K7Geschichte wird definiert
    clear()
    print('Du gehst Tiefer in den Wald, Nach einer Zeit findest du im Wald eine Höhle')
    time.sleep(sleep_time)
    print('Auf der Höhle ist eine Tafel')
    time.sleep(sleep_time)
    print('Auf der Tafel steht:')
    print('hawara kimmst du hier ause bist a Floridsdorfer, da rennt jeder grindiger cusche weg')
    time.sleep(sleep_time)
    print('Übersetzt heißt das: Wenn du es in der Höhle überlebst, wird jeder vor dir wegrennen')
    time.sleep(sleep_time)
    K7()

def K7():                                                                                                           #K7 wird definiert
    while True:
        clear()
        print('Du bist vor dem Dungeon')
        print('Was machst du jetzt ?')
        print('A Den Dungeon betreten \nB Zurück in die Taverne gehen \nC Nochmal die Tafel lesen')
        Abfrage()
        eingabe= input()
        if eingabe == 'A':
            break
        elif eingabe == 'B':
            Taverne()
            time.sleep(sleep_time)
            print('Du bist wieder zurück')
            time.sleep(sleep_time)
        elif eingabe == 'C':
            clear()
            time.sleep(sleep_time)
            print('Auf der Tafel steht:')
            print('hawara kimmst du hier ause bist a Floridsdorfer, da rennt jeder grindiger cusche weg')
            time.sleep(sleep_time)
            print('Übersetzt heißt das: Wenn du es in der Höhle überlebst, wird jeder vor dir wegrennen')
            input('Klick Enter um zurückzugehen')
        elif eingabe == ('I'):
            Inventory()
        elif eingabe == ('S'):
            Werte()              
    if eingabe == 'A':
        K8Geschichte()

Spinne = 'Nicht Tot'                                                                                              #eingestellt ob man die Spinne getötet hat, wichtig damit man nicht immerwieder gegen die Spinne käpmfen muss
def K8Geschichte():                                                                                               #Geschichte zu K8
    if Spinne == 'Tot':
        K9()
    else:
        clear()
        print('Der Dungeon ist Dunkel und Feucht')
        time.sleep(sleep_time)
        print ('Aufeinmal taucht eine riesen Spinne auf ')
        time.sleep(sleep_time)
        print (f'Momentan beherscht du die Techniken {Techniken}')
        time.sleep(sleep_time)
        print('Du musst nun kämpfen')
        time.sleep(sleep_time)
        K8()



def K8 ():                                                                                          #K8 wir definiert
    global Spinne
    while True:
        clear()
        print('Was willst du anwenden?')
        time.sleep(sleep_time)
        if len(Techniken) >= 1 :
            print(f'Du berherscht die folgenden Techniken: {Techniken} \nA nichts tun')
            print('Gib ein was du nutzen willst?')
            Technikenauswahl = input()
            if Technikenauswahl == 'Feuerball':
                break
            elif Technikenauswahl == 'A':
                print('Die Spinne hat dich gegessen')
                time.sleep(sleep_time)
                Tot()
        else:
            print('Die Spinne hat dich gegessen')
            time.sleep(sleep_time)
            Tot()
    if Technikenauswahl == 'Feuerball':
        clear()
        print('Du hast der Spinne den Kopf weggeschmolzen.')
        time.sleep(sleep_time)
        print('Du bemerkst dass du einen kleinen Fakel mit deinem kleinen Finger erzeugen kannst')
        time.sleep(sleep_time)
        print('Du hast eine neue Techniken erlent -Fingerfakel-')
        time.sleep(sleep_time)
        Techniken.append('Fingerfakel')
        Spinne = 'Tot'
    K9Geschichte()

def K9Geschichte():                                                                                                   #K9 Geschichte wird definiert
    clear()
    print('Du nutzt die Fingerfakel um dich in der Höhle zurecht zu finden ')
    time.sleep(sleep_time)
    print('Du erkennst 4 Gänge, über 3 der Gänge ist je ein Tier')
    time.sleep(sleep_time)
    print('eine Eule, ein Einhorn, ein Falke')
    time.sleep(sleep_time)
    print('Auf der 4ten Tür sind alle 3 zu erkennen')
    time.sleep(sleep_time)
    print('Auf der 4ten Tür, ist auch eine Tabelle 5 Spalten, 2 Zeilen ')
    time.sleep(sleep_time)
    print('Die Zahlen sind von links nach rechts, von 0-9')
    time.sleep(sleep_time*2)
    K9()

def K9():                                                                                                                   #K9 wird definiert
    clear()
    print('Alle Türen sind offen bis auf die vierte')
    time.sleep(sleep_time)
    print('Es scheint wohl ein zu Rätsel sein')
    time.sleep(sleep_time)
    while True:
        clear()
        print('Was machst du nun ?')
        time.sleep(sleep_time)
        print('A Durch die erste Tür gehen \nB Durch die zweite Tür gehen \nC Durch die dritte gehen \nD Zur 4ten Tür gehen \nE Aus dem Dungeon rausgehen ')
        Abfrage()
        time.sleep(sleep_time)
        eingabe = input()
        if eingabe == 'A':
            break
        elif eingabe == 'B':
            break
        elif eingabe == 'C':
            break
        elif eingabe == 'D':
            break
        elif eingabe == 'E':
            break
        elif eingabe == ('I'):
            Inventory()
        elif eingabe == ('S'):
            Werte()
    if eingabe == 'A':
        K9k2()
    elif eingabe == 'B':
        K9k3()
    elif eingabe == 'C':
        K9k4()
    elif eingabe == 'D':
        K10Zugang()
    elif eingabe == 'E':
        K7()  

Raum1 = 'nicht erledigt'                                                         #eingestellt ob man den Code hat, wichtig damit man dynamische entscheidungen treffen kann

def Puppenimdungeonhauen():                                                                                                                                     #Der Kampf bei anwendung von Techniken
    global Raum1
    global Puppeneingabedungeon
    if 'Tornadokick' in Techniken:
        while True:
            clear()
            print(f'Du beherscht die folgenden Techniken: {Techniken}')
            time.sleep(sleep_time)
            print('Welche Technik willst du gegen die Puppen anwenden? Gib A ein um aufzuhören') 
            Puppeneingabedungeon = input()
            if Puppeneingabedungeon == 'Tornadokick':
                break
            elif Puppeneingabedungeon == 'Feuerball':
                clear()
                print('Der Feuerball schleudert die Puppe nach hinten, aber sie verbrennt nicht')
                time.sleep(sleep_time)
            elif Puppeneingabedungeon == 'Fingerfakel':
                clear()
                print('Es ist heller geworden, mehr passiert nicht')
                time.sleep(sleep_time)
            elif Puppeneingabedungeon == 'A':
                break
        if Puppeneingabedungeon == 'Tornadokick':
            clear()
            print('Die Puppe wird wegeschleudert')
            time.sleep(sleep_time)
            print('Die Puppe implodiert')
            time.sleep(sleep_time)
            print('Es springt ein Zettel raus')
            time.sleep(sleep_time)
            print('Auf dem Zettel steht 2107')
            time.sleep(sleep_time)
            print('Du Solltest den Code bei der 4ten Tür probieren ')
            time.sleep(sleep_time)
            Raum1 = 'Erledigt'
            Code.append('Tür 1= 2107')
    else:
        while True:
            clear()
            print(f'Du berherscht die folgenden Techniken: {Techniken}')
            time.sleep(sleep_time)
            print('Welche Technik willst du gegen die Puppen anwenden? Gib A ein um aufzuhören')
            Puppeneingabedungeon = input()
            if Puppeneingabedungeon == 'Feuerball':
                print('Der Feuerball schleudert die Puppe nach hinten, aber verbrennt sie nicht')
                time.sleep(sleep_time)
            elif Puppeneingabedungeon == 'Fingerfakel':
                print('Es ist heller geworden, mehr passiert nicht')
                time.sleep(sleep_time)
            elif Puppeneingabedungeon == 'A':
                break
def KungfuBuch():                                                                                                                   #Erlernen von Tehnicken möglich/nicht mnöglich aufgrund bereits können
    if 'Tornadokick' in Techniken:
        clear()
        print('Du kannst das Buch schon')
        time.sleep(sleep_time)
        print('Du legst das Buch zurück')
        time.sleep(sleep_time)
    else:    
        clear()
        print('Auf dem Buch steht: Der Weg des Kungfu')
        time.sleep(sleep_time)
        print('Das Buch lehrt einen über den Weg des Kungfu')
        time.sleep(sleep_time)
        while True:
            print('Was willst du machen ?')
            print('A Das Buch lesen \nB Das Buch zurücklegen')
            eingabe = input()
            if eingabe == 'A':
                break
            elif eingabe == 'B':
                break
        if eingabe == 'A':
            clear()
            print('Du kannst nun die Wege des Kung fu, Du kannst nun den Tornadokick')
            time.sleep(sleep_time)
            print('Du hast eine neue Technik erlernt -Tornadokick-')
            Techniken.append('Tornadokick')
            Status[1] += 300
            print('Die Technik -Tornadokick- verstärkt dein ATK um 300')
            time.sleep(sleep_time)
        elif eingabe == 'B':
            print('Du legst das buch zurück')
            time.sleep(sleep_time)



def K9k2():                                                                                                                 #Geschichte für die erste Tür
    clear()
    if Raum1 == 'Erledigt':
            print('Du bist mit diesem Raum schon fertig')                                                                   
            time.sleep(sleep_time)
            print('Du hast hier nichts mehr zu tun')
            time.sleep(sleep_time*1.5)
            K9()
    else:
        print('Du gehst den Gang entlang und kommst in einen Traningsraum')
        time.sleep(sleep_time*2)
        print('Du bist in einem Raum in dem eine Trainingspuppe und ein Buch sind')
        time.sleep(sleep_time)
        while True:
            clear()      
            print('Was willst du machen?')
            print('A Das Buch lesen \nB Mit der Puppe Trainieren \nC Zurückgehen')
            Abfrage()
            Puppeneingabe = input()
            if Puppeneingabe == 'A':
                KungfuBuch()
            elif Puppeneingabe == 'B':
                Puppenimdungeonhauen()
                if Puppeneingabedungeon == 'A':
                    pass
                else:
                    break
            elif Puppeneingabe == 'C':
                break
            elif Puppeneingabe == ('I'):
                Inventory()
            elif Puppeneingabe == ('S'):
                Werte()
        if 'Tornadokick' in Techniken:
            K9k2m2()
        if Puppeneingabe == 'C':
            K9()

def K9k2m2():                                                                                                                         #Die Möglichkeiten innerhalb der ersten Tür 
    while True:
        clear()
        print('Was willst du machen?')
        print('A Das Buch lesen \nB Mit der Puppe Trainieren \nC Zurückgehen')
        Abfrage()
        Puppeneingabe = input()
        if Puppeneingabe == 'A':
            KungfuBuch()
        elif Puppeneingabe == 'B':
            clear()
            print('Die Puppe ist zerstört')
            time.sleep(sleep_time)
        elif Puppeneingabe == 'C':                                                          
            break
        elif Puppeneingabe == ('I'):
            Inventory()
        elif Puppeneingabe == ('S'):
            Werte()
    if Puppeneingabe == 'C':
        K9()

def Riesenschlangeangriff():
    Status[0] -= 500

Raum2 = 'nicht erledigt'                                                                #wichtige für Entscheidungen

def K9k3():                                                                                                                 #Geschichte der zweiten Tür
    global Lebenvorkampf
    global ATKvorkampf
    Lebenvorkampf = Status[0]
    ATKvorkampf = Status[1]
    if Raum2 == 'Erledigt':
        print('Du bist mit diesem Raum schon fertig')                                                                   
        time.sleep(sleep_time)
        print('Du hast hier nichts mehr zu tun')
        time.sleep(sleep_time*1.5)
        K9()
    else:
        clear()                                                                                                                 #Die zu einem Kampf führt
        print('Du gehst den Gang entlang ')
        time.sleep(sleep_time)
        print('Du bist jetzt in einer leeren Höhle auf einmal siehst du eine Riesenschlange')
        time.sleep(sleep_time)
        print('Sie beachtet dich nicht')
        time.sleep(sleep_time)
        print('Die Riesenschlange hat eine Kampfkraft von 500ATK und ein Lebensstatus von 600HP')                            #Schlange hat {600Hp} & {500ATK}
        time.sleep(sleep_time)
        print(f'Du hast eine Kampfkraft von {Status[1]}ATK und ein Lebensstatus von {Status[0]}HP')
        time.sleep(sleep_time)
        while True:  
            print('Willst du die Schlange bekämpfen?')
            time.sleep(sleep_time)
            print('A Ja \nB Nein und zurückugehen')
            Abfrage()
            eingabe = input()
            if eingabe == 'A':
                break
            elif eingabe == 'B':
                break
            elif eingabe == ('I'):
                Inventory()
            elif eingabe == ('S'):
                Werte()
        if eingabe == 'A':
            if Status[1] >= 500 and Status[0] > 500:
                clear()
                print('Du kannst es mit der Riesenschlange aufnehmen')
                time.sleep(sleep_time)
                while True :
                    clear()
                    print(f'Du berherscht die folgenden Techniken: {Techniken}')
                    time.sleep(sleep_time)
                    print('Was willst du anwenden?')
                    eingabe = input()
                    if eingabe == 'Feuerball':
                        break
                    elif eingabe == 'Tornadokick':
                        break
                    elif eingabe == 'Fingerfakel':
                        break
                if eingabe == 'Feuerball':                                                                      #Feuerball eingabe
                    clear()
                    print('Du machst der Riesenschlange eine Schaden von 500')
                    time.sleep(sleep_time)
                    print('Die Riesenschlange hat nun 100HP & 500ATK')
                    time.sleep(sleep_time)
                    print('Die Riesenschlange hat dich angegriffen, Du verlierst 500HP')            #Zu diesem Zeitpunkt kann man Maximal 800 Hp haben und 800ATK
                    Riesenschlangeangriff()
                    time.sleep(sleep_time)
                    print('deine Werte sind nun')
                    print('HP', Status[0])
                    print('ATK', Status[1])
                    time.sleep(sleep_time*1.5)
                    while True:
                        clear()
                        print('Du greifst nun die Riesenschlange an')
                        print(f'Du berherscht die folgenden Techniken: {Techniken}')
                        print('Welche Technik willst du jetzt nutzen ?')
                        eingabe = input()
                        if eingabe == 'Feuerball':
                            break
                        elif eingabe == 'Tornadokick':
                            break
                        elif eingabe == 'Fingerfakel':
                            break
                    if eingabe == 'Feuerball':
                        clear()
                        print('Du verursachst 500 Schaden')
                        time.sleep(sleep_time)
                        print('Du hast die Schlange getötet')
                        time.sleep(sleep_time)
                        SchlangeistTot()
                    elif eingabe == 'Tornadokick':
                        clear()
                        print('Du verursachst 300 Schaden')
                        time.sleep(sleep_time)
                        print('Du hast die Schlange getötet')
                        time.sleep(sleep_time)
                        SchlangeistTot()
                    elif eingabe == 'Fingerfakel':
                        clear()
                        print('Du verursachst keinen Schaden')
                        time.sleep(sleep_time)
                        print('Die Riesenschlange hat dich angegriffen, Du kriegst einen Schaden von 500')
                        time.sleep(sleep_time)
                        Riesenschlangeangriff()
                        Tot()
                elif eingabe == 'Tornadokick':                                                                                      #Tornadokick eingabe
                    clear()
                    print('Du machst der Riesenschlange eine Schaden von 300')
                    time.sleep(sleep_time)
                    print('Die Riesenschlange hat nun 300HP & 500ATK')
                    time.sleep(sleep_time)
                    print('Die Riesenschlange hat dich angegriffen, Du verlierst 500HP')            #Zu diesem Zeitpunkt kann man Maximal 800 Hp haben und 900ATK
                    Riesenschlangeangriff()
                    time.sleep(sleep_time)
                    print('deine Werte sind nun')
                    print('HP', Status[0])
                    print('ATK', Status[1])
                    time.sleep(sleep_time*1.5)
                    while True:
                        clear()
                        print('Du greifst nun die Riesenschlange an')
                        time.sleep(sleep_time)
                        print(f'Du berherscht die folgenden Techniken: {Techniken}')
                        time.sleep(sleep_time)
                        print('Welche Technik willst du jetzt nutzen ?')
                        eingabe = input()
                        if eingabe == 'Feuerball':
                            break
                        elif eingabe == 'Tornadokick':
                            break
                        elif eingabe == 'Fingerfakel':
                            break
                    if eingabe == 'Feuerball':
                        clear()
                        print('Du verursachst 500 Schaden')
                        time.sleep(sleep_time)
                        print('Du hast die Schlange getötet')
                        time.sleep(sleep_time)
                        SchlangeistTot()
                    elif eingabe == 'Tornadokick':
                        clear()
                        print('Du verursachst 300 Schaden')
                        time.sleep(sleep_time)
                        print('Du hast die Schlange getötet')
                        time.sleep(sleep_time)
                        SchlangeistTot()
                    elif eingabe == 'Fingerfakel':
                        clear()
                        print('Du verursachst keinen Schaden')
                        time.sleep(sleep_time)
                        print('Die Riesenschlange hat dich angegriffen, Du kriegst einen Schaden von 500')
                        time.sleep(sleep_time)
                        Riesenschlangeangriff()
                        Tot()
                elif eingabe == 'Fingerfakel':                                                                          #Fingerfakel eingabe
                    clear()
                    print('Du machst der Riesenschlange keinen Schaden')
                    time.sleep(sleep_time)
                    print('Die Riesenschlange bemerkt aber das Leuchten')
                    time.sleep(sleep_time)
                    print('Die Riesenschlange hat dich angegriffen, Du verlierst 500HP')            #Zu diesem Zeitpunkt kann man Maximal 800 Hp haben und 900ATK
                    Riesenschlangeangriff()
                    time.sleep(sleep_time)
                    print('deine Werte sind nun')
                    print('HP', Status[0])
                    print('ATK', Status[1])
                    time.sleep(sleep_time*1.5)                
                    while True:
                        clear()
                        print('Du greifst nun die Riesenschlange an')
                        print(f'Du berherscht die folgenden Techniken: {Techniken}')
                        print('Welche Technik willst du jetzt nutzen ?')
                        eingabe = input()
                        if eingabe == 'Feuerball':
                            break
                        elif eingabe == 'Tornadokick':
                            break
                        elif eingabe == 'Fingerfakel':
                            break
                    if eingabe == 'Feuerball':
                        clear()
                        print('Du verursachst 500 Schaden')
                        time.sleep(sleep_time)
                        print('Die Schlange hat nun 100HP & 500ATK')
                        time.sleep(sleep_time)
                        print('Die Riesenschlange hat dich angegriffen, Du kriegst einen Schaden von 500')
                        Riesenschlangeangriff()
                        time.sleep(sleep_time)
                        Tot()
                    elif eingabe == 'Tornadokick':
                        clear()
                        print('Du verursachst 300 Schaden')
                        time.sleep(sleep_time)
                        print('Die Schlange hat nun 300HP & 500ATK')                    
                        time.sleep(sleep_time)
                        print('Die Riesenschlange hat dich angegriffen, Du kriegst einen Schaden von 500')
                        time.sleep(sleep_time)
                        Riesenschlangeangriff()
                        Tot()
                    elif eingabe == 'Fingerfakel':
                        clear()
                        print('Du verursachst keinen Schaden')
                        time.sleep(sleep_time)
                        print('Die Riesenschlange hat dich angegriffen, Du kriegst einen Schaden von 500')
                        time.sleep(sleep_time)
                        Riesenschlangeangriff()
                        Tot()
            else:
                clear()
                print('Du kannst es nicht mit der Riesenschlange aufnehmen')
                time.sleep(sleep_time)
                print('Ihr zwei habt gekämpft, du stirbst')
                time.sleep(sleep_time)
                Tot()
        
        elif eingabe == 'B':
            K9()


def SchlangeistTot():                                                                                                  #Ereignisse die nach dem Tod der Schlange passieren
    global Lebenvorkampf
    global ATKvorkampf
    global Cash
    Status[0] = Lebenvorkampf
    Status[1] = ATKvorkampf
    global Raum2
    Raum2 = 'Erledigt'
    clear()
    print('Die Schlange verwandelt sich in ein Zettel auf dem die Nummern 4167 steht')
    Code.append('Tür 2= 4167')
    time.sleep(sleep_time)
    print('Du siehst eine Truhe in der sehr viel geld ist du hast 650 Kronen gefunden')
    time.sleep(sleep_time)
    Cash = Cash + 650 
    while True:
        clear()
        print('Was machst du jetzt?')
        print('A zurückgehen')
        Abfrage()
        eingabe = input ()
        if eingabe == 'A':
            break
        elif eingabe == ('I'):
            Inventory()
        elif eingabe == ('S'):
            Werte()    
    if eingabe == 'A':
        K9()

Raum3 = 'icht Erledigt'

def K9k4():                                                                                                                     #Der Raum Für das Rätsel wird erstellt
    global Raum3
    if Raum3 == 'Erledigt':
        print('Du bist mit diesem Raum schon fertig')                                                                   
        time.sleep(sleep_time)
        print('Du hast hier nichts mehr zu tun')
        time.sleep(sleep_time*1.5)
        K9()
    else:
        clear()
        print('Du gehst den Gang entlang')
        time.sleep(sleep_time)
        print('Du findest einen Koffer in dem du deine Code eingeben musst')
        time.sleep(sleep_time)
        print('Daneben liegt ein Zettel auf dem Steht:')
        time.sleep(sleep_time)
        while True:
            clear()
            print('Der Code zum öffnen des Koffers ist das Jahr in das Marty und doc in die Zukunft gereist sind')
            print('falls du eine falsche Code eingibst explodiert der Koffer also arbeite bedacht')
            print('A aufgeben und zurückgehen')
            eingabe = input()
            try:
                int(eingabe)
                if int(eingabe) == 2015:
                    break
                else:
                    clear()
                    print('Der Code war falsch')
                    time.sleep(sleep_time)
                    print('Der Koffer explodiert')
                    time.sleep(sleep_time)
                    Tot()
            except ValueError:
                if eingabe == 'A':
                    break
                else:
                    pass
        if int(eingabe) == 2015:
            clear()
            print('Der Koffer öffnet sich')
            time.sleep(sleep_time)
            print('Im Koffer befindet sich ein Trank')
            time.sleep(sleep_time)
            print('auf dem Trank steht Trinke das und deine Haut wird 8 mal stärker')
            Raum3 = 'Erledigt'
            Inventar.append('Trank')
            print('Du hast das Rätsel gelöst')
            time.sleep(sleep_time)
            while True:
                clear()
                print('Was machst du jetzt?')
                print('A zurückgehen')
                Abfrage()
                eingabe = input()
                if eingabe == 'A':
                    break
                elif eingabe == ('I'):
                    Inventory()
                elif eingabe == ('S'):
                    Werte() 
            if eingabe == 'A':
                K9()
        if eingabe == 'A':
                K9()        

def K10Zugang():                                                                                                                    #Der Ausgang bzw Ort um das Rätsel zu lösen um weiter zu kommen 
    clear()
    while True:
        print('Du bist nun an der 4ten Tür ')
        print('Was machst du nun ?')
        print('A die Tür öffnen')
        print('B zurückgehen')
        Abfrage()
        eingabe = input()
        if eingabe == 'A':
            break
        elif eingabe == 'B':
            break
        elif eingabe == ('I'):
            Inventory()
        elif eingabe == ('S'):
            Werte()
    if eingabe == 'A':
        Codeversuche = 0
        while True:
            clear()
            print('Du musst nun die Codes eingeben die du gefunden hast')
            time.sleep(sleep_time)
            print(f'Du hast die folgenden Codes gelernt {Code}')
            print('Zuerst gibst du den aus der ersten Tür ein und dann den zweiten')
            time.sleep(sleep_time)
            print('Gib A ein um aufzugeben')
            eingabe = input('Der erste Code > ')
            if eingabe == 'A':
                break            
            eingabe2 = input('Der zweite Code > ')
            if eingabe2 == 'A':
                break  
            elif eingabe == '2107' and eingabe2 == '4167' :
                break
            else:
                clear()
                time.sleep(sleep_time)
                print('Der eingebene Code war falsch versuch es nochmal')
                time.sleep(sleep_time)
                Codeversuche += 1
            
            if Codeversuche > 5:
                time.sleep(sleep_time)
                print('Aus der Tür kommen auf einmal Speere rausgeschossen')
                time.sleep(sleep_time)
                print('Du kannst es nicht aufhalten')
                time.sleep(sleep_time)
                print('Alle Speere Treffen dich')
                time.sleep(sleep_time)
                Tot()

        if eingabe == 'A':
            K10Zugang()
        elif eingabe2 == 'A':
            K10Zugang
        elif eingabe == '2107' and eingabe2 == '4167' :
            K10Geschichte()

    elif eingabe == 'B':
        K9()

def K10Geschichte():                                                                                                       #Vorgeschichte paar fakten wichtig für das Nächst Kapitel
    clear()
    print('Du siehst ein Unglaublich helles Licht aus der Tür scheinen')
    time.sleep(sleep_time)
    print('Du gehst durch die Tür')
    time.sleep(sleep_time)
    print('Aufeinmal merkst du das unter dir kein Boden ist')
    time.sleep(sleep_time)
    print('Du Fällst aus cirka 400 Metern Höhe auf den Boden')
    time.sleep(sleep_time)
    K10()

def K10():                                                                                                  #Das treffen mit Bernhard,  wie es abläuft wegen der Beziehung die man hätte vorher aufbauen können 
    global Cash
    global Bernhardkenngelernt
    global Bernhardshop
    clear()
    if Bernhardkenngelernt == 'Ja':
        print('Bernhard fängt dich mit seinem weichen Bauch auf')
        time.sleep(sleep_time)
        print('Du: Bernhard?')
        time.sleep(sleep_time)
        print('Bernhard: Richtig! Lang nicht gesehen, Junge.')
        time.sleep(sleep_time)
        print('Du: Sag mal wo bin ich ?')
        time.sleep(sleep_time)
        print('Bernhard: Du bist in Central city, sag wieso regnest du vom Himmel?')
        time.sleep(sleep_time)
        print('Du: Gute Frage, ich war in so einer Höhle und hab gerade so ne Fett Schlange zerlegt.')
        print('Du: Dann ging ich durch so eine Leuchtende Tür, und naja dann war ich hier.')
        time.sleep(sleep_time)
        print('Bernhard: Sag komm mit lass mich dir ein Kaffe machen, und du erzählst mir was du erlebt hast.')
        time.sleep(sleep_time)
        print('Bernhard nimmt Nero mit in seine Wohnung, macht ihm ein Kaffe und die beiden reden ein bisschen miteinander')
        time.sleep(sleep_time*2)
        clear()
        time.sleep(sleep_time)
        print('Du: ....Haha, du bist mir einer Bernahard')
        time.sleep(sleep_time)
        print('Bernhard: Danke, nur sag wir haben ja unseren spaß, aber wie heißt du eigentlich?')
        time.sleep(sleep_time)
        print('Du: Eigentlich weiß ich das selber nicht so genau, aber paar Leute nannten mich Nero also schätze ich mal dass das mein Name ist')
        time.sleep(sleep_time)
        print('Bernhard: Nero? ')
        time.sleep(sleep_time)
        print('Du: Ja, wieso ?')
        time.sleep(sleep_time)
        print('Bernhard: Nix, nur Nero war bei uns ein Stark gefürchteter Krieger. Er und sein Bruder Mizu, aber beide verschwanden.')
        time.sleep(sleep_time)
        print('Bernhard: Niemand weiß was mit dennen passiert ist. Schließlich wurden sie verehrt von den Menschen.')
        time.sleep(sleep_time)
        print('Bernhard: Sie waren nunmal immer da wenn jemand problem gemacht hat')
        print('....')
        time.sleep(sleep_time)
        clear()
        print('Bernhard: Sag wie wäre es mit einer Runde Armdrücken?')
        time.sleep(sleep_time)
        print('Du: Klar wieso nicht ?')
        time.sleep(sleep_time)
        print('Bernhard: Machen wir es aber Interresanter lass uns wetten, um 300 Kronen. Jeder von uns setzt 300. Gewinner kriegt alles')
        time.sleep(sleep_time)
        print('Du: Ok, du wirst aber verlieren')
        print('...')
        time.sleep(sleep_time*2.4)
        print('Du: Gewonnen, ich schätze das heißt ich kriege dann alles')
        time.sleep(sleep_time)
        print('Bernhard: Na gut, Glück gehabt.')
        Cash += 300
        time.sleep(sleep_time)
        clear()
        print('Bernhard: Krasse Sache aber sag Was hast du jetzt vor?')
        time.sleep(sleep_time)
        print('Du: Keine Ahnung, ich weiß nur dass ich antworten brauche schließlich kann ich mich an nichts errinern. ')
        time.sleep(sleep_time)
        print('Berhard: Naja hast du keine Anhaltspunkte oder so ?')
        time.sleep(sleep_time)
        print('Du:Naja es gibt so eine Frau du mich scheinbar zu kennen scheint aber die muss ich erstmal finden.')
        time.sleep(sleep_time)
        print('Bernhard: Was weißt du den über sie?')
        time.sleep(sleep_time)
        print('Du: Nix naja, bis darauf dass sie fies ist. Und warscheinlich nicht gut auf mich zu sprechen ist')
        time.sleep(sleep_time)
        print('Bernhard: Na toll.')
        time.sleep(sleep_time)
        print('Du: Ich glaube ich werde erstmal das Wirtshaus aufsuchen.')           
        time.sleep(sleep_time)
        print('Bernhard: Was für ein Wirtshaus?')
        time.sleep(sleep_time)
        print('Du: Ich weiß zwar nicht wie es heißt, aber Kelvin heißt der Barkeeper.')
        time.sleep(sleep_time)
        print('Bernhard: Aso na klar, das ist gleich außerhalb der Stadt.')
        print('Bernhard: Ich bring dich hin.')
        time.sleep(sleep_time)
        print('Du: Ok klar gern.')
        time.sleep(sleep_time)
        clear()
        time.sleep(sleep_time)
        print('Bernhard: Bevor du gehst ich habe da noch was für dich')
        time.sleep(sleep_time)
        print('Du: Was den ?')
        time.sleep(sleep_time)
        print('Bernhard: Du weißt dass ich ein Geschäft Habe. Da du ja hier noch was vor hast habe ich bisschen ausrüstung für dich.')
        Inventar.append('Kampf Brustpanzer [+100HP]')
        time.sleep(sleep_time)
        print('Der Kampf Brustpanzer wurde deinem Inventar hinzugefügt')
        time.sleep(sleep_time)
        print('Du: Danke, das ist lieb')
        time.sleep(sleep_time)
        print('Bernhard: Übrigens wenn du mal was bei mir kaufen willst, nutzt diese Telekugeln. Damit kommst du sofort in den Shop.')
        Bernhardshop = 'offen'
        time.sleep(sleep_time)
        print('Du: Ok das ist aber cool.')
        time.sleep(sleep_time)
        print('Bernhard: Wir sollten jetzt aber los')
        time.sleep(sleep_time)
        print('Du: Ok')
        time.sleep(sleep_time)
        while True: 
            clear()
            print('Was willst du jetzt machen ?')
            print('A Los gehen zu Taverne')
            Abfrage()
            eingabe = input()
            if eingabe == 'A':
                break
            elif eingabe == ('I'):
                Inventory()
            elif eingabe == ('S'):
                Werte()
            elif eingabe == 'L':
                Shop()
        if eingabe == 'A':
            K11()
    else:
        print('Du knallst mit auf den Harten Boden')
        time.sleep(sleep_time)
        print('Du spürst Schmerzen auf dem ganzen Körper')
        time.sleep(sleep_time)
        print('Du bist ko gegangen')
        time.sleep(sleep_time)
        print('Du wachst auf')
        time.sleep(sleep_time)
        print('Fremder: Guten Morgen, Sonnenschein.')
        time.sleep(sleep_time)
        print('Du: Boah hab ich Kopfschmerzen, wer bist du ?')
        time.sleep(sleep_time)
        print('Fremder: Ich bin der Schrotthändler Bernhard')
        time.sleep(sleep_time)
        print('Du: Aso danke fürs pflegen, aber ich muss los. Nur noch ein Frage wie komme ich zu Kelvins Taverne ?')
        time.sleep(sleep_time)
        print('Bernhard: Es ist gleich außerhalb der Stadt da kommst du leicht hin.')
        time.sleep(sleep_time)
        print('Bernhard: Ahja falls du was kaufen willst nutze diese Telekugeln')
        time.sleep(sleep_time)
        Bernhardshop = 'offen'
        print('Du: Danke, Tschüss')
        time.sleep(sleep_time)
        print('Du bist losgegangen')
        time.sleep(sleep_time)
        print('Bernhard: Der schien es aber eilig zu haben.')
        K11()

def K11():                                                                      #Anfang vom ende der Geschichte bereitung auf Finale
    global Bernhardkenngelernt
    global Bernhardbar
    Bernhardbar = 'Ja'
    if Bernhardkenngelernt == 'Ja':
        clear()
        print('Musik Startet')
        playbarMusik()
        clear()
        print('Kelvin: Hey, und wer ist diese Random neben dir ?')
        time.sleep(sleep_time)
        print('Bernhard: Kein Grund, gleich gemein zu sein.')
        time.sleep(sleep_time)
        print('Du: Kelvin, ich muss diese Frau finden!')
        time.sleep(sleep_time)
        print('Kelvin: Ich weiß nicht wo sie sein könnte, aber vlt weiß das Orakel was.')
        time.sleep(sleep_time)
        print('Bernhard: Die Orakel werden aber von Drachen beschützt.')
        time.sleep(sleep_time)
        print('Kelvin: Deswegen werden wir bisschen trainieren, dann kannst du den Drachen mit Leichtigkeit erlegen.')
        time.sleep(sleep_time)
        print('Bernhard: Na, dann wünsche ich euch viel Spaß.')
        time.sleep(sleep_time)
    else:
        playbarMusik()
        clear()
        print('Du: Kelvin, ich muss diese Frau finden!')
        time.sleep(sleep_time)
        print('Kelvin: Ich weiß nicht wo sie sein könnte, aber vlt weiß das Orakel was.')
        time.sleep(sleep_time)
        print('Du: Dann finde ich es.')
        time.sleep(sleep_time)
        print('Kelvin: Die Orakel werden aber von Drachen beschützt.')
        time.sleep(sleep_time)
        print('Kelvin: Deswegen werden wir bisschen trainieren, dann kannst du den Drachen mit Leichtigkeit erlegen.')
        time.sleep(sleep_time)
    K11finalTraining()

def K11finalTraining():                                                                                                 #Training für den Drachen Final Kampf
    global Bernhardkenngelernt
    clear()
    print('Krasse Trainingsmusik setzt ein')
    time.sleep(sleep_time)
    finaltrainingmusik()
    clear()
    time.sleep(sleep_time)
    print('Kelvin: Bist du bereit es gehört sich einiges Um einen Drachen zu erlegen.')
    time.sleep(sleep_time)
    print('Kelvin: Dieser Drache hat nämlich einen HP Wert von 5000 und einen ATK von 1000')
    time.sleep(sleep_time)
    print('Kelvin: Bei deinen Jetzigen Werten wirst du das nicht überleben')
    time.sleep(sleep_time)
    print('Kelvin: Deswegen lehre ich dich jetzt die Kraft der Oni um dein HP zu steigern')
    time.sleep(sleep_time)
    print('Klevin: Danach lehre ich dich den Angriff Michaels dieser wird dein ATK um 5000')
    time.sleep(sleep_time)
    print('Kelvin: Dadurch wirst den Drachen sofort Töten aber die Technick kannst du nur anwenden wenn du 3 mal vom Drachen getroffen wurdest ')
    time.sleep(sleep_time)
    print('Du: Ok, legen wir los')
    time.sleep(sleep_time)
    clear()
    time.sleep(sleep_time)
    print('Kelvin: als erstes Muss du dich Konzentrieren und alles an Kraft anwenden was du kann')
    while True:
        clear()
        print('Drück A um dich zu Konzentrieren')
        eingabe = input()
        if eingabe == 'A':
            break
    time.sleep(sleep_time)
    print('Du hast die Kraft der Oni erlangt')
    Status[0] = 3500
    print('Dein HP steigt auf 3.500')
    time.sleep(sleep_time)
    print('Kelvin: Gut gemacht, jetzt hast du genug HP um es mit ihm Aufzunehemen')
    time.sleep(sleep_time)
    clear()
    print('Kelvin: Jetzt geht es um den Angriff des Michaels, dieser Technick kann nur einmal genutzt werden den danach verliert man jegliche Kraft ihn nochmal auszuüben')
    time.sleep(sleep_time)
    while True:
        clear()
        print('Kelvin: Um diese Technick zu erlernen musst du das Blut einer Erzengels trinken.')
        print('Kelvin: Du musst aber psychisch stark genug sein sonst stirbst du')
        print('Drück A um das Blut zu trinken')
        eingabe= input()
        if eingabe == 'A':
            break
    print('*Dir wird übel*')
    time.sleep(sleep_time)
    print('Du fliegst um')
    time.sleep(sleep_time)
    print('Du wachst auf')
    time.sleep(sleep_time)
    print('Kelvin: Gehts dir gut ? Du Hast 11 Stunden geschlafen')
    time.sleep(sleep_time)
    print('Du: Ja alles ok. Mir war nur kurzzeitig übel aber jetzt gehts')
    time.sleep(sleep_time)
    print('Kelvin: Dein ATK ist um 5000 gestiegen, du bist bereit du musst jetzt zum Orakel.')
    Status[1] += 5000
    time.sleep(sleep_time)
    print('Kelvin: Ich geb dir eine die dir zeigen wird wie du hinkommst')
    time.sleep(sleep_time)
    if Bernhardkenngelernt == 'Ja':
        clear()
        print('Du bereitest dich gerade vor zum Orakel zu gehen')
        time.sleep(sleep_time)
        print('Bernhard: Hey, Nero! Ich wünsche dir viel Glück.')
        time.sleep(sleep_time)
        print('Du: Danke.')
        time.sleep(sleep_time)
    K12()

Drache = [5000, 1000]

def K12():
    clear()
    time.sleep(sleep_time)
    print('Du Stehst vor dem Tempel des Orakels')
    time.sleep(sleep_time)
    print('Du siehst den Drachen wachend vor dem Tempel. Er ist Riesengroß und spuckt feuer')
    while True:
        clear()
        print('Was machst du Jetzt?')
        print('A Gegen den Drachen antreten \nB In die Taverne gehen')
        Abfrage()
        eingabe = input()
        if eingabe == 'A':
                break
        elif eingabe == 'B':
            Taverne()
        elif eingabe == ('I'):
            Inventory()
        elif eingabe == ('S'):
            Werte()
        elif eingabe == 'L':
            Shop()
    print('Du Kämpfst jetzt gegen den Drachen')
    if Status[0] >= 3500 and Status[1] >= 5000:
        print('Der Kampf beginnt')
        x = Status[0]
        Aufladung = 0
        while True:
            clear()
            print('Du greifst den Drachen an ')
            print('Der Drache hat einen HP Wert von 5000 und einen ATK Wert von 1000')
            print(f'Du kannst folgende Techniken anwenden: {Techniken}')
            eingabe = input()
            if eingabe == 'Schwert' and Schwertausgerüstet == 'Ja':
                Drache[0] -= 700
                print(f'Du hast die HP vom Drachen auf {Status[0]} gesenkt ')
                Aufladung += 1
                time.sleep(sleep_time)
            elif eingabe == 'Feuerball':
                Drache[0] -= 500
                print(f'Du hast die HP vom Drachen auf {Status[0]} gesenkt ')
                Aufladung += 1
                time.sleep(sleep_time)
            elif eingabe == 'Fingerfakel':
                Drache[0] -= 0
                print(f'Du hast die HP vom Drachen auf {Status[0]} gesenkt ')
                Aufladung += 1
                time.sleep(sleep_time)
            elif eingabe == 'Tornadokick':
                Drache[0] -= 300
                print(f'Du hast die HP vom Drachen auf {Status[0]} gesenkt ')
                Aufladung += 1
                time.sleep(sleep_time)
            elif eingabe == 'Angriff Michaels' and 'Angriff Michaels' in Techniken:
                Drache[0] -= 5000
                print('Du tötest den Drachen')
                time.sleep(sleep_time)
                Techniken.remove('Angriff Michaels')
                Status[1] -= 5000
            if Drache[0] <= 0:
                break
            else:
                print('Der Drache greift dich an ')
                time.sleep(sleep_time)
                Status[0] = Status[0] - Drache[1]
                if Status[0] > 0:
                    print(f'Dein HP sinkt auf {Status[0]}')
                    if Aufladung >= 3:
                        Techniken.append('Angriff Michaels')
                        print('Der Angriff hat sich aufgeladen')
                        time.sleep(sleep_time)
                        print('Du kannst die Technik nun nutzen')
                        time.sleep(sleep_time)
                else:
                    Drachentot() 
        Status[0] = x
        Ende()
    else:
        Drachentot()

def Drachentot():
    print('Der Drache spuckt feuer auf dich und bringt dich sofort um')
    time.sleep(sleep_time)
    Tot()

def Ende():                                                                     ######End Sequenz letzte Geschehnisse 
    clear()
    print('Der Drache wurde erschlagen')
    time.sleep(sleep_time)
    print('Du gehst zum Orakel')
    time.sleep(sleep_time)
    print('Das Orakel sieht dich an')
    time.sleep(sleep_time)
    print('Orakel: Ich habe dich erwartet')
    time.sleep(sleep_time)
    print('Du: Dann weißt du wieso ich hier bin!')
    time.sleep(sleep_time)
    print('Orakel: Ich kann dir nicht sagen wo du Frau ist.')
    time.sleep(sleep_time)
    print('Du: Wenn es sein muss zwing ich dich')
    time.sleep(sleep_time)
    print('Orakel: Du weißt selber ganz genau dass selbst wenn du mich Tötest sag ich dir nix')
    time.sleep(sleep_time)
    print('Du: Gib mir doch irgendwas')
    time.sleep(sleep_time)
    print('Orakel: Geh in die Taverne, dort wirst du deine Antworten finden')
    time.sleep(sleep_time)
    print('Orakel: Bestell dir dein Lieblingsdrink und du wirst dein antworten kriegen.')
    time.sleep(sleep_time)
    print('Du: Also ist die Antwort saufen ?')
    time.sleep(sleep_time)
    print('Das Orakel schmunzelt')
    time.sleep(sleep_time)
    print('Orakel: So ziemlich')
    time.sleep(sleep_time)
    print('Du: Auf wiedersehen')
    time.sleep(sleep_time)
    clear()
    print('In der Bar')
    playbarMusik()
    time.sleep(sleep_time)
    print('Du: Kelvin einen wie immer')
    time.sleep(sleep_time)
    print('Kelvin: Was hast du herausgefunden')
    time.sleep(sleep_time)
    print('Du: Nichts')
    time.sleep(sleep_time)
    print('Kelvin: Ähm ok, hier dein Drink')
    time.sleep(sleep_time)
    print('plötzlich spricht ihn ein Fremder an')
    time.sleep(sleep_time)
    print('Fremder: Hallo ich bin Mizu')
    time.sleep(sleep_time)
    print('Nero fängt an zu Schmunzeln')
    time.sleep(sleep_time)
    clear()
    print('Outro Musik spielt')
    outro()
    ENDEGELENDE()

Start()                                                                                                #Spiel wird gestartet