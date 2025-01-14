#main tebak tebakkan yuk sama python
#sebelum itu install random dulu yaa
#pip install  random
import random

nama = input('Masukkan username untuk memulai game: ')
uang = 100
print(f'Saldo Anda adalah {uang}')

def game():
    global uang
    while True:
        if uang < 50:
            print('Saldo Anda tidak cukup untuk bermain.')
            isi_ulang = input('Apakah Anda ingin isi ulang saldo? (y/n): ').lower()
            if isi_ulang == 'y':
                nominal = int(input('Masukkan nominal saldo Anda (50/100): '))
                if nominal in [50, 100]:
                    uang += nominal
                    print(f'Saldo Anda sekarang adalah {uang}')
                else:
                    print('Nominal yang Anda masukkan tidak valid.')
                    continue
            else:
                print('Terima kasih telah bermain!')
                break

        mulai_game = input('Sudah siap bermain? (y/n): ').lower()
        if mulai_game == 'y':
            uang -= 50
            pilihan = int(input('Pilih nomor 1 atau 0: '))
            hasil = random.randint(0, 1)

            if pilihan == hasil:
                uang += 100
                print(f'Hasil: {hasil}')
                print(f'Jackpot! Selamat Anda menang dan total uang Anda adalah {uang}')
            else:
                print(f'Hasil: {hasil}')
                print(f'Anda kurang beruntung, harap coba lagi. Sisa uang Anda adalah {uang}')
        else:
            print('Terima kasih telah bermain!')
            break

        # Tanya apakah mau bermain lagi
        main_lagi = input('Mau main lagi? (y/n): ').lower()
        if main_lagi != 'y':
            print('Terima kasih telah bermain!')
            break

# Jalankan permainan
game()
