#Nama           :bintang krisna
#Kelas          :XI-TKJ-1
#Nomor Absen    :5
#Rumus: Bilangan Fibonacci ke-n = Bilangan Fibonacci ke-(n-1) + Bilangan Fibonacci ke-(n-2)

def fibonacci(n):
    if n <= 0:
        return "Bilangan Fibonacci hanya didefinisikan untuk n >= 1"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Mengambil input nilai n
n = int(input("Masukkan nilai n untuk bilangan Fibonacci ke-n: "))

# Memanggil fungsi fibonacci untuk menghitung bilangan Fibonacci ke-n
hasil = fibonacci(n)

# Mencetak hasil
print(f"Bilangan Fibonacci ke-{n} adalah: {hasil}")
