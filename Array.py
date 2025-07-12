data = []

while True:
    input_data = int(input("Masukkan data (Berhenti jika 0): "))
    if input_data == 0:
        break
    data.append(input_data)

data.sort()

print("Data yang sudah diurutkan:")
for item in data:
    print(item)
