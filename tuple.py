my_tuple = (1, 2, 3, "empat", "lima")
print(my_tuple)

print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: empat
print(my_tuple[-1]) # Output: lima

tuplebaru = (6, 7, 8)
tuplesangatbaru = my_tuple + tuplebaru
print(tuplesangatbaru)

tupleganda = my_tuple * 2
print(tupleganda)

print("Panjang tuple:", len(my_tuple))

print("empat" in my_tuple)
print("Apakah 10 ada dalam tuple?", 10 in my_tuple)

a, b, c, d, e = my_tuple
print(a, b, c, d, e)

