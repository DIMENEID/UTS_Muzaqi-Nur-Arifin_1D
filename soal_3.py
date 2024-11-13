jumlah = int(input('Masukkan Jumlah Barang :'))
total_harga_barang = 0

for i in range (1,jumlah + 1):
    harga_barang = int(input(f'Masukkan Harga Barang ke-{i}: '))
    total_harga_barang += harga_barang


      
print("")
print(f'Total belanjaan dari ke {jumlah} barang adalah : Rp.{total_harga_barang:,}')
print("")