mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75}
}

# 1. tampilkan nama mahasiswa yang memiliki ipk di atas 3.5

for x in mahasiswa:
    if (mahasiswa[x]["ipk"]) > 3.5:
        print(mahasiswa[x]["nama"]) 

# 2. hitung rata-rata IPK seluruh mahasiswa

hitung = 0
jumlah = 0
for x in mahasiswa:
    jumlah = jumlah + (mahasiswa[x]["ipk"])
    hitung = hitung + 1
avgIPK = jumlah/hitung
print(f"{avgIPK:.2f}")

# 3. tambahkan satu data mahasiswa baru ke data tersebut 

mahasiswa["A004"] = {"nama": "ilyas", "prodi":"Informatika", "ipk":3.6 }

for x, obj in mahasiswa.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

