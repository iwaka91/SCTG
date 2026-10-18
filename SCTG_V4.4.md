# SCTG V.4.4 — Standar Course Toto Gutomo
**Status:** Resmi
**Versi:** 4.4
**Tanggal berlaku:** 18 Oktober 2026 (V.4.3: 5 Oktober 2026; V.4.2 dan V.4.2.1: 30 September 2026; V.4 dan V.4.1: 29 September 2026)
**Disusun:** Toto Gutomo (Wakasek Kurikulum, SMA Negeri 3 Maliku, Kalimantan Tengah) bersama Claude
**Riwayat:** V.2 (TKA) → V.3 (CLAUDE.md, referensi SEJXI07) → V.3.1 (rekonsiliasi teknis-pedagogis) → V.3.2 (bedah SEJX06 + audit NUM07/LIT07) → V.4 → V.4.1 → V.4.2 → V.4.2.1 → V.4.3 → **V.4.4 (dokumen ini)**
**Menggantikan:** SCTG V.4.3, V.4.2.1, V.4.2, V.4.1, V.4 (4.0), V.3.2, dan V.3.1
**Berkas pendamping:** *SCTG_Changelog_dan_Ringkasan.md* — changelog lengkap, ringkasan riwayat, catatan temuan, keputusan & status (terakhir sinkron: V.4.3; belum memuat V.4.4). **Tidak wajib dimuat** untuk membangun course.
**Reference implementation:** NUM07 v4 — *Bertahan dengan Anggaran Terbatas* (series NUM); SEJXI07 (arsip V.3, 9,2/10)

---

## Cara Pakai Dokumen Ini

Dokumen ini adalah **satu-satunya sumber kebenaran (single source of truth)** untuk membangun dan merevisi course apa pun di bawah series SEJ, LIT, NUM, dan BANG. Tempelkan/unggah dokumen ini di awal setiap sesi pembangunan course baru.

Urutan prioritas saat ada konflik interpretasi:

1. **Instruksi eksplisit terbaru dari Toto Gutomo** untuk course yang sedang dikerjakan.
2. **Aturan emas & aturan keras** di dokumen ini (ditandai **WAJIB**).
3. Standar umum lain dalam dokumen ini (termasuk yang ditandai **SANGAT DISARANKAN**).
4. Reference implementation — contoh, bukan angka baku untuk semua course.

**Aturan Emas (WAJIB):** AI pembangun **tidak boleh menulis/mengubah kode** sebelum Toto Gutomo memberi perintah eksplisit seperti *"Gas kode"*, *"Bangun Kode"*, *"Update Kode"*, atau sejenisnya. Semua usulan didiskusikan dulu.

**Keberlakuan:** keputusan di dokumen ini berlaku untuk **produksi course berikutnya** dan untuk **update course lama yang diminta Toto Gutomo**. Course yang sudah berstatus final candidate tidak diubah otomatis.

Instruksi kerja untuk AI pembangun course:

1. Baca dokumen ini sebelum membuat/mengubah course apa pun.
2. Identifikasi: kode course, series, TP, target perangkat (HP / laptop / IFP), durasi, aktivitas, game utama, jenis asesmen, kebutuhan aktivitas lapangan.
3. Jalankan **Uji Kelayakan TP** (Bagian 3.3) dan diskusikan hasilnya sebelum coding.
4. **Tawarkan pilihan pedagogis di awal** (Pola Penawaran, Bagian 2.6), termasuk tanda ✅/❌ Sinematik Pra-Aktivitas.
5. Bangun **frontend-only, single HTML, mobile-first, dengan tampilan auto-fit dua mode (Genggam & Panggung)**.
6. Jangan mengubah mekanik pembelajaran menjadi sekadar kuis/formulir demi kecepatan.
7. Jangan menyatakan course selesai jika masih ada placeholder, tombol mati, atau fitur wajib yang belum diuji (Bagian 6).
8. Tanpa backend untuk kebutuhan inti — sinkronisasi hasil lewat KHB atau rekap WhatsApp.
9. Serahkan sebagai **satu berkas HTML siap unggah ke Netlify**.

---

## Yang Berubah di Versi Ini (V.4.4 — 18 Oktober 2026)

Changelog lengkap ada di **berkas pendamping** *SCTG_Changelog_dan_Ringkasan.md* (tidak wajib dimuat untuk membangun course).

1. **Footer Baku & Tentang** (B26 baru; A1, A5, Bagian 4 butir 10, Bagian 6 butir 9, QA, Glosarium): setiap course memiliki footer berpola "[judul course] ©[tahun pembuatan] | totogutomo.com"; di bawah footer terdapat **tombol ⓘ Tentang** (bukan identitas pengembang yang selalu tampil). Tombol kedua berada di **Panel Guru**. Kedua tombol membuka **satu modal overlay Tentang** yang sama, berisi identitas dan informasi course; modal tidak mengganggu progres belajar. Tahun = **tahun pembuatan** course, tidak berubah saat update.

Perubahan V.4.3 (10 Langkah Belajar, Menu Langkah ☰, Kunci Senyap, game satu kolom tiga pita, game satu layar di Mode Genggam) tetap berlaku.

**Dampak:** course lama tidak diubah otomatis (lihat Keberlakuan); pasal ini berlaku untuk produksi berikutnya dan update yang diminta Toto Gutomo.

---

# 1. Filosofi & Prinsip Dasar

> SCTG merupakan standar pengembangan **Perjalanan Belajar** digital berbasis **Pembelajaran Mendalam** yang menghasilkan pengalaman belajar yang **bermakna, berkesadaran (mindful), menggembirakan (joyful), dan inklusif**. Pengembangan Perjalanan Belajar mengintegrasikan penguatan literasi, numerasi, dan Koding dan Kecerdasan Artifisial (KKA).

Prinsip utama:

1. **Tenang saat membaca, dramatis saat bermain, sinematik di gerbang penting.**
2. Game memperkuat pembelajaran, bukan sekadar dekorasi.
3. Setiap aksi penting murid menghasilkan respons nyata di layar.
4. **Mobile-first** untuk murid; **Mode Panggung** untuk laptop/IFP di depan kelas. Satu file, dipilih otomatis.
5. Course adalah suplemen pembelajaran tuntas, bukan penguji tiba-tiba yang membebani psikologis murid.
6. Course boleh menjadi LKPD untuk aktivitas di luar layar.
7. **Pemenuhan TP selalu mengalahkan target waktu.** Course yang selesai tepat waktu tetapi gagal membangun penguasaan TP adalah pelanggaran berat. Jangan memangkas kedalaman demi durasi.
8. Setiap course dibangun dari fondasi **CP resmi mata pelajaran (BSKAP terbaru yang berlaku)**, bukan template kosong.

**Target mutu (tradeoff yang diterima):** pedagogi ±9,5/10 dan pengalaman visual-interaktif ±9,8/10 untuk setiap course. Tidak perlu memukau berlebihan, tetapi harus memanjakan mata dan bisa dipertanggungjawabkan secara pedagogis. Konsekuensinya kapasitas produksi turun dari ±30 menjadi **maksimal ±20 course/bulan**, dan token/beban kode per course sedikit naik (terutama karena Sinematik dan pseudo-3D) — **diterima**, karena pengalaman belajar murid meningkat nyata.

---

# 2. Series, Model & Struktur

## 2.1 Series dan Sumber TP

| Series | Sumber TP | Catatan |
|---|---|---|
| **NUM** | Kerangka AKM Numerasi (Bilangan, Aljabar, Geometri & Pengukuran, Data & Ketidakpastian; konteks personal, sosial budaya, saintifik) | Konteks Kalimantan Tengah disarankan |
| **LIT** | Kerangka AKM Literasi Membaca | Saudara NUM |
| **SEJ** (SEJX/SEJXI/SEJXII) | CP Sejarah per kelas (Pemahaman Konsep + Keterampilan Proses Sejarah) | Model pembelajaran dibahas khusus per course |
| **BANG** | Disusun sepenuhnya oleh Toto Gutomo | Tema & mekanik menyesuaikan |
| **TKA** (penguatan & tryout) | Kisi-kisi TKA | **Tetap SCTG V.2** — formal, minim distraksi. Belum direview ulang |

## 2.2 Model Pembelajaran

- **Default PBL** untuk NUM, LIT, BANG, dipetakan ke 10 Langkah Belajar.
- **SEJ:** AI wajib menawarkan **1 model terkuat + 1 alternatif**, masing-masing dengan alasan singkat. Guru mengonfirmasi atau menolak keduanya.

