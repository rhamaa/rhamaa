# Portofolio Rhamaa

Website satu halaman berbahasa Indonesia untuk memperkenalkan Firdaus Nuur Rhamadhan melalui proyek pilihan, perjalanan proyek, pengalaman, pendidikan, dan kontak LinkedIn.

## Menjalankan secara lokal

Gunakan Node.js 22.12.0 atau lebih baru.

```bash
npm install
npm run dev
```

Astro menampilkan alamat lokal di terminal. Untuk membuat versi statis:

```bash
npm run build
npm run preview
```

Hasil siap-host berada di folder `dist/`. Jalankan pemeriksaan data dan halaman dengan:

```bash
npm test
```

Perintah tes otomatis membangun ulang halaman terlebih dahulu agar pemeriksaan selalu memakai output terbaru.

## Memperbarui isi

Ubah satu sumber isi di `src/data/portfolio.json`. URL proyek hanya ditampilkan jika repositorinya sudah diverifikasi. Runutin belum memiliki tautan publik di halaman ini. Status Captr Studio dan prototipe Kirei sengaja ditampilkan secara eksplisit.

Situs menggunakan Astro dengan keluaran statis. JavaScript kecil mengaktifkan penanda navigasi dan dialog detail proyek; pengalaman menggunakan elemen `details` bawaan browser. Halaman tidak membutuhkan server aplikasi atau basis data.

## Desain dan aset

Desain mengikuti lima gambar referensi dari chat: hero desktop, proyek pilihan, perjalanan, pengalaman/kontak, dan versi ponsel. Ilustrasi asli disimpan di `public/art/` dan ditampilkan melalui viewport SVG; judul, isi, navigasi, dan tombol tetap HTML yang dapat dipilih dan diakses lewat keyboard. Font DM Sans disimpan di `public/fonts/` sehingga tidak perlu permintaan Google Fonts saat membuka situs.

`technology-standalone.webp` dihasilkan dengan tool imagegen bawaan untuk tampilan tablet, menggunakan hero asli sebagai target ekstraksi. Brief: ambil ilustrasi laptop, mikrokontroler, sensor, kabel teal/amber, dan skema elektronik; pertahankan perspektif dan warna; hapus seluruh teks, logo, navigasi, dan tombol website. Deskripsi proyek dan tautan tetap mengikuti data repo yang telah diverifikasi, termasuk keterangan telemetri simulasi Kirei.
