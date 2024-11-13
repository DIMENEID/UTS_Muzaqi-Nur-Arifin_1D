#inputan
berat_badan = float(input('Masukkan berat badan (Kg) :' ))
tinggi_badan = float(input('Masukkan Tinggi Badan (M): '))


#proses
rumus_tinggi_badan = tinggi_badan**2
rumus_bmi = berat_badan//rumus_tinggi_badan

#output
print(f'Berat Badan : {berat_badan}')
print(f'Tinggi Badan : {tinggi_badan}')
print(f'Nilai BMI : {rumus_bmi}')

#pengkondisian
if rumus_bmi < 18.5:
    print('Kategori BMI : Berat Badan Anda Kurang Ideal')
elif rumus_bmi < 24.9:
    print('Kategori BMI : Berat Badan Anda Normal')
elif rumus_bmi < 29.9:
    print('Kategori BMI : Anda Kelebihan Berat Badan')
elif rumus_bmi >= 30:
    print('Kategori BMI : Anda Obesitas')