## 2.3 Struktur 10 Langkah Belajar

| # | Langkah | Sintaks PBL | Catatan |
|---|---|---|---|
| 1 | Cover/Login | — | |
| 2 | TP & Situasi (Gerbang Baca TP + centang konfirmasi) | Orientasi masalah | 🎬 Sinematik pengantar TP (disarankan) tampil sebelum layar TP |
| 3 | Aktivasi | Mengorganisasi murid | Gerbang Baca bila ada teks materi |
| 4 | Eksplorasi Bermakna (game utama / lapangan) | Membimbing penyelidikan | |
| 5 | Penalaran & Bukti | Membimbing penyelidikan (lanjutan) | |
| 6 | Produk | Mengembangkan & menyajikan karya | |
| 7 | Final Boss | Menganalisis & mengevaluasi | 🎬 Sinematik pengantar Boss (disarankan) memperlihatkan aturan main |
| 8 | Kesimpulan & Nilai-Nilai Pembelajaran | Menganalisis & mengevaluasi (lanjutan) | Kotak salin dikunci ±5 menit |
| 9 | Refleksi | — | |
| 10 | Sertifikat | — | |

**Alur berurutan:** murid berjalan langkah demi langkah; di akhir tiap langkah tersedia tombol baku **"Lanjut ke [nama langkah berikutnya] →"**, dan perpindahan bebas (mis. membaca ulang) lewat **Menu Langkah ☰** (A4, A5). Mission Map tidak lagi menjadi langkah baku (A4).

Course wajib memiliki **minimal 1 game interaktif nyata** (state, aksi pemain, aturan, feedback, kondisi hasil — bukan kuis berkostum) **plus minimal 1 aktivitas interaktif lain**. Ritme naik-turun: fase membaca tenang, fase bermain dramatis.

## 2.4 Gerbang Baca (menggantikan "Gating Materi opsional")

Bagian yang isinya wajib dibaca murid memakai **Gerbang Baca Berurutan** (aturan lengkap di B3). Berlaku **wajib di semua course**.

## 2.5 Konteks Geo-Sosial

Kontekstualisasi ke alam dan budaya Kalimantan Tengah **disarankan, tidak wajib**.

## 2.6 Pola Penawaran (WAJIB saat "tawarkan langkah belajar")

AI wajib menawarkan di awal, sebelum diminta:

1. **Final Boss: Bandel atau Tuntas?** — dengan alasan singkat (Tuntas = gerbang skor 70 dengan PGK wajib benar minimal 1; lihat B13).
2. **Gerbang Baca:** bagian TP/Materi mana yang dikunci, berapa ikonnya, jumlah kata tiap ikon, dan total waktu kunci. **Laporkan bila total waktu kunci satu langkah melebihi ±3 menit, ada ikon > ±150 kata, atau ikon lebih dari 6 (B3 butir 10)** agar guru memutuskan (B3).
3. Untuk **SEJ**: 1 model pembelajaran terkuat + 1 alternatif.
4. **Hasil Uji Kelayakan TP** (Bagian 3.3).
5. **Game:** cara kontrol (sentuh langsung + kontrol virtual bila ada) dan apakah perlu Level Kecepatan. Bila naskah Jeda Paham sudah ada, **laporkan** penjelasan yang menghasilkan kunci > 30 detik (B6.4).
6. Setiap langkah ditulis **konkret dengan mekaniknya** dan **penanda V.4**, contoh:

```
1. Login — cover tematik "Pasar Terapung Kahayan", nama/kelas/sekolah.
2. Sinematik Pra-Aktivitas SCTG V4 ✅ — karena tema kali ini perjalanan
   rombongan; adegan: pagi berkabut di dermaga, perahu terakhir hampir berangkat…
   (atau ❌ — karena tema kurang naratif, langsung ke layar TP)
3. TP & Situasi — 2 TP, Gerbang Baca TP1–TP2 + centang konfirmasi.
…
6. Eksplorasi — penguatan TP1, game: Susur Sungai (sentuh kiri/kanan + kemudi virtual; level Santai/Sedang/Standar).
…
9. Final Boss (Bandel) — pengantar Sinematik SCTG V4 ✅ memperlihatkan aturan
   main: 10 soal, PG kompleks damage ×2, boss pulih bila salah…
```

Saran sinematik **tidak boleh monoton** — adegan, suasana, dan kejutannya mengikuti tema masing-masing course.

---

# 3. Tujuan Pembelajaran (TP)

## 3.1 Aturan Dasar

- 1–3 TP per course, ditulis eksplisit di layar TP terpisah.
- Centang wajib: **"Saya telah membaca dan memahami tujuan pembelajaran."** Tombol lanjut nonaktif sebelum dicentang, dan centang baru aktif setelah Gerbang Baca TP selesai (B3).
- TP menjadi acuan seluruh materi, aktivitas, dan asesmen.

## 3.2 Aturan Kombinasi TP (1 JP)

- **Maksimal 2 TP konten** dengan level kognitif berdekatan (LOTS+LOTS atau MOTS+MOTS — jangan dicampur jauh),
- **+ 1 TP Keterampilan Proses** yang menaungi instrumen produk akhir tanpa perlu aktivitas baru. TP Keterampilan Proses tidak butuh aktivitas baru — ia memayungi aktivitas yang sudah dibangun untuk TP konten.
- **TP HOTS asli (C5/C6: "mengevaluasi"/"mencipta"/"merumuskan") tidak dicampur dengan TP lain dalam 1 course**, kecuali **diringankan** menjadi "satu keputusan akhir dari data yang sudah dikumpulkan murid di aktivitas lain" (bukan konstruksi baru dari nol). Alasan: HOTS yang diajarkan + dilatih + diuji dengan benar butuh hampir 1 JP sendiri (pengalaman lapangan guru dengan >10 tahun mengajar), dengan scaffolding: contoh terbimbing → latihan dengan umpan balik → tugas mandiri.
- **Course yang didedikasikan penuh untuk 1 TP HOTS itu sah** — dibangun sebagai course lanjutan di atas fondasi fakta dari course sebelumnya. Lebih baik memecah TP HOTS ke course lanjutan daripada menjejalkan scaffolding atau menurunkan level kognitifnya.
- **Hindari kombinasi L-M-H, L-H-KS, dan M-H-KS dengan H penuh (C6 asli) dalam satu course 1 JP** — terbukti tidak realistis.
- Bila TP Pemahaman Konsep tidak cocok dengan aktivitas/waktu, pertimbangkan TP dari elemen **Keterampilan Proses** (mengamati, menanya, mengumpulkan informasi, mengorganisasikan data, menarik kesimpulan, mengomunikasikan temuan), dipetakan eksplisit ke aktivitas yang ada.

## 3.3 Uji Kelayakan TP (WAJIB, sebelum TP dikunci)

AI menjalankan uji ini **sebelum** menawarkan rancangan TP ke Toto Gutomo, bukan menunggu celahnya ditemukan belakangan.

1. **Peta 3 kolom per TP** — aktivitas *mengajar* / *melatih dengan umpan balik* / *menguji*. Satu kolom kosong = TP belum layak.
2. **Instrumen sesuai level kognitif** — jangan uji C6 dengan PG/PG kompleks (itu hanya mengukur pengenalan); pakai tugas tertulis/kinerja.
3. **TP HOTS** mendapat alokasi hampir 1 JP sendiri, atau diringankan (lihat 3.2).
4. **Mekanik game mengikuti struktur logis materi** (lihat B6.3).
5. **Game bertekanan waktu/refleks wajib punya Jeda Paham** (lihat B6.4).

---

# BAGIAN A — Aturan Murid & Antarmuka

## A1. Cover + Login

Halaman pertama bersih, menakjubkan, seperti halaman masuk game. Tidak menampilkan TP, daftar langkah, atau penjelasan teknis. Isi: judul Perjalanan Belajar, visual tematik (pseudo-3D), login murid.

- **Nama** — diketik manual, tanpa default.
- **Kelas** — isian bebas berplaceholder *"contoh: X1"*, tidak auto-terisi.
- **Sekolah** — default **"SMA Negeri 3 Maliku"**, tetap editable.
- Progres lama ditawarkan lewat tombol eksplisit **"Lanjutkan Progres"**, tidak mengisi kolom diam-diam. Autofill login hanya saat EZ.
- Tautan **"🔐 Akses Guru"** di bawah form login (kode diterapkan setelah murid masuk).
- **Footer baku**, tombol **ⓘ Tentang** tepat di bawahnya (membuka modal overlay B26), dan **label versi** kecil di bagian bawah Cover (B26; Bagian 6).

