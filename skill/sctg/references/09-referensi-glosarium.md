<!-- Disalin tanpa perubahan dari SCTG_V4.4.md, baris 745,794 -->

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
