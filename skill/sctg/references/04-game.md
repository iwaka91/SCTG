<!-- Disalin tanpa perubahan dari SCTG_V4.4.md, baris 405,483 -->

## B6. Game

### B6.1 Palet Mekanik Resmi

**Drag-and-drop dihapus permanen.** Mekanik resmi (berbasis sentuh/ketuk):

| Mekanik | Cara main singkat | Paling cocok untuk |
|---|---|---|
| **Balon/Bola** | Objek bergerak disentuh untuk ditangkap | Reaksi cepat, hitung cepat |
| **Jeep/Kendaraan** | Kendaraan dikendalikan sentuh langsung ke arah tujuan dan/atau tombol arah/joystick (lihat B6.6) | Navigasi, ruang bebas |
| **Ban Berjalan (Conveyor Sort)** | Objek berjalan dilempar ke keranjang kategori | Klasifikasi |
| **Ketok Cepat (Whack Target)** | Objek muncul sebentar, disentuh sebelum hilang | Recall cepat |
| **Flip Card** | Kartu dibalik mencari pasangan | Istilah–definisi (hati-hati: terasa janggal bila dipaksakan pada materi prosedural) |
| **Susun Runtun** | Tukar posisi dua kotak hingga urut | **Hanya** untuk rantai prasyarat tunggal yang tegas |
| **Gerbang Pilihan (Lane Runner)** | Karakter berjalan, sentuh kiri/kanan memilih gerbang | Keputusan cepat beruntun |
| **Roda Nasib (Spin Wheel)** | Roda berhenti acak di skenario | Pembuka rasa penasaran |
| **Susur Sungai (Kompas Perahu)** | Perahu menyusuri sungai, berhenti di titik soal | Ruang + konteks Kalteng |
| **Menara Kayu Betang (Tower Builder)** | Benar menambah balok, salah menara bergetar | Progres kumulatif |
| **Rantai Sebab-Akibat** | Satu pertanyaan per sambungan (pilih akibat langsung dari 2–3 pilihan), dibangun selangkah demi selangkah | Penalaran bertahap dari data murid sendiri; **pengganti standar Susun Runtun** untuk materi berstruktur rantai prasyarat |
| **Perjalanan Bergerbang** | Kendaraan berhenti di gerbang keputusan, konsekuensi terbawa ke gerbang berikut | Simulasi keputusan berantai (satu perjalanan, bukan ronde berulang) |

Pengganti drag-and-drop lain yang sah: tap-to-match, hotspot, branching choice, radar target, interactive map.

### B6.2 Standar Visual Game & Ilusi 3D (pseudo-3D)

Langkah game **tidak boleh terlihat seperti kode malas**:

- **WAJIB canvas** — tidak boleh grid tombol DOM berwarna rata.
- **Ilusi 3D tanpa render 3D** (Canvas 2D/CSS saja, tanpa WebGL/pustaka):
  - **Gradasi volume** — sisi terang & sisi gelap dari satu sumber cahaya yang konsisten (disarankan kiri-atas).
  - **Cahaya** — glow radial pada elemen kunci (target, boss, gerbang, ikon hadiah), rim light tipis di tepi objek.
  - **Bayangan berlapis** — contact shadow elips di bawah objek + drop shadow lembut.
  - **Kilau kaca (glass highlight)** — kilap lengkung putih transparan di sisi atas objek mengkilap (koin, kartu kunci, tombol utama, panel kaca, gelembung jawaban). Dipakai **selektif**.
  - **Parallax** berlapis untuk latar bergerak.
- Gerak natural (easing), umpan balik tersinkron audio, perayaan kecil (konfeti/partikel tanpa pustaka).
- Efek berlaku merata untuk **semua** langkah game, sinematik, dan cover (serta Mission Map bila dipakai) — bukan hanya satu game favorit. Langkah membaca/refleksi/form tetap **bersih dan fungsional** (boleh aksen kaca ringan pada kartu/tombol utama).

### B6.3 Kesesuaian Mekanik dengan Struktur Materi (WAJIB)

Pelajaran dari kasus "Susun Runtun" SEJX06: memaksa peristiwa campuran (prasyarat logis + siklus berulang + skala waktu berbeda) ke satu garis urutan tanpa kriteria eksplisit hanya bisa diselesaikan lewat coba-coba, bahkan oleh guru senior. Karena itu, sebelum memilih mekanik, periksa struktur logis materi:

