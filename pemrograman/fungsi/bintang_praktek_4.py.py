#Nama           :bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5
#Rumus: Jumlah digit dari bilangan n = jumlah dari setiap digit dalam n

# Mengambil input bilangan bulat n
n = int(input("Masukkan bilangan bulat n: "))

# Menginisialisasi variabel jumlah_digit dengan nilai awal 0
jumlah_digit = 0

# Menghitung jumlah digit dalam n
while n > 0:
    digit = n % 10  # Mengambil digit terakhir
    jumlah_digit += digit
    n //= 10  # Menghapus digit terakhir

# Mencetak jumlah digit
print(f"Jumlah digit dalam bilangan {n} adalah: {jumlah_digit}")