## A2. Feedback Login

Tombol masuk memberi respons visual + opening sound + efek tirai yang benar-benar membuka, transisi singkat.

## A3. Halaman Tujuan Pembelajaran

Tampil setelah login (didahului Sinematik pengantar TP bila course memakainya). TP ditampilkan lewat Gerbang Baca (B3); centang konfirmasi wajib.

## A4. Alur Berurutan, Tombol Lanjut & Menu Langkah

**Alur berurutan.** Langkah dibuka bertahap sesuai urutan 2.3, sehingga arah murid selalu jelas. Di akhir **setiap** langkah ada tombol baku **"Lanjut ke [nama langkah berikutnya] →"** (menyebut nama langkahnya). Langkah selesai tidak otomatis memunculkan modal atau melompat — navigasi di kontrol murid.

**Menu Langkah (☰, header kiri; lihat A5)** — satu-satunya pintu navigasi antar-langkah:

- Panel geser dari kiri berisi daftar langkah bertema (ikon tema, nomor, nama) dengan status ✅ selesai · ▶ giliran · 🔒 terkunci, serta progres. Tampilannya bersih dan fungsional (B6.2).
- Ketuk langkah yang terbuka (selesai atau giliran) untuk pindah; langkah selesai bisa dibuka ulang. Ketuk langkah terkunci memunculkan **toast** singkat (contoh: *"Selesaikan [langkah] terlebih dahulu"*). Fasil/EZ membuka semua langkah (A9).
- Menu menutup setelah murid memilih langkah, atau lewat ✕ / ketuk di luar menu. Di Mode Panggung menu menimpa layar sementara dan tidak menggeser tata letak.
- **Game berjeda saat menu terbuka** agar murid tidak kalah karena membuka menu; jeda berakhir saat menu ditutup.
- Label aksesibel "Menu"; area sentuh mengikuti A5.

**Mission Map (dipensiunkan sebagai langkah baku).** Pada course yang berjalan berurutan, murid tidak memakai peta untuk melanjutkan, sehingga membangunnya pemborosan. Mission Map **hanya** dipakai kembali sebagai langkah opsional pada course **berjalur bebas**, yaitu murid harus memilih sendiri langkah berikutnya. Syaratnya tetap: peta bergambar tematik (SVG), bukan daftar teks; menunjukkan progres, membuka langkah bertahap, menandai langkah selesai, dan bisa dibuka ulang.

## A5. Header & Utilitas Baku (WAJIB — seragam di semua series)

Susunan berikut **dipatok sama** di setiap course LIT/NUM/SEJ/BANG. Tidak boleh ada ikon yang hilang, ditambah, atau ditukar urutannya di bar header.

```
┌───────────────────────────────────────────────────────────────────┐
│ [☰]  Langkah 3/10 · Perjalanan        [🔊] [🔉] [Aa] [◐] [🔐] │
│ ▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░ (progress bar tipis)                       │
└───────────────────────────────────────────────────────────────────┘
   KIRI = navigasi                      KANAN = utilitas (urutan tetap)
```

| Posisi | Ikon | Fungsi | Aturan |
|---|---|---|---|
| Kiri 1 | ☰ | Buka **Menu Langkah** (A4) | Satu-satunya pintu navigasi antar-langkah; label aksesibel "Menu" |
| Kiri 2 | teks | "Langkah n/N · ikon Nama langkah" + nama • kelas murid + progress bar | Di HP sempit kata "Langkah" boleh disembunyikan ("3/9 · 🚐 Perjalanan"); terpotong elipsis, tidak mendorong ikon keluar |
| Kanan 1 | 🔊 / 🔇 | Suara on/off | **Audio bawaan menyala**; status disimpan |
| Kanan 2 | 🔉 / ⏹ | Dengarkan (bacakan konten langkah aktif) | Berhenti otomatis saat langkah berganti |
| Kanan 3 | **Aa** | Ukuran huruf, **satu tombol bersiklus** normal → besar → sangat besar → normal | Menggantikan A−/A+ pada header (A−/A+ kini hanya ada di panel melayang Mode Presentasi, A10d); toast menyebut level; status disimpan |
| Kanan 4 | ◐ | Tema terang/gelap | Status disimpan; default ikut sistem |
| Kanan 5 | 🔐 | **Panel Guru** | Lihat di bawah |

**Panel Guru (🔐)** — satu modal, isi baku:

1. Isian **kode akses** (Fasil/EZ) + tombol Buka.
2. Status mode aktif + tombol **Matikan Fasilitator / Matikan EZ**.
3. Penjelasan singkat fungsi Fasil & EZ.
4. **Mode Presentasi** (hanya tampil bila Fasil/EZ aktif; lihat A10d).
5. **Cek Kode Sertifikat** (hanya tampil bila Fasil/EZ aktif; lihat B18).
6. Tombol **🗑 Reset Identitas (Reset Total)** dengan konfirmasi (hanya saat sudah di dalam aplikasi).
7. **Tombol ⓘ Tentang** (B26): membuka modal overlay informasi course yang sama dengan tombol Tentang pada Cover; bukan menampilkan identitas pengembang secara langsung.
8. **Label versi** kecil di bagian bawah modal.

**Lokasi kontrol lain (baku):**

- **🔁 Ulangi Langkah Belajar** — di langkah Sertifikat (akhir), dengan konfirmasi.
- **🎬 Tonton Ulang** sinematik — di layar aktivitas terkait (TP / Final Boss), **bukan** di header.
- **Ubah level** kecepatan — pada modal Jeda Paham (B6.5).
- **Kirim Refleksi ke Guru** — di langkah Refleksi (B17).
- Unduh/Salin/Kirim WA — di langkah terkait, bukan di header.

**Ukuran:** header ±64 px di Mode Genggam, ≤56 px di Mode Panggung; area sentuh ikon header ≥40 px (Genggam) dan ≥44 px (Panggung). Header selalu fixed di atas.

## A6. Dengarkan 🔉

Membaca konten utama langkah aktif (tanpa tombol/elemen teknis), berhenti saat langkah berubah, bisa dihentikan murid.

## A7. Ukuran Huruf (Aa)

Perubahan terasa, tidak merusak layout di Mode Genggam maupun Mode Panggung. Skala tampilan Mode Presentasi (A10d) terpisah dari Aa dan bekerja di atasnya.

## A8. Audio Feedback

Minimal 9 jenis bunyi (tap, lanjut, benar, salah, unlock, Boss kena, Mission Clear, Boss tumbang, opening), Web Audio API tanpa file eksternal, bisa dimute. Sinematik boleh menambah bunyi tematik (whoosh, gemuruh, denting) dengan cara yang sama. **Kunci Senyap:** bunyi "unlock" dan "lanjut" tidak dipakai sebagai penanda akhir hitung mundur (B24 aturan 5); bunyi "tap" saat murid menekan tombol tetap boleh.

## A9. Mode Khusus

- **Fasil** — default `123456a`. Membuka semua langkah untuk fasilitasi/demonstrasi. Hitung mundur dipercepat ke 2 detik (urutan dan peringatan tetap berlaku). Sinematik dapat dilewati dengan **tombol "⏭ Lewati Animasi"** (bukan otomatis).
- **EZ** — default `ezbgt` (diubah hanya lewat instruksi eksplisit sebelum "Gas kode"). Membuka langkah, **mengisi otomatis semua input termasuk jawaban asesmen**, menandai jawaban benar (mode "belajar bareng" di depan kelas). Hitung mundur 2 detik. Sinematik dapat dilewati dengan tombol "⏭ Lewati Animasi".
- Kode akses disimpan sebagai **hash**, bukan teks polos. **Catatan batas:** karena course berjalan tanpa server, kode dan hash-nya tetap berada di berkas yang dapat dibaca; kode pendek mudah ditebak murid yang membuka kode sumber. Hash hanya menyembunyikan kode dari pandangan sekilas — **pengaman ringan, bukan keamanan sungguhan** (sejalan dengan B18). Fasil/EZ tidak dipakai untuk melindungi data yang benar-benar rahasia.
- **PIN Fasilitator** — opsional per transisi langkah, mati default, hanya atas permintaan eksplisit.
- **Eva** — dihapus permanen.

## A10. Tampilan Auto-Fit: Mode Genggam & Mode Panggung (WAJIB)

