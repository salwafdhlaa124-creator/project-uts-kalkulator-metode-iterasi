Kelompok 1 : Metode Iterasi
1. Salwa Fadhilla
2. Putri Rahmatul 'Ulya
3. Muhammad Rayyan
4. Muhammad Isyraq Akramim
5. Imam As-Shadiq
6. Farras Arthada Siregar

##Kalkulator Metode Iterasi Titik Tetap
1. Deskripsi Proyek
      Kalkulator metode iterasi adalah aplikasi yang berbasis python yang dirangcang untuk membantu dalam menghitung serta memvisualisasikan penyelesaiain non-linier.
dalam motode numerik, motote iterasi titik tetap mengubah persamaan f(x) = 0 menjadi bentuk x = g(x). dilengkapi dengan antarmuka grafis (GUI) tabel riwayat iterasi otomatis, 
serta grafik konvergensi secara real-time

2. Fitur utama
    - Antarmuka Grafis (GUI) : dibangun menggunakan pustaka 'tkinter' dengan desain warna yang nyaman dipandang.
    - Pilihan Persamaan Fleksibel : menyediakan dropdown untuk contoh fungsi g(x) dan mendukkung fungsi matematika kustom.
    - Tabel Riwayat Iterasi : menampilkan nomor iterasi , nilai x_n, g(x_n), dan besar error/absolut.
    - Visualisasi Grafik Konvergensi : Menggunakan 'matplotlib' untuk menggambarkan kurva fungsi y = g(x), garis acuan y = x, serta titik temu akar secara otomatis.
    - Validasi Input : Mencegah program crash akibat from kosong, input tipe data yang salah, atau rumusan ekspresi matematika yang tidak valid.

3. Prasyarat dan Spesifikasi Sistem
Agar aplikasi bisa dijalankan, komputer harus memiliki Python versi 3.8 atau lebih baru sebagai bahasa pemrograman utama. Selain itu, aplikasi membutuhkan Matplotlib versi 3.x untuk membuat grafik yang menunjukkan proses konvergensi atau perubahan hasil perhitungan selama iterasi.
Untuk memasang Matplotlib, buka Command Prompt atau Terminal, lalu ketik perintah berikut:
'pip install matplotlib'

4. Panduan Penggunaan Aplikasi
1). Pilih atau Masukkan Persamaan g(x): Pilih fungsi yang tersedia pada dropdown, seperti 'math.sqrt(2 + x)` atau 'math.cos(x)'. Pengguna juga bisa memasukkan fungsi sendiri menggunakan penulisan matematika python.
2). Tentukan Tebakan Awal (x0): Masukkan nilai awal yang diperkirakan mendekati akar persamaan, misalnya 1.0.
3). Atur Toleransi Error: Masukkan batas kesalahan yang digunakan untuk menghentikan iterasi, misalnya 0.00001 atau 1e-5.
4). Atur Maksimum Iterasi: Tentukan jumlah perulangan paling banyak agar proses perhitungan tidak berjalan terus-menerus, misalnya 50 kali.
5). Proses Perhitungan: Klik tombol Hitung Akar untuk menjalankan perhitungan dan menampilkan grafik hasilnya.
6). Reset Input: Klik tombol Reset Form untuk mengosongkan semua kolom input, menghapus hasil perhitungan, dan mengembalikan grafik ke kondisi awal.5. Arsitektur Komponen Kode
Program ini dibuat menggunakan beberapa fungsi yang memiliki tugas masing-masing. Tujuannya agar bagian tampilan aplikasi dan proses perhitungan lebih teratur dan mudah dipahami.

a. Fungsi 'hitung()'
Fungsi ini bertugas membaca input yang dimasukkan pengguna, memeriksa apakah input sudah benar, melakukan perhitungan iterasi menggunakan rumus Xbaru = g(x), menampilkan hasil pada tabel, dan membuat grafik.

b. Fungsi 'buat_grafik()'
Fungsi ini digunakan untuk membuat grafik fungsi y = g(x), garis diagonal y = x, dan menandai titik akar yang berhasil ditemukan ketika perhitungan mencapai hasil yang konvergen.

c. Fungsi 'reset_form()'
Fungsi ini digunakan untuk mengosongkan kolom input, menghapus hasil pada tabel iterasi, dan mengembalikan tampilan grafik seperti semula.
