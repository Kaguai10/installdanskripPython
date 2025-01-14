#yang mau main batu gunting kertas tapi python yang nentuin nih cobain yuk xixixixixiix
#sebelumnya install import random agar python ikut main juga 
import random

print("Selamat datang di game Batu Gunting Kertas!")

# Input nama pemain
player1 = input("Masukkan username untuk Player 1: ")
player2 = input("Masukkan username untuk Player 2: ")

# Pilihan dalam game
choices = ["batu", "gunting", "kertas"]

# Skor awal
score_player1 = 0
score_player2 = 0

# Fungsi untuk menentukan pemenang
def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "seri"
    elif (choice1 == "batu" and choice2 == "gunting") or \
         (choice1 == "gunting" and choice2 == "kertas") or \
         (choice1 == "kertas" and choice2 == "batu"):
        return "player1"
    else:
        return "player2"

# Main loop permainan
while True:
    print("\nBersiap untuk bermain!")
    ready1 = input(f"{player1}, apakah Anda siap? (y/n): ").lower()
    if ready1 != "y":
        print(f"{player1} tidak siap. Permainan berakhir.")
        break

    ready2 = input(f"{player2}, apakah Anda siap? (y/n): ").lower()
    if ready2 != "y":
        print(f"{player2} tidak siap. Permainan berakhir.")
        break

    # Pilihan diacak secara random
    player1_choice = random.choice(choices)
    player2_choice = random.choice(choices)

    # Tampilkan pilihan dan hasil
    print(f"\n{player1} secara acak memilih: {player1_choice}")
    print(f"{player2} secara acak memilih: {player2_choice}")

    result = determine_winner(player1_choice, player2_choice)

    # Update skor
    if result == "seri":
        print("Hasil: Seri!")
        score_player1 += 1
        score_player2 += 1
    elif result == "player1":
        print(f"Hasil: {player1} menang!")
        score_player1 += 1
    elif result == "player2":
        print(f"Hasil: {player2} menang!")
        score_player2 += 1

    # Tampilkan skor terkini
    print(f"\nSkor sementara: {player1} = {score_player1}, {player2} = {score_player2}")

    # Tanya apakah ingin bermain lagi
    play_again = input("\nMau main lagi? (y/n): ").lower()
    if play_again != "y":
        print("Permainan selesai.")
        print(f"Skor akhir: {player1} = {score_player1}, {player2} = {score_player2}")
        if score_player1 > score_player2:
            print(f"Pemenang keseluruhan adalah {player1}!")
        elif score_player1 < score_player2:
            print(f"Pemenang keseluruhan adalah {player2}!")
        else:
            print("Permainan berakhir seri!")
        break