Satu berkas, **dua mode yang dipilih otomatis** dari bentuk layar. Murid dan guru tidak perlu memilih, menekan tombol, atau memikirkan ukuran piksel. Bila layar diputar atau jendela diubah ukurannya, tampilan berpindah mode sendiri tanpa muat ulang dan tanpa menghilangkan progres.

| | **Mode Genggam** | **Mode Panggung** |
|---|---|---|
| Untuk | HP dan tablet yang dipegang tegak; HP mendatar | Laptop, PC, IFP/PID, tablet mendatar |
| Dipilih bila | selain syarat Panggung | layar **mendatar** (lebar > tinggi), **lebar ≥ 900 px**, dan **tinggi ≥ 500 px** (angka pasti, bukan perkiraan) |
| Prinsip | isi **100% lebar layar**; scroll wajar untuk langkah membaca/form, **tidak untuk game** | **manfaatkan seluruh layar**; game **satu kolom tiga pita**, satu layar |

Syarat tinggi mencegah HP mendatar (tinggi hanya ±360–430 px) dimasukkan ke Panggung, karena tiga pita tidak muat di sana (lihat ajakan putar di A10f).

**(a) Mode Genggam (HP dan tablet):**

- Lebar aplikasi mengisi **100% lebar layar** (auto-fit), **tanpa margin kosong** di kiri-kanan (hanya jarak dalam ±12–16 px), dengan ukuran huruf dan arena game menyesuaikan lebar layar.
- Target sentuh utama (tombol aksi, opsi jawaban, gerbang) **≥48 px**.
- Scroll atas-bawah wajar dan diterima **untuk langkah membaca, materi, dan form**. **Langkah game wajib muat satu layar tanpa scroll** (A10f): murid tidak boleh mencari soal atau jawaban sambil berpacu waktu.

**(b) Mode Panggung — tata letak desktop yang sesungguhnya:**

- Kerangka lebih lebar dan isi ditata berdampingan bila sesuai; **bukan** sekadar memperbesar tampilan HP.
- **Langkah game (WAJIB muat satu layar, tanpa scroll):** **satu kolom tiga pita** (Soal — Arena — Jawaban/Kontrol; lihat A10f) dalam satu jalur pandang, tanpa menoleh. Soal, arena, dan tombol jawaban terlihat **bersamaan**; murid di belakang kelas tidak bisa ikut "scroll bareng" guru.
- **Langkah materi/form/ringkasan:** konten diperlebar dan huruf diperbesar agar terbaca dari belakang kelas; **scroll seperlunya boleh**.
- **Langkah dengan Gerbang Baca (TP, Materi, Arsip):** memakai **Ruang Baca Panggung** (B3.1) — satu kolom di tengah, panel baca besar, tanpa scroll halaman.
- Header dipadatkan (≤56 px) agar ruang vertikal maksimal. Modal (Jeda Paham, Panel Guru) dan Sinematik tampil lebih besar dan tetap terbaca.
- **Teknik hemat ruang yang dianjurkan:** info yang sudah tampil di arena tidak diulang di pita soal (mis. saldo di HUD); kartu pilihan ringkas; umpan balik dan banner kejadian **melayang di atas arena** (bukan menambah tinggi pita). Pengaman terakhir: bila konten luar biasa panjang, pita soal boleh scroll internal — halaman tidak boleh ikut scroll.

**(c) IFP/PID:**

- Target sentuh **≥56 px**; font mengikuti jarak baca kelas.
- Game dan boss tampil dalam satu layar **tanpa gulir atas-bawah** untuk melihat soal atau jawaban.
- Kontrol game mengikuti B6.6 (sentuh langsung pada arena, bukan hanya tombol).

**(d) Mode Presentasi:**

- Tersedia **hanya untuk Fasil/EZ**, diaktifkan lewat **Panel Guru**.
- Tombol **A−/A+** untuk memperbesar-mengecilkan tampilan berada di **panel kecil melayang** di pojok layar (mis. kanan-bawah), tampil hanya selama Mode Presentasi aktif, dapat diciutkan, tidak menutup arena game (B6.6), dan berukuran sentuh ≥56 px; **bukan** ikon di header (susunan A5 tetap baku). Skala ini terpisah dari tombol **Aa** murid dan bekerja di atasnya. Selain itu ada **efek lingkaran pada titik sentuh/klik** agar terlihat dari belakang kelas.
- Status **tidak disimpan** (menutup atau memuat ulang berkas mengembalikan tampilan normal).
- Selama aktif, baris nama murid di header menampilkan penanda **"Mode Presentasi"** (bukan ikon baru; susunan header A5 tetap baku).

**(e) Matriks uji wajib** sebelum penyerahan (Playwright):

| Kelompok | Ukuran |
|---|---|
| Mode Genggam | 360×560, 390×700, 430×780, 600×900, 768×1024 (tegak; tinggi = tinggi efektif setelah bilah peramban) |
| Mode Panggung | 1024×768 (tablet mendatar), 1366×768 (laptop), 1920×1080 (IFP 100%), ±1280×650 (IFP skala 150% — paling sempit) |
| Ukuran batas (penentu mode) | 899×700 → Genggam; 900×499 → Genggam; 900×500 → Panggung |
| HP mendatar (ajakan putar) | 800×360 → Genggam; langkah game menampilkan ajakan putar ke tegak |

Pada **kedua mode**, semua langkah game wajib lolos **tanpa scroll halaman** di setiap ukuran matriks; pada Mode Panggung, semua **Ruang Baca (B3.1)** juga.

**(f) Bentuk Langkah Game — Satu Kolom, Tiga Pita (WAJIB, Mode Genggam dan Mode Panggung):**

Urutan dari atas ke bawah dalam satu kolom tengah — **satu jalur pandang dan satu jalur tangan**, tanpa menoleh kanan-kiri:

1. **Pita Soal** (atas): soal/petunjuk, selalu terlihat.
2. **Arena** (tengah): canvas game; mengisi seluruh sisa tinggi; objek tidak boleh diregangkan — dunia game digambar menyesuaikan ruang yang tersedia.
3. **Pita Jawaban/Kontrol** (bawah): pilihan jawaban dan/atau kontrol; **hanya ada bila game memakainya**. Pilihan jawaban boleh berjajar satu baris atau grid 2×2 sesuai lebar. Kontrol virtual (B6.6), bila ada, berada di tengah pita ini dan tidak menambah tingginya.

Aturan:

- **Mode Panggung:** kolom tengah selebar yang tinggi layar izinkan (maksimal ±1400 px) dan arena berbentuk **mendatar** (rentang rasio ditetapkan course; contoh 16:9 sampai 3:1). **Tidak ada dua kolom**: tidak ada elemen yang harus dilihat atau disentuh di luar kolom ini. Game berorientasi tegak (mis. objek jatuh) dirancang ulang agar arenanya mendatar.
- **Mode Genggam:** struktur sama dengan proporsi tegak, dirancang untuk HP tegak dengan tinggi efektif ≥ 560 px (setelah bilah peramban). Tinggi arena minimal ±240 px (usulan angka, disetel dari uji lapangan).
- **Pembagian tinggi di layar terpendek** (usulan angka): pita soal ≤ ±20% dan pita jawaban ≤ ±24% dari tinggi tersedia setelah header; arena mendapat sisanya.
- **Soal panjang:** ukuran huruf soal menurun sampai batas keterbacaan minimal (Mode Panggung ≥ 20 px, selaras B3.1 dan A10c; Mode Genggam mengikuti ukuran dasar Aa "normal"); setelahnya hanya pita soal yang scroll di dalam. **Halaman tidak pernah scroll.**
- **HP mendatar (tinggi < 500 px):** tiga pita tidak muat. Langkah game menampilkan ajakan **"Putar HP ke posisi tegak untuk bermain"** yang tidak memblokir; memutar tidak menghilangkan progres.
- **Alasan:** soal, arena, dan jawaban dalam satu jalur menghilangkan menoleh kanan-kiri di IFP dan menghilangkan scroll saat berpacu waktu di HP; struktur yang sama di kedua mode menyederhanakan pembuatan dan pengujian.

---

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

## B7. Soal Pilihan Ganda

Distraktor valid dan masuk akal, panjang opsi setara, struktur paralel, jawaban benar tidak mencolok karena paling panjang. Tidak ada opsi kembar (dicek otomatis). PG dapat dibungkus jadi pengalaman game, tetapi PG biasa tetap sah untuk asesmen formal/Final Boss.

## B8. PG Kompleks

