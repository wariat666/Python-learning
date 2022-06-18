import random
word = "indeks"
print("wartość zmiennej ", word, "to")
high = len(word)
low = -len(word)
print(high, low)
for i in range (10):
    position = random.randrange(low, high)
    print ("word[", position, "]\t", word[position])

input("\n\nAby zakończyć...")