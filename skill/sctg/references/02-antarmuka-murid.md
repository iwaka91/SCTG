<!-- Disalin tanpa perubahan dari SCTG_V4.4.md, baris 174,340 -->

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