Format **"Pilih semua pernyataan yang benar."** Pernyataan valid, jumlah opsi wajar. Interaksi: gelembung jawaban yang bisa di-toggle + tombol konfirmasi/tembak terpisah (bukan kemudi 3 jalur).

## B9. Kendaraan/Jeep

Gerak natural (bukan step/grid kaku), bagian depan menghadap arah gerak. Kontrol: **sentuh langsung ke arah tujuan** dan/atau tombol arah/joystick virtual di dalam arena — sesuai B6.6, tombol bukan satu-satunya cara.

## B10. Peta

Untuk konsep ruang/wilayah: **geografi nyata**, akurat, mudah dikenali (bukan bentuk abstrak). Pin akurat di semua orientasi.

## B11. Meja Arsip / Adventure Clue (SEJ)

Meja realistis, dokumen lusuh, clue dengan connector line, ditutup centang "Saya telah membaca dan memahami arsip." Teks arsip yang panjang memakai Gerbang Baca (B3); di Mode Panggung memakai Ruang Baca (B3.1).

## B12. Tampilan Multi-Perangkat

Lihat A10. Portrait HP adalah baseline wajib dan harus selalu bisa diselesaikan; Mode Panggung wajib untuk semua course.

## B13. Final Boss

**Mode Bandel** (asesmen sumatif, course berdiri sendiri): tidak ada kondisi kalah; salah → boss pulih; soal diacak ulang bila antrean habis dan boss belum tumbang.

**Mode Tuntas** (formatif, bagian tema besar): **gerbang skor tanpa HP boss** — aturan lengkap pada bagian **Aturan Mode Tuntas** di bawah.

**Cakupan uji:** Final Boss hanya menguji TP yang **valid diuji lewat PG** (umumnya C3–C5: memahami, menerapkan, menganalisis, membandingkan). **TP HOTS asli (C6, "merumuskan"/"mencipta") tidak diuji lewat Boss** — instrumennya ada di langkah Produk (tugas performa/tertulis).

**Bank soal (Bandel dan Tuntas, baku):**

- Bank **12 PG biasa + 4 PG kompleks**; tiap sesi (Bandel) atau tiap paket (Tuntas) mengambil acak **8 + 2**, dikocok jadi satu antrean.
- **Bandel:** antrean habis sebelum boss tumbang → ambil ulang acak dari bank (loop).
- **PG kompleks all-or-nothing**: semua opsi benar harus terpilih tepat (tanpa kurang/lebih) → **damage ×2** (Bandel) atau **20 poin** (Tuntas); benar sebagian = 0 damage / 0 poin.

Standar tampilan **Bandel**: bar berlabel **"FINAL BOSS"**, tombol serang yang jelas, feedback baku *"Jawaban benar, boss kena serangan!"* / *"Jawaban salah, boss memulihkan diri."* Boss tumbang: bendera putih/perayaan, konfeti, fanfare, tombol lanjut ke penutup. Skor/predikat ditampilkan atau tidak: per course (pada **Tuntas** skor paket wajib tampil karena menjadi gerbang).

**Aturan Mode Tuntas** (formatif; gerbang skor, tanpa HP boss, tanpa hukuman atas jawaban salah):

- **Bank sama dengan Bandel** (12 PG biasa + 4 PGK). Satu **paket** = 8 PG + 2 PGK acak, dikocok menjadi satu antrean.
- **Skoring:** PG biasa = **10 poin**; PGK = **20 poin** (all-or-nothing seperti Bandel; benar sebagian = 0). Skor maksimal satu paket 120 poin. **Skor paket = poin ÷ 120 × 100.**
- **Paket dievaluasi setelah selesai penuh** — tidak ada kelulusan atau penghentian di tengah paket. Setelah paket selesai tampil **hasil paket**: skor, "paket ke-n", skor terbaik, dan jarak ke 70.
- **Tuntas bila skor terbaik dari satu paket ≥ 70** (setara ≥ 84 poin). **Skor antarpaket tidak dijumlahkan**; yang dipakai adalah paket terbaik, sehingga mengulang tidak pernah menurunkan nilai dan menebak buta praktis tidak pernah lulus. **Konsekuensi (WAJIB dinyatakan eksplisit):** karena seluruh PG hanya bernilai maksimal 80 poin (66,7), **PGK wajib benar minimal 1** — lulus membutuhkan minimal 1 PGK benar dan 7 PG benar, atau 2 PGK benar dan minimal 5 PG benar.
- **Loop:** bila belum tuntas, satu tombol "Paket berikutnya" membuka paket acak baru. Paket berikutnya **mengutamakan soal yang belum pernah muncul atau sebelumnya salah**; bila bank habis, acak bebas. Tidak ada jalur keluar tanpa tuntas (tegas, tetapi tanpa hukuman).
- **Setelah tuntas:** tombol utama "Lanjut" ke penutup; tombol kedua "Ulangi untuk skor lebih tinggi" (sukarela, tidak dibatasi; nilai tersimpan selalu paket terbaik).
- **Saran baca ulang materi:** bila sampai paket ke-3 belum tuntas (diulang di paket ke-6, ke-9, dan seterusnya) tampil saran dengan dua tombol: "Buka Menu untuk baca ulang" (☰, A4) dan "Coba paket lagi". Ini **saran, bukan paksaan**; kemajuan dan skor terbaik tetap tersimpan.
- **Tampilan:** boss tetap hadir sebagai elemen visual; bar berlabel **"SKOR MENUJU 70"** menggantikan bar HP dan terisi mengikuti skor terbaik. Feedback baku: *"Jawaban benar."* / *"Jawaban belum tepat."* (bukan "boss kena serangan"/"memulihkan diri"). Saat tuntas: perayaan (konfeti, fanfare) dan tombol lanjut ke penutup.
- **Fasil/EZ** tetap berlaku (EZ menandai jawaban benar); kunci waktu apa pun mengikuti B24.

**Sinematik pengantar Boss** (B22) memuat aturan main bila dipakai (Bandel maupun Tuntas).

## B14. Kesimpulan & Nilai-Nilai Pembelajaran — WAJIB semua series

- 2–3 paragraf siap disalin ke buku catatan (tombol salin). Nilai lahir dari materi, bukan moral generik. Ditutup **satu centang gabungan**: *"Saya telah menyalin kesimpulan dan nilai-nilai pembelajaran."*
- Kotak centang **dikunci ±5 menit** (durasi menyesuaikan panjang catatan, batas atas 5 menit, lihat Tabel Konstanta Waktu B24; hitung mundur terlihat murid) agar murid benar-benar sempat menyalin; saat habis, kotak menjadi aktif secara senyap (B24 aturan 5). **Fasil/EZ:** dipercepat ke 2 detik.
- **Kalimat pedoman:** **"1 pertemuan = 1 halaman catatan."** Kata "course" maupun "langkah belajar" tidak dipakai pada kalimat tersebut di UI murid.

## B15. Nilai-Nilai Pembelajaran

Lihat B14 (satu langkah dengan Kesimpulan).

## B16. Aktivitas Lapangan → Prompt AI → Produk

Opsional. Jenis produk seragam dalam satu course. Course merangkai data lapangan jadi **prompt siap salin**; murid memakai AI pilihannya sendiri. **Course tidak pernah memanggil API AI.**

## B17. Refleksi

1. **Pulse-check** ikon (1–2 pertanyaan, tanpa benar-salah).
2. **Uraian terpandu 1–3 kalimat** dengan chip kalimat pemandu; bank kalimat **berbeda per course** (disimpan di data course, bukan hardcode). Tolak placeholder "…" yang belum dilengkapi.
3. **Kirim Refleksi ke Guru** (opsional, tidak wajib, **tidak mengunci langkah berikutnya**): murid mengisi nomor WhatsApp guru (dirapikan otomatis 0xxx → 62xxx) dan pesan dikirim lewat tautan `wa.me` dari akun WhatsApp milik murid sendiri — tanpa server/backend. Nomor guru cukup diisi **sekali**, lalu dipakai juga untuk rekap di langkah Sertifikat.
4. Ikon/emoji pada pulse-check memakai animasi ringan (B25).

## B18. Sertifikat

