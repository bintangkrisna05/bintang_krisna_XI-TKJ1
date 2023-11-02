W#Nama           :Bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5
#Soal 3         :Deskripsi Pekerjaan: Sebagai seorang sistem administrator, Anda bertanggung jawab untuk memeriksa apakah suatu file di server sudah ada atau belum sebelum menggantinya.
#Soal           :Buat program Python yang memeriksa apakah suatu file sudah ada di direktori server. Jika file sudah ada, program harus mencetak "File sudah ada," jika tidak, program harus mencetak "File belum ada."


import os

# Memasukkan nama file yang ingin diperiksa
nama_file = input("Masukkan nama file yang ingin diperiksa: ")

# Memeriksa apakah file sudah ada di direktori saat ini
if os.path.isfile(nama_file):
    print("File sudah ada")
else:
    print("File belum ada")