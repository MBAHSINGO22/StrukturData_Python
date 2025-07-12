kata_unik = []

while True:
    input_kata = input('Masukkan kata (Berhenti jika ENTER saja sebagai input): ')
    if input_kata == '':
        break

    kata_unik.append(input_kata)

for kata in kata_unik:
    print(kata)
