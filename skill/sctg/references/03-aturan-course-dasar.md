<!-- Disalin tanpa perubahan dari SCTG_V4.4.md, baris 342,404 -->

# BAGIAN B — Aturan Course

## B1. Struktur Perjalanan Belajar

Lihat 2.3. Materi tidak seluruhnya permainan; wajib ada fase membaca, eksplorasi, aktivitas interaktif, asesmen/tantangan, kesimpulan, dan reward.

## B2. Model Pembelajaran

Lihat 2.2.

## B3. Gerbang Baca Berurutan (WAJIB, semua course)

**Cakupan:** daftar TP pada langkah 1 (**selalu**) dan **setiap langkah lain yang memuat banyak teks bacaan** — yaitu bagian yang lebih dari ±60 kata, atau langkah yang memiliki 2 bagian bacaan atau lebih (mis. kartu Materi/Kantong Rumus, arsip). Instruksi pendek tidak ikut dikunci.

**Cara kerja (verifikasi bertahap: collapse-expand + hitung mundur + toast):**

1. Bagian bacaan ditampilkan **tertutup** berupa ikon/kartu bernomor (TP1, TP2, TP3 / Materi 1, 2, 3, dst.).
2. Isi ikon **terbuka saat diketuk**, dan saat itu **hitung mundur** berjalan. Durasi dihitung dari **jumlah kata** isi ikon: **detik = jumlah kata ÷ 3** (±180 kata/menit, dibulatkan ke atas), **batas bawah 5 detik**. **Tidak ada batas atas per ikon maupun batas total per langkah.** Hitung mundur adalah **waktu baca minimum**, bukan waktu baca penuh; murid tetap boleh membaca lebih lama. Pembuat course boleh menyetel pembagi (mis. ÷2,5 untuk teks padat istilah) dan mencatatnya di Pola Penawaran. Rumus dan konstanta waktu lain tercatat di Tabel Konstanta Waktu (B24).
   - **2a. Ikon tidak pernah menutup sendiri.** Isi ikon hanya tertutup karena tindakan murid: mengetuk ikon itu lagi, mengetuk ikon lain pada tampilan satu-terbuka, atau ✕ di Ruang Baca (B3.1). Habisnya hitung mundur **tidak boleh** menutup, menggulung, atau menggeser layar. Saat hitung mundur habis hanya terjadi tiga hal: (1) cincin/angka berubah menjadi ✅ selesai (angka tidak dibiarkan tampil); (2) tombol **"Lanjut ke [ikon berikutnya] →"** — yang **sudah terlihat sejak awal dalam keadaan nonaktif** di dalam kartu — menjadi aktif **tanpa suara dan tanpa sorotan** (Kunci Senyap, B24 aturan 5); pada ikon terakhir tombolnya **"Selesai Membaca"**; sama dengan B3.1 butir 3 sehingga Mode Genggam dan Mode Panggung seragam; (3) ikon berikutnya berstatus ▶ giliran, tetapi **tidak terbuka sendiri** dan layar **tidak digulung otomatis**. Menekan "Lanjut ke …" adalah tindakan murid, jadi boleh membuka ikon berikutnya sekaligus menutup ikon yang lama.
   - **2b. Jam hanya berjalan saat dibaca.** Hitung mundur berjalan hanya selama isi ikon terbuka **dan** layar terlihat. Bila aplikasi ditutup, tab atau layar tersembunyi, atau kartu ditutup/✕ ditekan di tengah hitungan, hitung mundur **berjeda** — bukan diulang dan bukan dianggap selesai. Sisa detik disimpan bersama kemajuan baca (butir 7) dan dilanjutkan dari sisa itu saat ikon dibuka lagi.
3. Ikon berikutnya **baru dapat dibuka setelah hitung mundur ikon sebelumnya habis.**
4. Bila murid mengetuk ikon yang belum gilirannya, tampil **toast peringatan singkat** (contoh: *"Baca TP1 terlebih dahulu"*) dan tidak terjadi perubahan lain.
5. Ikon yang sudah selesai dibaca boleh dibuka-tutup bebas untuk dibaca ulang tanpa hitung mundur baru.
6. **Kotak konfirmasi/ceklis akhir** ("Saya telah membaca dan memahami…") baru aktif setelah **seluruh ikon selesai dibaca**.
7. **Kemajuan baca disimpan** di perangkat; murid yang menutup berkas tidak mengulang dari awal. Kemajuan (termasuk sisa detik ikon yang sedang berjalan, butir 2b) dihapus saat Ulangi/Reset.
8. **Fasil/EZ:** hitung mundur dipercepat ke **2 detik**, tetapi **urutan dan toast peringatan tetap berlaku** agar dapat didemonstrasikan.
9. **Beban dijaga lewat isi, bukan waktu:** satu ikon idealnya **≤ ±150 kata**. Bila lebih, **pecah menjadi ikon baru** atau padatkan tanpa membuang substansi TP. Bila total waktu kunci satu langkah melebihi **±3 menit**, AI melaporkannya saat Pola Penawaran (2.6) agar guru memutuskan; angka ini pemicu laporan, bukan larangan. *Catatan:* empat ikon berisi ±150 kata (masing-masing 50 detik) sudah melampaui 3 menit, jadi laporan akan cukup sering muncul; ini disengaja sebagai pemicu diskusi. Kedua angka belum diuji lapangan: total waktu kunci per langkah dicatat di tiga course pertama sebelum angka ditinjau.
10. **Maksimal 6 ikon per Gerbang Baca.** Bila bacaan lebih dari 6 ikon, pecah menjadi dua gerbang — bukan menambah ikon. Alasan: di layar terpendek Mode Panggung (±1280×650), menu Ruang Baca dengan target sentuh IFP ≥56 px ditambah progress bar dan centang mulai tidak muat pada kisaran 8–9 ikon (perhitungan kasar, belum diuji); batas 6 menyisakan ruang aman untuk huruf Aa sangat besar.

