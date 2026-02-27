dict = {
    'nama': 'Andi',
    'umur': 25,
    'kota': 'Jakarta'
}

print(dict['nama'])
print(dict['umur'])
print(dict.get('kota'))

dict['pekerjaan'] = 'Programmer'
print(dict)

dict['umur'] = 26
print(dict)

print("Isi dictionary:", dict)


