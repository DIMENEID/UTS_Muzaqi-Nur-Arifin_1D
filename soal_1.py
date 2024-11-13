import modul as md

print ('''Pilih Operasi Matematika
1. Penjumlahan
2. Pengurangan
3. Perkalian
''')

while True :
    pemilihan = input('Masukkan Pilihan Operasi (1/2/3):')
    angka_pertama = int(input('Masukkan Nilai A :'))
    angka_kedua = int(input ('Masukkan Nilai B :'))
    
    if pemilihan == '1':
        md.penjumlahan(angka_pertama,angka_kedua)
       
        
    elif pemilihan == '2':
        md.pengurangan(angka_pertama,angka_kedua)
        
        
    elif pemilihan == '3':
        md.perkalian(angka_pertama,angka_kedua)




