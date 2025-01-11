# Smart Transportation System

Smart Transportation System adalah sistem yang bertujuan untuk memberikan prediksi rute perjalanan yang optimal menggunakan data dari API HERE, dengan memanfaatkan teknologi informasi untuk meningkatkan efisiensi transportasi. Sistem ini mengintegrasikan data lalu lintas untuk memberikan estimasi waktu perjalanan dan jarak yang dibutuhkan.

## Fitur Utama
- **Prediksi Rute**: Menentukan rute perjalanan optimal antara dua titik (origin dan destination) berdasarkan kondisi lalu lintas saat ini.
- **Informasi Durasi dan Jarak**: Menampilkan durasi estimasi perjalanan dalam format jam dan menit, serta jarak dalam kilometer.
- **Peta Interaktif**: Menampilkan rute perjalanan di peta menggunakan poliline untuk menggambarkan jalur dari origin ke destination.
  
## Teknologi yang Digunakan
- **Flask**: Framework Python untuk membangun aplikasi web.
- **HTML/CSS**: Untuk tampilan antarmuka pengguna.
- **Leaflet.js**: Untuk menampilkan peta dan menggambar rute perjalanan.
- **HERE API**: Untuk mendapatkan data rute dan prediksi perjalanan.
  
## Prasyarat
Sebelum menjalankan aplikasi, pastikan Anda telah menginstal:
- **Python 3.x**
- **Flask**
- **Requests**
  
## Instalasi

1. **Clone Repositori ini**

   Gunakan perintah `git` untuk menyalin repositori ini ke komputer lokal Anda:
   ```bash
   git clone https://github.com/ars1810/smart-transportation-system.git
   ```

2. **Install Dependensi**

   Setelah repositori ter-clone, instal dependensi Python yang diperlukan:
   ```bash
   cd smart-transportation-system
   pip install -r requirements.txt
   ```

3. **API Key**

   Anda memerlukan API key dari HERE untuk dapat mengakses rute dan prediksi perjalanan. Daftarkan akun di [HERE Developer](https://developer.here.com/) dan ambil API key Anda. Masukkan API key Anda pada variabel `HERE_API_KEY` di file `app.py`.

4. **Jalankan Aplikasi**

   Setelah semua langkah di atas selesai, jalankan aplikasi dengan perintah berikut:
   ```bash
   python app.py
   ```

5. **Akses Aplikasi di Browser**

   Akses aplikasi melalui browser dengan membuka URL berikut:
   ```
   http://127.0.0.1:5000/
   ```

## Penggunaan

1. **Masukkan Lokasi**

   Pada halaman utama, masukkan lokasi asal (origin) dan tujuan (destination) pada kolom yang tersedia.

2. **Pilih Mode Transportasi**

   Pilih mode transportasi (misalnya mobil, sepeda, atau pejalan kaki) untuk mendapatkan rute yang sesuai.

3. **Dapatkan Rute**

   Setelah klik "Find Route", aplikasi akan memproses rute perjalanan menggunakan HERE API dan menampilkan hasil berupa estimasi durasi, jarak, dan peta rute perjalanan.

## Contributing

Jika Anda ingin berkontribusi pada proyek ini, silakan lakukan fork repositori ini dan buat pull request dengan perubahan yang ingin Anda ajukan. Pastikan untuk mengikuti pedoman berikut:
- Jelaskan dengan jelas perubahan yang Anda buat.
- Ikuti standar kode dan penulisan yang sudah diterapkan.
- Pastikan untuk menguji aplikasi sebelum membuat pull request.

## Lisensi

Proyek ini dilisensikan di bawah **MIT License**. Lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.

---

Terima kasih telah menggunakan Smart Transportation System! Semoga aplikasi ini dapat membantu Anda dalam merencanakan perjalanan lebih efisien dan optimal.
```

### Penjelasan Beberapa Bagian:
- **Fitur Utama**: Menjelaskan fitur yang dimiliki oleh aplikasi.
- **Teknologi yang Digunakan**: Memberikan informasi tentang teknologi dan library yang digunakan dalam proyek.
- **Prasyarat**: Menyebutkan perangkat lunak yang harus diinstal untuk menjalankan aplikasi.
- **Instalasi**: Langkah-langkah untuk menyiapkan dan menjalankan aplikasi.
- **Penggunaan**: Menjelaskan cara pengguna dapat berinteraksi dengan aplikasi.
- **Contributing**: Mendorong orang untuk berkontribusi pada proyek dan memberikan pedoman kontribusi.
- **Lisensi**: Menyediakan informasi tentang lisensi yang diterapkan pada proyek.