Semua kunci waktu memakai mesin dan tabel konstanta yang sama (B24).

## B3.1 Ruang Baca Panggung (WAJIB di Mode Panggung)

Di Mode Panggung (A10), Gerbang Baca **tidak** ditampilkan sebagai accordion atau grid, melainkan sebagai **Ruang Baca** dengan dua keadaan. Tujuannya: bacaan terbaca dari belakang kelas di IFP tanpa halaman bergulir, dan urutan baca tetap terkendali.

**(a) Keadaan Daftar** (belum ada ikon yang dibuka):

- Semua ikon bacaan tersusun **satu kolom di tengah layar** (lebar ±640–760 px).
- Tiap ikon memuat ikon tematik, nomor, judul, dan status: ▶ giliran · ⏳ sedang dibaca · 🔒 terkunci · ✅ selesai.
- Progress bar di atas, kotak konfirmasi (centang) di bawah.

**(b) Keadaan Baca** (setelah ikon diketuk):

- Daftar **bergeser ke kanan** (animasi ±300 ms) menjadi **menu ringkas** (±260–320 px), seperti daftar menu.
- **Panel baca mengisi area tengah** hampir penuh: judul, cincin/hitung mundur, isi berhuruf besar (**≥18 px**; **≥20 px** di IFP), dan tombol ✕.

**Aturan:**

1. Panel baca adalah **panel di dalam halaman, bukan modal overlay**. Header tetap berfungsi; 🔉 Dengarkan membacakan isi panel aktif.
2. **Halaman tidak scroll.** Bila isi panjang, hanya panel baca yang scroll di dalam.
3. Tombol **"Lanjut ke [ikon berikutnya] →"** sudah terlihat di panel sejak ikon dibuka, dalam keadaan nonaktif (abu-abu); setelah hitung mundur habis ia menjadi aktif secara senyap (B24 aturan 5). Pada ikon terakhir tombolnya **"Selesai Membaca"**. Ikon tetap terbuka setelah hitung mundur habis (B3 butir 2a).
4. Menu kanan tunduk pada B3: berurutan, **toast peringatan** untuk ikon yang belum gilirannya, baca ulang bebas tanpa hitung mundur baru.
5. **Centang konfirmasi berada di bawah menu kanan**, selalu terlihat tanpa scroll; aktif hanya setelah semua ikon selesai dibaca. **Pengaman:** bila menu tetap tidak muat (mis. huruf Aa sangat besar), hanya daftar ikon yang scroll di dalam; centang tetap menempel di bawah dan terlihat.
6. **✕** mengembalikan tampilan ke Keadaan Daftar; kemajuan baca tidak hilang. ✕ adalah tindakan murid (B3 butir 2a); bila hitung mundur sedang berjalan, ia berjeda dan sisa detiknya disimpan (B3 butir 2b).
7. Berlaku untuk **semua Gerbang Baca** (TP, Materi, Arsip B11). **Mode Genggam tetap accordion satu kolom** (B3).
8. Perpindahan antar-mode (layar diputar atau jendela diubah ukuran) **tidak mengulang hitung mundur maupun menghilangkan kemajuan baca** (sisa detik dibawa, B3 butir 2b).
9. Visual mengikuti aturan langkah membaca (B6.2): bersih dan fungsional, boleh aksen kaca ringan pada panel dan kartu.
10. Fasil/EZ: hitung mundur 2 detik, urutan dan toast tetap berlaku (B3 butir 8).

## B4–B5. Aktivitas Bergerak & Tangkap Jawaban

Objek bergerak dengan visual multiwarna, pseudo-3D, gerak natural. Benar → flash/pop + chime; salah → shake + error sound. Kecepatan boleh progresif.

