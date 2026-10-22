---
name: sctg
description: Standar Course Toto Gutomo (SCTG) V.4.4 untuk membangun, merevisi, dan memeriksa course "Perjalanan Belajar" digital (satu berkas HTML) series SEJ, LIT, NUM, dan BANG. Gunakan saat user menyebut SCTG, course, Perjalanan Belajar, Uji Kelayakan TP, Gerbang Baca, Final Boss, Sertifikat, Footer Baku atau Tentang, atau kode course seperti NUM07 dan LIT10. Baca berkas ini dulu; dokumen utuh SCTG_V4.4.md hanya bila diminta atau dibutuhkan. Series TKA memakai SCTG V.2, bukan skill ini.
---

# SCTG V.4.4 — Skill (baca ini dulu)

**Sinkron dengan:** `SCTG_V4.4.md` (berlaku 18 Oktober 2026), disinkronkan 22 Oktober 2026.
Berkas di `references/` adalah salinan per bagian dari `SCTG_V4.4.md` **tanpa perubahan kalimat**. Bila terjadi beda, `SCTG_V4.4.md` di root repo yang berlaku. Setiap ada versi SCTG baru, folder skill ini diperbarui bersamaan dan tanggal sinkron di atas diganti.

## Aturan pakai skill

1. Mulai dari berkas ini. Baca **hanya** berkas `references/` yang sesuai pekerjaan (lihat peta di bawah), bukan semuanya.
2. Baca `SCTG_V4.4.md` **utuh** hanya bila:
   - Toto Gutomo memintanya, atau
   - membangun course penuh dari nol, atau
   - ada pasal yang bertentangan atau meragukan antarberkas.
3. Update kecil cukup membaca berkas pasal yang disentuh, ditambah `08-uji-dan-qa.md` saat tahap uji dan serah.

## Peta berkas: pekerjaan → berkas yang dibaca

| Pekerjaan | Berkas di `references/` |
|---|---|
| Diskusi awal: series, TP, Uji Kelayakan TP, Pola Penawaran | `01-fondasi-dan-tp.md` (Bagian 1–3) |
| Cover, login, header, tombol, ukuran huruf, auto-fit (A1–A10) | `02-antarmuka-murid.md` |
| Struktur, Gerbang Baca, Ruang Baca Panggung (B1–B5) | `03-aturan-course-dasar.md` |
| Game: mekanik, visual, Jeda Paham, kecepatan, kontrol (B6) | `04-game.md` |
| Soal, peta, Final Boss, kesimpulan, refleksi, sertifikat, KHB, ulangi, terminologi (B7–B21) | `05-asesmen-dan-penutup.md` |
| Sinematik, unduhan, Jam Kunci Serentak, emoji bergerak (B22–B25) | `06-sinematik-dan-fitur-tambahan.md` |
| Footer Baku dan modal Tentang (B26) | `07-footer-tentang.md` |
| Uji kelayakan visual, standar teknis, proses build, checklist QA (Bagian 4–7) | `08-uji-dan-qa.md` |
| Reference implementation dan glosarium (Bagian 8–9) | `09-referensi-glosarium.md` |
| Riwayat versi dan apa yang berubah di V.4.4 | `00-versi-dan-perubahan.md` |

Pasal yang disebut silang (mis. "Bagian 3.3", "B26", "A10(e)") dicari lewat peta di atas.

## Cara pakai dan aturan emas (salinan dari SCTG_V4.4.md, tanpa perubahan)

> Catatan: anjuran "tempelkan/unggah dokumen ini di awal setiap sesi" di bawah **digantikan** oleh Aturan pakai skill di atas (skill dulu, dokumen utuh hanya bila diminta atau dibutuhkan). Isi lainnya tetap berlaku.

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
