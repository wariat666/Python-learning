price = int(input("Podaj kwotę do zapłaty za posiłki "))
withoutTips = price
withTips15 = withoutTips * 0.15
withTips20 = price * 1.2

withTips15 = int(withTips15)

print("Kwota do zapłaty to: ", withoutTips)
print("W przypadku zapłaty 15% napiwku wyjdzie łącznie: ", withTips15)
print("W przypadku zapłaty 20% napiwku wyjdzie łącznie: ", withTips20)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