- **Rantai prasyarat tunggal, tak ambigu** → mekanik urut boleh dipakai, tetapi dibangun **selangkah demi selangkah** (tampilkan sebab, tanya akibat langsung dari 2–3 pilihan), **bukan** menyusun banyak kartu lepas sekaligus (mencegah tebak-tebakan kombinatorial).
- **Siklus berulang / proses tanpa titik waktu tunggal** → jangan dipaksa jadi garis urutan; gunakan **pengelompokan/klasifikasi (Ban Berjalan) atau diagram siklus**, bukan sequencer linear.
- **Beberapa jalur sejajar/independen** → jangan dipaksa jadi satu urutan; **gabungkan simpul yang sebenarnya sejajar menjadi satu simpul**, atau gunakan **pencocokan (Flip Card/pairing)**, bukan urutan mutlak.
- Bila mekanik menuntut "urutkan berdasarkan X", **X dinyatakan eksplisit** kepada murid (kronologis? prasyarat logis? sebab-akibat?).
- Simulasi cukup **satu perjalanan utuh**; jangan ronde berulang yang membuat murid pusing.

### B6.4 Jeda Paham (WAJIB untuk game bertekanan waktu/refleks)

- Setelah jawaban (benar/salah), game berhenti penuh; muncul modal penjelasan **non-skippable**.
- Hitung mundur mengunci tombol **"Saya Paham"**: detik = jumlah kata penjelasan ÷ 3 (dibulatkan ke atas), **minimal 10 detik, tanpa batas atas** (Tabel Konstanta Waktu, B24). Hitung mundur adalah waktu baca minimum; murid boleh membaca lebih lama, dan modal tidak menutup sendiri. Bila penjelasan menghasilkan kunci > 30 detik, AI melaporkannya (Pola Penawaran, 2.6) agar guru memutuskan — pemicu laporan, bukan larangan. Murid harus menekan tombolnya sendiri untuk melanjutkan (tidak otomatis lanjut); tombol terlihat nonaktif sejak awal dan menjadi aktif secara senyap (Kunci Senyap, B24 aturan 5).
- **Skin tematik per game** (contoh: gulungan pelaut untuk Susur Sungai, kartu katalog museum untuk Ban Berjalan, struk belanja/buku bendahara untuk NUM07) — bukan satu gaya generik.
- Fasil/EZ: modal tetap tampil (agar dapat dicek/didemokan) tetapi hitung mundur dipercepat ke 2 detik.
- Final Boss dikecualikan (asesmen sumatif penutup, bukan tempat mengajar) kecuali diminta eksplisit.

### B6.5 Level Kecepatan Game

Game bertekanan waktu/refleks (Susur Sungai, Ban Berjalan, Ketok Cepat, dan sejenisnya) wajib menyediakan pilihan level sebelum permainan dimulai:

| Level | Kecepatan |
|---|---|
| **Santai** | ±×0,5 |
| **Sedang** | ±×0,75 |
| **Standar** (bawaan) | ×1 (kecepatan asli) |

- Murid dapat mengubah level di tengah permainan lewat tautan **"Ubah level"** pada modal Jeda Paham (B6.4); perubahan berlaku mulai soal berikutnya, bukan soal yang sedang berjalan.
- Level **hanya mengubah kecepatan** — tidak boleh mengubah syarat penyelesaian, materi, atau isi sertifikat.
- Final Boss tidak wajib memiliki pilihan level (sudah berjalan dalam mode Bandel), kecuali diminta eksplisit.
- Nama level sengaja **Santai/Sedang/Standar** agar tidak tertukar dengan mode EZ.

### B6.6 Kontrol Virtual & Sentuh Langsung (WAJIB)

- Bila game menyediakan **kontrol virtual** (tombol panah, joystick, kemudi), kontrol itu **tidak boleh menjadi satu-satunya cara bermain.**
- Game **wajib** dapat dimainkan dengan **sentuh langsung pada arena**: ketuk sisi kiri/kanan (atau jalur/tujuan) untuk bergerak atau memilih, geser (swipe) bila relevan, dan ketuk objek langsung untuk menangkap/memilih.
- Zona sentuh langsung cukup besar (mis. tiap sisi kiri/kanan minimal sepertiga lebar arena; objek ≥ ukuran target sentuh A10).
- Di laptop, **klik mouse** dan **keyboard** (panah / A-D / Spasi / Enter) juga berfungsi. Di IFP, sentuh langsung menjadi cara utama.
- Kontrol virtual, bila ada, **tidak menutupi arena** dan **tidak menambah tinggi pita jawaban** (agar kedua mode tetap satu layar, A10f); boleh disembunyikan di Mode Panggung karena sentuh langsung tersedia.
- Pengujian otomatis mencakup jalur sentuh langsung dan (bila ada) kontrol virtual.