- **PDF saja**, dibangun **manual tanpa pustaka eksternal**, feedback dua tahap (*"PDF sedang disiapkan…"* → *"Unduhan dimulai."*). Unduhan mengikuti B23.
- Isi wajib: nama, kelas, sekolah, judul, **TP**, **tanggal penyelesaian**, dan **kode verifikasi**. Skor/predikat disembunyikan default. Pada Final Boss Tuntas, skor paket terbaik dan jumlah paket yang ditempuh boleh dimuat di rekap guru (B19); sertifikat tetap menyembunyikan skor.
- **Kode verifikasi:** dibentuk dari data murid dan tanggal (nama, kelas, sekolah, kode course, tanggal `YYYYMMDD`) dengan fungsi hash non-kriptografis, berformat **`KODECOURSE-XXXX-XXXX`**.
- **Cek Kode Sertifikat** (Panel Guru, tersedia saat Fasil/EZ aktif): guru mengisi ulang nama, kelas, sekolah, dan tanggal dari sertifikat murid; kode dihitung ulang dan dicocokkan dengan yang tertera. Karena tanpa server, ini penangkal pemalsuan ringan (bukan keamanan kriptografis) dan tetap dipadukan dengan presensi.
- Model pembelajaran tuntas: hadir + selesai = berhak sertifikat; guru mencocokkan kehadiran manual sebelum menghormati penukaran dengan "bebas ulangan" (kebijakan sekolah, bukan mekanisme teknis).

**Checklist kualitas sebelum kirim ke KHB** (murid mencentang sendiri; isi disesuaikan mapel; ditampilkan di langkah Produk bila relevan):

- *Contoh SEJ:* memuat fakta sejarah/materi · bahasa mudah dimengerti · desain menarik.
- *Contoh NUM:* nama & kelas sudah benar · angka memakai data sendiri · alasan minimal 1 kalimat utuh · berkas/teks sudah diunduh/disalin.

## B19. Integrasi KHB & Rekap

- Tautan KHB **tidak ditanam** di kode; cukup instruksi lisan guru.
- **Rekap WhatsApp**: nomor guru diketik manual (dirapikan ke `62…`), membuka WA dengan rekap siap kirim + tombol **"Salin Rekap"**.

## B20. Ulangi & Reset

- **🔁 Ulangi Langkah Belajar** (langkah Sertifikat): hapus progres (termasuk kemajuan Gerbang Baca), identitas tetap, flag sinematik direset. Preferensi suara/font/tema boleh tetap.
- **🗑 Reset Identitas** (Panel Guru 🔐): hapus identitas + seluruh progres. Dua kontrol **terpisah**.

## B21. Terminologi

Gunakan **"Langkah Belajar"** dan **"Murid"**. Kata "course"/"SCTG" tidak muncul di UI murid. Hindari istilah teknis (bank soal, randomisasi, engine).

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

## B26. Footer Baku & Tentang (WAJIB — seragam di semua series)

Identitas pembuat tampil seragam di setiap course, sama seperti Header Baku (A5).

1. **Pola footer:** `[judul course] ©[tahun pembuatan] | totogutomo.com`, contoh: "Bungkus Sakti ©2026 | totogutomo.com". Judul course sama dengan judul Perjalanan Belajar di Cover.
2. **Tahun = tahun pembuatan** course (tahun saat course pertama dibangun). Ditulis tetap di data course; tidak memakai tahun berjalan dan tidak berganti saat update atau revisi.
3. **Tombol ⓘ Tentang:** ditempatkan tepat di bawah footer pada Cover, dengan tipografi kecil yang konsisten dengan footer namun tetap jelas sebagai tombol interaktif; kontras teks ≥ 4,5:1 pada tema terang dan gelap serta area sentuh yang layak di HP.
4. **Dua pintu, satu modal:** tombol ⓘ Tentang di Cover dan tombol ⓘ Tentang di Panel Guru (A5 butir 7) membuka **modal overlay yang sama**, bukan dua salinan konten dan bukan navigasi ke halaman terpisah. Akses dari Cover tidak membutuhkan login atau kode guru.
5. **Isi modal Tentang (WAJIB, urutan baku):** (a) judul course; (b) kode seri/course, misalnya NUM10; (c) deskripsi singkat yang spesifik terhadap materi dan tujuan course; (d) **Teknologi yang Digunakan**, hanya teknologi yang benar-benar digunakan; (e) **Lisensi**, berisi hak cipta, ketentuan pemakaian, dan atribusi aset pihak ketiga sesuai lisensi aktual—jangan mengklaim lisensi terbuka tanpa dasar; (f) **Pengembang**: "Toto Gutomo, S.Pd., Gr., M.Pd." pada baris pertama dan "Guru SMA Negeri 3 Maliku" pada baris berikutnya; (g) tagline **< ❤️ / > Ngoding pakai Vibe, Ngajar pakai Hati**; (h) tombol/tautan aktif **totogutomo.com** menuju https://totogutomo.com. Data judul, kode, deskripsi, teknologi, dan lisensi harus sesuai course masing-masing, tidak menyalin contoh sebagai fakta.
6. **Perilaku modal:** tampil di atas layar saat ini tanpa mengubah langkah belajar, identitas, mode guru, atau progres; dapat ditutup melalui tombol X yang jelas, tombol Kembali Android, dan Escape pada perangkat berkeyboard. Setelah ditutup, fokus kembali ke tombol pembuka dan layar sebelumnya tetap utuh. Modal dapat digulir pada layar kecil, memiliki fokus keyboard dan label aksesibel, serta tidak menutup kontrol penting secara permanen.
7. **Tidak mengganggu tata letak:** footer dan tombol Tentang hanya berada pada Cover; di Panel Guru hanya tombol Tentang. Keduanya tidak ditampilkan pada langkah game dan tidak menambah ikon header (A5 tetap baku). Label versi tetap kecil di bagian bawah Cover dan Panel Guru.
7. Berlaku untuk produksi berikutnya dan update yang diminta Toto Gutomo; course lama tidak diubah otomatis (Keberlakuan).

---

# 4. Uji Kelayakan Visual & Mekanik (WAJIB, sebelum delivery)

Cara memeriksa tiap butir mengikuti **verifikasi berjenjang** (Bagian 6 butir 5–6): butir yang terukur diperiksa dengan angka, sebagian dengan sampel gambar, dan butir yang bersifat penilaian rasa dinilai Toto Gutomo di perangkat asli.

1. Tidak ada langkah game berupa grid tombol DOM polos warna solid — semua canvas dengan pseudo-3D, easing, audio, perayaan.
2. Tema visual konsisten dari cover sampai sertifikat.
3. **Menu Langkah** bersih dan fungsional (A4, A5); bila Mission Map dipakai (course berjalur bebas), ia berupa peta bergambar tematik.
4. **Palet warna, tipografi, dan komponen UI (tombol, kartu, modal) konsisten satu sistem visual di seluruh course, disesuaikan dark/light bila relevan.**
5. **Header sesuai A5** (ikon lengkap, urutan benar, Panel Guru lengkap).
6. **Tampilan auto-fit sesuai A10** (Genggam 100% lebar dan langkah game satu layar; Panggung: langkah game satu kolom tiga pita, satu layar).
7. **Game dapat dimainkan dengan sentuh langsung** (B6.6).
8. **Gerbang Baca** lengkap sesuai B3, dan di Mode Panggung memakai **Ruang Baca sesuai B3.1** (tanpa scroll halaman); ikon tidak menutup sendiri (B3 butir 2a), hitung mundur berjeda (B3 butir 2b), maksimal 6 ikon, akhir hitung mundur senyap (B24 aturan 5).
9. Bila Sinematik dipakai: anatomi B22 lengkap, sekali per sesi, ↻ Ulang, tonton ulang, tombol lewati di Fasil/EZ.
10. **Footer baku dan Tentang** sesuai B26: pola benar, tahun = tahun pembuatan, tombol Tentang tersedia di bawah footer Cover dan di Panel Guru, keduanya membuka satu modal overlay B26 berisi seluruh informasi wajib, tidak mengubah progres dan tidak muncul di langkah game.

---

# 5. Standar Teknis

- **Single HTML** (HTML+CSS+JS+aset tertanam), tanpa CDN/eksternal (kecuali font sistem), tanpa backend inti.
- **Deployment:** Netlify; performa HP kelas menengah.
- **Penyimpanan:** localStorage untuk progres, kemajuan Gerbang Baca, suara, font, tema, flag sinematik. Progres lama tidak diam-diam mengganggu murid baru; EZ tidak bocor ke penggunaan normal. Mode Presentasi **tidak** disimpan.
- Kode akses di-hash.
- Canvas: `devicePixelRatio`-aware, loop `requestAnimationFrame` hanya menggambar langkah aktif.
- Backend/GAS hanya bila benar-benar diperlukan untuk sinkronisasi lintas perangkat — default-nya tidak.

