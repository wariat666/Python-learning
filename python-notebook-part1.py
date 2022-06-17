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