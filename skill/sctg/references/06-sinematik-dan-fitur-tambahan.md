<!-- Disalin tanpa perubahan dari SCTG_V4.4.md, baris 586,655 -->

## B22. Sinematik Pra-Aktivitas (SANGAT DISARANKAN, tidak wajib)

**Tujuan:** memberi bobot emosional dan rasa penasaran pada gerbang berbobot tinggi, sehingga murid menanti "kejutan" berikutnya.

**Titik pemasangan:** pengantar **TP** (setelah login, sebelum layar TP) dan pengantar **Final Boss** (sebelum duel dimulai). Boleh di gerbang besar lain bila tema mendukung.

**Anatomi:**

1. **Latar visual tematik** di canvas, beranimasi (contoh: laut tenang untuk pengantar TP; badai/tegang untuk Boss), memakai pseudo-3D (B6.2).
2. **4–6 beat teks** muncul satu demi satu dengan transisi fade/slide, **disinkronkan dengan efek suara**.
3. **Tempo baca ditetapkan dari panjang teks**, bukan dari kenyamanan pembuat: durasi beat ≈ **jumlah kata ÷ 2,5 detik + 1 detik, minimal 3 detik**, diuji keterbacaannya oleh murid berkecepatan baca sedang. Total ±15–25 detik. (Acuan awal bila belum ada data: 0,75 dari tempo draf pertama.) Rumus ini tercatat di Tabel Konstanta Waktu (B24).
4. **Minimal satu elemen kejutan** yang tidak bisa ditebak (kemunculan karakter, perubahan cuaca, twist kecil, benda yang jatuh/terbuka) — berbeda di tiap course.
5. **Layar ajakan bertindak (CTA) terkunci** di akhir: tombol lanjut baru aktif setelah beat terakhir, murid menekan secara sadar.
6. Pengantar Boss **memperlihatkan aturan main**: pada **Bandel** (cara menyerang, jumlah soal, PG kompleks ×2, perilaku boss); pada **Tuntas** (satu paket = 8 PG + 2 PGK, skor PG 10 dan PGK 20, ambang tuntas 70, PGK wajib benar minimal 1, boleh mengulang paket).

**Perilaku:**

- Tampil **otomatis sekali per sesi belajar** (flag di state; flag dihapus saat Ulangi/Reset).
- Tombol **"↻ Ulang"** wajib ada di layar sinematik dan dapat ditekan kapan saja selama berjalan (mengulang dari beat pertama), agar murid yang belum sempat membaca tidak perlu menunggu sampai selesai.
- **🎬 Tonton Ulang** tersedia di layar aktivitas terkait; saat tonton ulang tersedia tombol tutup (✕).
- **Varian mikro acak** saat tonton ulang (2–3 varian kalimat/detail per beat) agar tidak identik.
- **Fasil/EZ:** tombol **"⏭ Lewati Animasi"** tampil sejak awal (bukan dilewati otomatis).
- Menghormati `prefers-reduced-motion` (transisi dipersingkat, tetap terbaca).
- Mode Panggung: teks beat besar, terbaca dari belakang kelas.

**Aturan desain:** jangan monoton — suasana, palet, adegan, dan kejutan mengikuti tema course. Dilarang menyalin sinematik course lain hanya dengan ganti teks.

## B23. Unduhan Berkas Tahan-Gagal

Setiap fitur yang menghasilkan berkas untuk diunduh murid (mis. sertifikat PDF, kartu gambar) wajib memiliki **dua jalur**:

1. **Jalur utama:** unduhan langsung.
2. **Jalur cadangan**, dijalankan otomatis bila jalur utama tidak berhasil: membuka atau membagikan berkas lewat penampil/menu berbagi peramban, disertai petunjuk singkat penyimpanan manual.

Ketentuan ini berlaku karena course SCTG harus tetap berfungsi baik saat diakses lewat tautan daring maupun saat berkas HTML dibuka langsung dari perangkat tanpa internet, dan sebagian peramban seluler (khususnya Chrome Android) membatasi unduhan otomatis pada berkas lokal. Jalur cadangan **tidak boleh mengubah isi berkas maupun perilaku** pada perangkat yang jalur utamanya sudah berhasil. Wajib diuji pada minimal satu perangkat Android dengan berkas dibuka langsung tanpa deploy; bila tidak dapat diuji, dilaporkan sebagai **"belum teruji di perangkat asli"** (Bagian 6).

## B24. Jam Kunci Serentak

