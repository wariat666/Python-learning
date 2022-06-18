#Drukuje tekst na ekran
print("tekst")
#Czeka na wprowadzenie znaku (w tym przypadku enter by zakończyć), instrukcja wejścia
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
#operatory do liczenia, zależnie co się da pomiędzy działaniami
#/ dzielenie zmiennoprzecinkowe
#// dzielenie do części całych (ścina przecinek)
#% modulo - reszta z dzielenia
# zmienne - zmienna name ma przypisany na sztywno tekst
name = "Radek"
# zmienna name ma podawany tekst z palca, domyślnie string
name = input("Podaj coś i daj enter mordo ")
age = int(input("podaj coś tam"))
# wypisze daną zmienną x razy, ale jej nie policzy!
print (age *10)
#zapis kapitalikami
print(name.upper())
#zapis małymi literami
print(name.lower())
#zapis każdego wyrazu z dużej litery
print(name.title())
# zapis z zamianą jednego wyrazu na inny
print(name.replace("Radek", "Bumbalabumba"))
# dwie metody losowania liczb
import random #importuje moduł do losowania
die1 = random.randint(1,6) #zakres od 1 do 6
die2 = random.randrange(6)+1 #randrange liczy od 0 do 6 (6 się nie łapie) więc +1 na końcu
total = die1 + die2
print("Wyrzuciłeś", die1, die2, "i uzyskałeś łącznie ", total)
#funkcja if 
password = input("Wprowadź hasło ")
if password == "sekret":
    print("Udzielono dostęp")
else:
    print("Błędne hasło")
#while
response = ""
while response != "Dlatego.":#wykonuje dopóki spełnia warunek
    response = input("Dlaczego?\n")
#for
for i in range (1000, -1 , -1):  #nazwa licznika np i w czym ma grzebać i przedziały od do i skok
    print (i, end = " ") #wyświetla zmienną i a end jest po to by wstawiać spacje na koniec