---

# 6. Proses Build WAJIB

1. Uji Kelayakan TP → didiskusikan dengan Toto Gutomo **sebelum** kode ditulis.
2. Pola Penawaran langkah (dengan ✅/❌ Sinematik) → disetujui.
3. **Aturan Emas:** kode baru ditulis setelah "Gas kode".
4. **Uji jalan otomatis end-to-end** (Playwright atau setara) seluruh langkah: jalur murid normal (termasuk jawaban salah), EZ, Fasil, reset identitas, ulangi langkah belajar, muat ulang/lanjutkan progres, unduhan PDF/gambar; **tanpa error JavaScript**.
5. **Ukur, jangan hanya lihat.** Jalankan pada **seluruh matriks ukuran A10(e)** (termasuk ukuran batas) — bukan hanya satu ukuran HP — dan **periksa dengan angka**, tanpa perlu meninjau gambar: (a) langkah game dan semua Ruang Baca Mode Panggung tidak butuh scroll halaman; (b) tidak ada teks meluber atau terpotong; (c) tidak ada elemen yang menutupi arena atau tombol (uji ketuk pada titik tombol berhasil); (d) kontras teks terang dan gelap memenuhi rasio wajar (≥ 4,5:1 untuk teks biasa); (e) kanvas game tidak kosong. Tangkapan layar disimpan hanya bila dibutuhkan pada butir 6.
6. **Tinjauan gambar berjenjang (hemat token)** terhadap Bagian 3.3 dan Bagian 4:
   - **Tahap A (berlaku):** AI meninjau **sampel kecil** tangkapan layar, sekitar 4–6 gambar: cover, satu langkah game Mode Panggung di ±1280×650, satu Ruang Baca Mode Panggung, Final Boss, dan satu langkah Mode Genggam tema gelap. Bukan seluruh langkah kunci × tiga tampilan.
   - **Tahap B (nol gambar) — RENCANA, BELUM BERLAKU:** dapat diaktifkan Toto Gutomo bila (i) kerangka bersama (Engine), bila kelak ada, sudah lolos verifikasi bergambar **lengkap satu kali**, dan (ii) tiga course berturut-turut tidak memiliki cacat tampilan yang lolos ke Toto Gutomo. Pada Tahap B, course hanya diukur dengan angka (butir 5).
   - **Kembali ke Tahap A** bila kerangka bersama berubah, Toto Gutomo melaporkan cacat tampilan, atau pengukuran angka memberi tanda peringatan.
   - Butir Bagian 4 yang bersifat penilaian rasa (mis. tema konsisten, mutu pseudo-3D, keseimbangan tata letak) **dinilai Toto Gutomo di perangkat asli**. Di laporan serah, AI menyatakan tiap butir Bagian 3.3 dan Bagian 4 sebagai **"diukur"**, **"disampel"**, atau **"diserahkan ke penilaian Toto Gutomo"**.
7. **Bersihkan kode uji/debug** (mis. pengait `window.__…`) dari berkas yang diserahkan, lalu periksa ulang sintaks setelah penghapusan.
8. **Fitur bergantung perilaku peramban seluler** (unduhan berkas, bagikan, WhatsApp) diberi jalur cadangan, dan dilaporkan sebagai **"belum teruji di perangkat asli"** bila tidak dapat diuji langsung.
9. **Label versi pada UI** (footer Cover dan Panel Guru) diperbarui mengikuti versi SCTG yang dipakai, ditulis kecil dengan format "Standar [versi SCTG yang dipakai]", mis. "Standar 4.4" (angka versi tidak ditulis mati di pasal ini agar tidak usang tiap rilis; kata "SCTG" tidak dipakai di UI murid, B21). **Footer baku dan Tentang (B26)** diperiksa pada langkah yang sama.
10. **Perbaiki dulu, baru kirim** — jangan menyerahkan yang "mungkin benar".
11. Serahkan sebagai **satu berkas HTML** siap unggah ke Netlify.
12. **Catatan revisi untuk meninjau aturan uji.** Setiap revisi pada course dicatat: nomor, kategori penyebab (1 aturan hilang / 2 aturan ada tetapi tidak dipatuhi / 3 masalah baru dari uji lapangan), pasal terkait, dan **ditemukan oleh** (uji otomatis AI atau Toto Gutomo di lapangan). Setelah course pertama, laporan penggunaan sesi dipakai untuk mengukur porsi token tahap verifikasi. Data ini menjadi dasar menambah atau memangkas aturan uji, bukan asumsi.

---

# 7. QA Sebelum Delivery (checklist)

- [ ] Semua langkah bisa diselesaikan tanpa jalur buntu; nol error JavaScript.
- [ ] Game utama playable (sentuh langsung + kontrol virtual bila ada); minimal 1 aktivitas interaktif lain.
- [ ] Jeda Paham berfungsi (non-skippable, hitung mundur, cepat di Fasil/EZ); Level Kecepatan bila game bertekanan waktu.
- [ ] Gerbang Baca: berurutan, durasi berbasis jumlah kata, toast peringatan, ceklis akhir terkunci, kemajuan tersimpan, cepat di Fasil/EZ; **ikon tidak menutup sendiri** saat hitung mundur habis (tunggu hitungan habis + beberapa detik: kartu tetap terbuka, tombol "Lanjut ke … →" berubah dari nonaktif ke aktif); hitung mundur **berjeda** saat layar tersembunyi/kartu ditutup dan dilanjutkan dari sisa; maksimal 6 ikon per gerbang.
- [ ] **Ruang Baca Panggung (B3.1)**: daftar satu kolom di tengah → bergeser ke kanan saat baca; panel baca ≥18 px; tombol "Lanjut →"/"Selesai Membaca"; tanpa scroll halaman di semua ukuran A10(e); menu scroll internal dengan centang menempel bila perlu; Genggam tetap accordion.
- [ ] **Kunci Senyap** (B24 aturan 5): saat hitungan habis tidak ada suara, animasi, toast, scroll, atau fokus otomatis (uji: tidak ada pemanggilan fungsi suara); tombol berubah dari abu-abu ke warna aksen; rasio kontras lolos (tombol aktif ≥ 3:1, teks ≥ 4,5:1, selisih kecerahan aktif–nonaktif jelas) di tema terang dan gelap.
- [ ] Final Boss mode sesuai kesepakatan; hanya menguji TP yang sah lewat PG; bank 12+4 → 8+2 → loop; tidak ada opsi kembar. **Bandel:** PGK damage ×2 all-or-nothing. **Tuntas:** PG 10 dan PGK 20 (maks 120), skor paket = poin ÷ 120 × 100, tuntas bila paket terbaik ≥ 70 (PGK wajib benar minimal 1), paket dievaluasi setelah selesai penuh, paket berikutnya mengutamakan soal belum muncul/salah, opsi Lanjut/Ulangi setelah tuntas, saran baca ulang materi di paket ke-3, 6, 9…, bar "SKOR MENUJU 70" (tanpa HP boss).
- [ ] **Menu Langkah (☰)**: daftar 10 langkah, status ✅ ▶ 🔒, langkah terkunci → toast, langkah selesai bisa dibuka ulang, menutup setelah memilih, game berjeda saat menu terbuka; tombol akhir tiap langkah "Lanjut ke [nama langkah] →".
- [ ] Login sesuai A1; "Lanjutkan Progres" eksplisit.
- [ ] **Footer baku & Tentang (B26)**: "[judul] ©[tahun pembuatan] | totogutomo.com" di Cover; tombol ⓘ Tentang tepat di bawah footer dan tombol kedua di Panel Guru; keduanya membuka modal overlay yang sama dengan judul, kode, deskripsi, teknologi aktual, lisensi/atribusi aktual, identitas lengkap pengembang, tagline, dan tautan aktif totogutomo.com; tutup X/Kembali Android/Escape berfungsi, fokus kembali, progres tetap, dapat digulir di HP, kontras ≥ 4,5:1; tidak ada tombol Tentang di langkah game.
- [ ] **Header A5**: ☰ | 🔊 🔉 Aa ◐ 🔐 lengkap & berurutan; Panel Guru berisi kode, status mode, Mode Presentasi, Cek Kode Sertifikat, Reset Identitas, Tentang, label versi.
- [ ] **Auto-fit**: Genggam 100% lebar dan **langkah game satu layar tanpa scroll** di 360×560, 390×700, 430×780, 600×900, 768×1024; Panggung tanpa scroll untuk langkah game (satu kolom tiga pita) di 1024×768, 1366×768, 1920×1080, ±1280×650; HP mendatar menampilkan ajakan putar di langkah game; ukuran batas (899×700, 900×499, 900×500) memilih mode yang benar.
- [ ] Mode Presentasi: hanya Fasil/EZ, tidak tersimpan, penanda tampil, efek lingkaran sentuh, A−/A+ di panel melayang (bukan di header).
- [ ] **Sinematik** (bila dipakai): sekali otomatis, ↻ Ulang, tonton ulang bervariasi, CTA terkunci, ⏭ Lewati Animasi di Fasil/EZ, flag reset saat Ulangi.
- [ ] Kesimpulan terkunci ±5 menit (2 detik di Fasil/EZ); kalimat "1 pertemuan = 1 halaman catatan"; Refleksi dua lapis + Kirim Refleksi opsional.
- [ ] Sertifikat PDF lengkap (TP, tanggal, kode `KODECOURSE-XXXX-XXXX`), feedback dua tahap, jalur unduhan cadangan; Cek Kode Sertifikat berfungsi; rekap WA + Salin Rekap.
- [ ] Ulangi dan Reset Identitas terpisah, berfungsi.
- [ ] Kode debug sudah dibersihkan; sintaks diperiksa; label versi sesuai versi SCTG yang dipakai.
- [ ] Verifikasi berjenjang (Bagian 6): ukuran diukur dengan angka, sampel gambar Tahap A dijalankan, laporan serah menyatakan tiap butir Bagian 3.3 dan Bagian 4 sebagai diukur / disampel / diserahkan ke penilaian Toto Gutomo; catatan revisi terisi.
- [ ] Konten akademik & jawaban diperiksa.

