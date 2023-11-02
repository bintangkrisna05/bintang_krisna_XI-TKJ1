#Nama           :bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5

# Input nilai tugas dan nilai ujian
nilai_tugas = float(input("Masukkan nilai tugas (skala 0-100): "))
nilai_ujian = float(input("Masukkan nilai ujian (skala 0-100): "))

# Tentukan kriteria untuk lulus
kriteria_tugas = nilai_tugas > 70
kriteria_ujian = nilai_ujian > 60

# Tentukan hasil akhir
if kriteria_tugas and kriteria_ujian:
    hasil_akhir = "Lulus"
else:
    hasil_akhir = "Gagal"

# Cetak hasil akhir
print(f"Hasil akhir: {hasil_akhir}")