kata = input("Masukkan sebuah kata: ")

karakter_unik = {}
for karakter in kata:
    if karakter not in karakter_unik:
        karakter_unik[karakter] = 1
    else:
        karakter_unik[karakter] += 1

jumlah_karakter_unik = len(karakter_unik)

print("Kata '{}' terdiri dari {} karakter unik.".format(kata, jumlah_karakter_unik))