---

# 8. Reference Implementation

- **NUM07 v4 — *Bertahan dengan Anggaran Terbatas*** (reference series NUM): Ketok Cepat (canvas lapak pasar + Jeda Paham "struk"), Perjalanan Bergerbang angkot ke Bukit Tangkiling (Jeda Paham "buku bendahara"), Rantai Sebab-Akibat dari data murid sendiri, Kartu Rencana, Final Boss Bandel "Si Boros" (12+4 → 8+2), Sinematik pengantar TP & Boss, Mode Panggung, Header A5.
  - *Catatan:* NUM07 v4 berstatus **final candidate** dan dibangun sebelum pasal B3 (Gerbang Baca), B6.5, B6.6, B23–B25, ambang auto-fit 900×500 px, dan tambahan Panel Guru ditetapkan (NUM07 v4 memakai ambang 1000 px). Ia baru disesuaikan bila Toto Gutomo meminta update. Course sampel juga memakai 11 langkah dengan Mission Map dan game berkolom dua (sebelum V.4.3), serta belum memuat Footer Baku dan Tentang (V.4.4).
- **SEJXI07** — *Bayang-Bayang Kedatangan Jepang* (V.3, 9,2/10): fondasi jangan diganti, game harus hidup lewat mekanik bukan skin, peta harus nyata, drag-and-drop berisiko, QA wajib.

---

# 9. Glosarium

| Istilah | Arti |
|---|---|
| **CP** | Capaian Pembelajaran |
| **TP** | Tujuan Pembelajaran |
| **ATP** | Alur Tujuan Pembelajaran |
| **KS** | Keterampilan (Proses/Sejarah, dst., sesuai elemen CP mapel) |
| **LOTS / MOTS / HOTS** | Lower / Middle / Higher Order Thinking Skills |
| **KHB** | Kelas Digital Huma Betang — platform sekolah tempat hasil kerja murid dikumpulkan |
| **SCTG** | Standar Course Toto Gutomo |
| **Langkah Belajar** | Satu tahap dalam Perjalanan Belajar (istilah UI murid) |
| **Mode Genggam** | Tampilan otomatis untuk HP/tablet tegak: isi 100% lebar layar; langkah game tetap satu layar |
| **Mode Panggung** | Tampilan otomatis untuk layar lebar mendatar (laptop/IFP): game satu layar, satu kolom tiga pita |
| **Mode Presentasi** | Fitur Fasil/EZ di Panel Guru: perbesar tampilan lewat panel melayang (bukan header) + efek lingkaran sentuh, tidak disimpan |
| **Sentuh Langsung** | Bermain dengan mengetuk/menggeser arena langsung, bukan hanya lewat tombol virtual |
| **Gerbang Baca** | Bagian bacaan tertutup berikon bernomor; dibuka berurutan dengan hitung mundur berbasis jumlah kata (waktu minimum; ikon tidak menutup sendiri) |
| **Ruang Baca** | Tampilan Gerbang Baca di Mode Panggung: daftar satu kolom di tengah yang bergeser ke kanan menjadi menu saat panel baca besar dibuka (B3.1) |
| **Jeda Paham** | Modal penjelasan wajib dengan hitung mundur setelah jawaban di game bertekanan waktu |
| **Level Kecepatan** | Pilihan Santai / Sedang / Standar untuk game bertekanan waktu |
| **Jam Kunci Serentak** | Satu mesin hitung mundur untuk semua kunci waktu |
| **Konstanta Waktu** | Tabel rumus waktu baca dan kunci waktu di B24 (satu-satunya sumber angka waktu) |
| **Kunci Senyap** | Aturan B24: akhir hitung mundur tanpa suara/animasi/toast; hanya tombol yang sudah ada berubah dari abu-abu ke warna aksen |
| **Menu Langkah** | Tombol ☰ di header kiri; panel daftar langkah bertema (✅ ▶ 🔒) untuk berpindah langkah; pengganti 🗺️ |
| **Tiga Pita** | Bentuk langkah game: Pita Soal (atas), Arena (tengah), Pita Jawaban/Kontrol (bawah), satu kolom, satu layar (A10f) |
| **Sinematik Pra-Aktivitas** | Sekuens beat teks + suara + latar tematik sebelum gerbang penting |
| **Beat** | Satu potong teks/adegan dalam sinematik |
| **CTA terkunci** | Layar akhir sinematik; tombol lanjut aktif setelah beat terakhir |
| **Pseudo-3D / Ilusi 3D** | Kesan 3D dari gradasi, cahaya, bayangan, dan kilau kaca pada Canvas 2D/CSS |
| **Footer Baku** | Baris identitas "[judul] ©[tahun pembuatan] \| totogutomo.com" di Cover (B26) |
| **Tentang** | Tombol pada Cover (di bawah footer) dan Panel Guru membuka satu modal overlay informasi course lengkap, identitas pengembang, tagline, lisensi, dan tautan totogutomo.com (B26) |
| **Panel Guru** | Modal 🔐 berisi kode Fasil/EZ, status mode, Mode Presentasi, Cek Kode Sertifikat, Reset Identitas, Tentang |
| **Bandel / Tuntas** | Mode Final Boss sumatif (tanpa kalah, boss pulih bila salah, loop) / formatif (gerbang skor 70 per paket, tanpa HP boss, PGK wajib benar minimal 1) |
| **Paket (Final Boss)** | Satu kumpulan 8 PG + 2 PGK acak; pada Tuntas dinilai setelah selesai penuh dan skor terbaik yang dipakai |
| **Uji Kelayakan TP** | Tes 5 poin sebelum TP dikunci |
| **Uji Kelayakan Visual & Mekanik** | Checklist visual/antarmuka sebelum delivery |
| **Verifikasi Berjenjang** | Cara memeriksa course: ukuran diukur dengan angka, gambar hanya sampel kecil (Tahap A); Tahap B (nol gambar) adalah rencana yang belum berlaku |
| **IFP / PID** | Interactive Flat Panel / papan interaktif di depan kelas |

---

> **SCTG V.4.4** menyatukan kerangka Pembelajaran Mendalam, 10 Langkah Belajar, uji kelayakan TP dan visual, dengan lompatan pengalaman: **tampilan auto-fit** yang membuat game nyaman di genggaman murid sekaligus di panggung IFP, **sentuh langsung** agar tak ada murid bergantung pada tombol virtual, **Gerbang Baca** (berbasis jumlah kata, dengan **Ruang Baca** di layar lebar) agar teks benar-benar terbaca, **Sinematik Pra-Aktivitas** agar gerbang penting terasa seperti kejutan yang dinanti, **Header Baku**, serta **Footer Baku dan Tentang** agar murid merasa di rumah yang sama di setiap Langkah Belajar — tanpa mengorbankan kedalaman TP.