Semua kunci waktu dalam course (Gerbang Baca B3, Jeda Paham B6.4, kunci Kesimpulan B14) memakai **satu mesin hitung mundur yang sama** dan **satu tabel konstanta**, dengan lima aturan:

1. Dipercepat menjadi **2 detik** pada Fasil/EZ.
2. Selalu dapat diskalakan lewat **pengali uji** (untuk QA otomatis).
3. Tombol lanjut **tidak pernah aktif sebelum hitung mundur habis**.
4. Hitung mundur **hanya berjalan saat isi terbuka dan layar terlihat**; selebihnya berjeda dan sisa detik disimpan (B3 butir 2b).
5. **Kunci Senyap** (zona membaca, memahami, dan menyalin). Saat hitung mundur berakhir pada Gerbang Baca, Ruang Baca, Jeda Paham, kunci Kesimpulan, dan centang konfirmasi akhir: **tidak ada** suara, animasi berkedip/denyut, konfeti, toast, scroll, maupun perpindahan fokus otomatis. Yang berubah hanya **tombol yang sudah ada sejak awal**: dari abu-abu (nonaktif) menjadi warna aksen tema (aktif), dengan transisi ≤ ±200 ms dan menghormati `prefers-reduced-motion`. Indikator timer tidak bergantung pada warna: angka menurun sampai 0 lalu berganti ✅; status ikon berganti diam-diam. Sinematik dan game dikecualikan (zona dramatis). Bunyi "tap" saat murid menekan tombol tetap boleh karena itu tindakan murid.

**Tabel Konstanta Waktu** (satu-satunya sumber angka waktu baca dan kunci waktu):

| Kunci | Rumus | Minimum | Batas atas | Fasil/EZ |
|---|---|---|---|---|
| Gerbang Baca (B3) | jumlah kata ÷ 3, dibulatkan ke atas | 5 dtk | tidak ada | 2 dtk |
| Jeda Paham (B6.4) | jumlah kata ÷ 3, dibulatkan ke atas | 10 dtk | tidak ada (lapor bila > 30 dtk) | 2 dtk |
| Beat Sinematik (B22) | jumlah kata ÷ 2,5 + 1 dtk | 3 dtk | total sinematik ±15–25 dtk (sasaran) | tombol ⏭ Lewati Animasi |
| Kunci Kesimpulan (B14) | menyesuaikan panjang catatan | — | 5 menit | 2 dtk |

- Pada Gerbang Baca dan Jeda Paham, hitung mundur adalah **waktu baca minimum**, bukan waktu baca penuh (B3 butir 2 dan 2a).
- Pembuat course boleh menyetel pembagi (mis. ÷2,5 untuk teks padat istilah) dan mencatatnya di Pola Penawaran.
- Perbedaan antarbaris disengaja: sinematik berjalan otomatis sehingga lebih lambat (±150 kata/menit + 1 detik per beat); Kunci Kesimpulan mempertahankan batas atas karena tujuannya memberi waktu menyalin, bukan menahan materi TP.

**Syarat keterbacaan perubahan tombol (Kunci Senyap)** — terukur, dan aman untuk buta warna serta layar terkena sinar matahari:

- Tombol aktif **lebih gelap dan lebih jenuh** daripada tombol nonaktif; tombol nonaktif pucat dengan teks redup; teks tombol aktif putih tegas. Tidak memakai gembok (indikator timer sudah menjelaskan keadaan tombol).
- Rasio kontras (usulan angka, disetel dari uji lapangan): tombol aktif terhadap latar halaman ≥ 3:1 (acuan WCAG untuk komponen antarmuka); teks tombol aktif ≥ 4,5:1; selisih kecerahan tombol aktif–nonaktif jelas (usulan ≥ 1,5:1).
- Warna aktif yang disarankan **biru** (paling terbedakan oleh buta warna merah-hijau). Hijau hanya boleh bila lolos pengukuran kecerahan; oranye bergantung pada kecerahan.
- Berlaku di tema terang dan gelap. Pengukuran dilakukan dengan angka (rasio kontras; boleh ditambah simulasi protan/deutan secara hitungan), bukan dengan gambar.

## B25. Emoji Bergerak

Ikon/emoji pada layar (pulse-check refleksi, indikator status, dsb.) memakai **animasi CSS ringan** (denyut, goyang, mengapung) tanpa berkas gambar/animasi tambahan, sehingga tidak menambah beban muat berkas tunggal. Menghormati `prefers-reduced-motion`.

