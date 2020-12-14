def suku_n(a,b,n):
    hasil = a + (n - 1) * b
    return hasil

def jumlah(a,b,n):
    hasil = n / 2 * (2 * a + (n-1) * b)
    return hasil

print('Deret Aritmatika')
print('Menu: ')
print('1. Nilai suku ke-n')
print('2. Jumlah suku ke-n')
menu = int(input('Masukkan menu yang anda pilih: '))

if menu == 1:
    a = int(input('Masukkan nilai awal: '))
    b = int(input('Masukkan selisih: '))
    n = int(input('Masukkan suku ke: '))
    print('Nilai dari suku ke {} adalah %d'.format(n)%suku_n(a,b,n))

elif menu == 2:
    a = int(input('Masukkan nilai awal: '))
    b = int(input('Masukkan selisih: '))
    n = int(input('Masukkan suku ke: '))
    print('Jumlah suku ke {} adalah %d'.format(n)%jumlah(a,b,n))

else:
    print('Menu yang anda masukkan salah')