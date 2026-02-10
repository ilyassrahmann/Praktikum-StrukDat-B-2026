kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

# 1. tentukan mata kuliah yang diambil oleh kedua kelas

duaKelas = kelas_A.intersection(kelas_B)
print(duaKelas)

# 2. tentukan mata kuliah yang hanya diambil oleh kelas A

kelasAExclusive = kelas_A.difference(kelas_B)
print(kelasAExclusive)

# 3. tentukan seluruh mata kuliah unik yang diambil oleh kelas A dan B

totalUnik = kelas_A.union(kelas_B)
print(totalUnik)
