<!-- Disalin tanpa perubahan dari SCTG_V4.4.md, baris 671,742 -->

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

