#Nama           :bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5
#Rumus: Faktorial n = n * (n-1) * (n-2) * ... * 1

# Mengambil input bilangan bulat positif n
n = int(input("Masukkan bilangan bulat positif n: "))

# Inisialisasi variabel faktorial dengan nilai awal 1
faktorial = 1

# Menghitung faktorial dari n
for i in range(1, n + 1):
    faktorial *= i

# Mencetak nilai faktorial
print(f"Faktorial dari {n} adalah: {faktorial}")