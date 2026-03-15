print("======================")
print("===Kalkulator BMI===")
print("======================")

print("Rumus Berat Badan Ideal:")
print("BBI = (Tinggi Badan - 100) - 10% x (Tinggi Badan - 100)")

# INPUT
nama = input("Nama : ")
tinggi_badan = float(input("Tinggi badan (cm) : "))

# PROSES
perhitungan = tinggi_badan - 100
berat_badan_ideal = perhitungan - (0.1 * perhitungan)

# OUTPUT
print("===Hasil Perhitungan===")
print("Nama: ", nama)
print("Tinggi badan: ", tinggi_badan, "cm")
print("Berat badan ideal: ", round(berat_badan_ideal,2), "kg")
