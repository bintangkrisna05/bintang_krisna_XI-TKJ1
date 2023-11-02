#Nama           :bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5

# Input jumlah penjualan bulanan
penjualan = int(input("Masukkan jumlah penjualan bulanan: "))

# Tentukan kategori berdasarkan jumlah penjualan
if penjualan > 1000:
    kategori = "Produk Terlaris"
elif penjualan >= 500:
    kategori = "Produk Populer"
else:
    kategori = "Produk Biasa"

# Cetak kategori produk
print(f"Kategori produk: {kategori}")