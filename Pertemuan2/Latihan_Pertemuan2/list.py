angka = [10,20,30,40,50]

# 1. tambahkan angka 60 ke dalam list
angka.append(60)

# 2. hapus angka 20 dari list
angka.remove(20)

# 3. tampilkan angka tertinggi dan terendah
print(max(angka))
print(min(angka))

# 4. hitung rata-rata angka setelah perubahan data
len = len(angka)
jumlah = 0
for x in (angka):
    jumlah = jumlah + x
average = jumlah/len
print(average)

# 5. tampilkan seluruh isi list setelah perubahan
print(angka)