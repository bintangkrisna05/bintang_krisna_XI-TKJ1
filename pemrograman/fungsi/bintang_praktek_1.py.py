#Nama           :bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5
#Rumus: Total deret bilangan ganjil = 1 + 3 + 5 + ... + (2n-1)

# Mengambil input bilangan bulat positif n
n = int(input("Masukkan bilangan bulat positif n: "))

# Inisialisasi variabel total dan suku awal
total = 0
suku = 1

# Menghitung total deret bilangan ganjil hingga suku ke-n
for i in range(n):
    total += suku
    suku += 2  # Menambahkan 2 untuk mendapatkan suku berikutnya

# Mencetak total deret bilangan ganjil
print(f"Total deret bilangan ganjil hingga suku ke-{n} adalah: {total}")