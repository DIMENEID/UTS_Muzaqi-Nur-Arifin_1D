#input
while True:
    tahun = int(input('Masukkan Tahun (contoh : 2000):'))

    #proses
    if ((tahun % 400) == 0) or (((tahun%4) == 0) and ((tahun % 100) != 0)):
        print(f'Tahun {tahun} merupakan tahun kabisat')
    else:
        print(f'Tahun {tahun} BUKAN merupakan tahun kabisat')
        
    milih = input('Apakah anda ingin menghitung lagi? (y/t) : ').lower()
      
    if milih == 't':
         print('Terima kasih dan jangan kembali')
         break