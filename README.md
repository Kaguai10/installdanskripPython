# Panduan Instalasi Python di Linux, Windows, dan Android

Python adalah bahasa pemrograman yang populer dan mudah digunakan. Panduan ini menjelaskan langkah-langkah instalasi Python di berbagai platform: **Linux**, **Windows**, dan **Android**.

---

## 🐧 Instalasi Python di Linux

### Debian/Ubuntu
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Fedora
```bash
sudo dnf install python3 python3-pip
```

### Arch Linux
```bash
sudo pacman -S python python-pip
```

### Verifikasi Instalasi
```bash
python3 --version
pip3 --version
```

---

## 🪟 Instalasi Python di Windows

1. Buka website resmi Python: https://www.python.org/downloads/
2. Klik tombol **Download Python [versi terbaru]**.
3. Jalankan file installer yang telah diunduh.
4. **PENTING**: Centang opsi **Add Python to PATH** sebelum klik "Install Now".
5. Ikuti instruksi hingga selesai.

### Verifikasi Instalasi (melalui Command Prompt)
```cmd
python --version
pip --version
```

---

## 📱 Instalasi Python di Android (Menggunakan Pydroid 3)

1. Buka **Google Play Store**.
2. Cari **Pydroid 3 - IDE for Python 3**.
3. Instal aplikasi tersebut.
4. Buka aplikasi dan kamu sudah bisa langsung menulis dan menjalankan kode Python!

> Untuk menginstal modul tambahan (seperti `numpy`, `matplotlib`, dll), buka menu kiri atas di Pydroid 3, lalu pilih **Pip**.

---

## 📌 Tips Tambahan

- Gunakan `pip` untuk menginstal library tambahan:
  ```bash
  pip install nama-library
  ```
- Gunakan **virtual environment** untuk mengelola proyek Python secara terpisah:
  ```bash
  python3 -m venv env
  source env/bin/activate  # Linux
  .\env\Scripts\activate   # Windows
  ```
- Jika ada masalah dalam eksternal menejemen environment:
  ```bash
  pip install nama-library --break-system-packages
  ```


---

## 🚀 Yuk Coding!

Setelah Python terpasang, kamu bisa langsung mulai membuat program menggunakan editor favoritmu seperti:
- Linux/Windows: VS Code, Sublime Text, PyCharm
- Android: Pydroid 3 Editor bawaan

sekarang kalian bisa mencoba skrip skrip diatas:
   ```bash
  git clone 
  ```
---

Semoga bermanfaat! 🐍✨
