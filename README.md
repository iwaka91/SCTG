# SCTG — Standar Course Toto Gutomo

**Versi terkini: V.4.4** (berlaku 18 Oktober 2026)
Disusun oleh Toto Gutomo, Guru SMA Negeri 3 Maliku, Kalimantan Tengah, bersama Claude.

SCTG adalah standar pembuatan **Perjalanan Belajar** digital berbasis Pembelajaran Mendalam: bermakna, berkesadaran, menggembirakan, dan inklusif. Standar ini dipakai untuk membangun course series **SEJ, LIT, NUM, dan BANG** (series TKA tetap memakai SCTG V.2).

## Isi repo

| Berkas | Keterangan |
|---|---|
| [`SCTG_V4.4.md`](SCTG_V4.4.md) | Dokumen standar resmi, satu-satunya sumber kebenaran untuk membangun course |
| [`skill/sctg/`](skill/sctg/) | Skill SCTG: `SKILL.md` (baca dulu) dan `references/` (salinan per bagian dari V4.4, tanpa perubahan kalimat) |
| `README.md` | Panduan singkat ini |

## Cara pakai

1. **Pakai skill lebih dulu:** muat `skill/sctg/SKILL.md`, lalu baca hanya berkas di `skill/sctg/references/` yang sesuai pekerjaan. **`SCTG_V4.4.md` utuh dibaca hanya bila diminta, atau saat dibutuhkan:** membangun course penuh dari nol, atau ada pasal yang bertentangan atau meragukan. Bila skill dan dokumen utuh berbeda, dokumen utuh yang berlaku.
2. Sebutkan kode course, series, TP, perangkat sasaran, dan durasi.
3. AI pembangun menjalankan Uji Kelayakan TP dan menawarkan pilihan pedagogis lebih dulu.
4. **Aturan Emas:** kode baru ditulis hanya setelah ada perintah eksplisit, misalnya "Gas kode", "Bangun Kode", atau "Update Kode".
5. Hasil akhir berupa satu berkas HTML siap unggah ke Netlify.

## Yang baru di V.4.4

- **Footer Baku** di setiap course: `[judul course] ©[tahun pembuatan] | totogutomo.com`. Tahun adalah tahun pembuatan course dan tidak berubah saat update.
- **Tombol ⓘ Tentang** tepat di bawah footer Cover dan tombol kedua di **Panel Guru** (🔐). Keduanya membuka **satu modal overlay** yang sama, bukan menampilkan identitas secara langsung atau berpindah halaman.
- Modal memuat judul course, kode seri, deskripsi singkat, teknologi yang benar-benar digunakan, lisensi dan atribusi aktual, pengembang **Toto Gutomo, S.Pd., Gr., M.Pd. — Guru SMA Negeri 3 Maliku**, tagline **< ❤️ / > Ngoding pakai Vibe, Ngajar pakai Hati**, serta tombol aktif **https://totogutomo.com**.
- Modal dapat ditutup dengan X, Kembali Android, atau Escape; progres belajar tidak berubah. Tombol Tentang tidak muncul di langkah game agar tetap satu layar.
- Aturan lengkap ada di pasal **B26**, dengan penyesuaian di A1, A5, Bagian 4, Bagian 6, daftar QA, dan Glosarium.

Course lama tidak diubah otomatis; pasal baru berlaku untuk produksi berikutnya dan update yang diminta.

## Ringkasan fondasi

- **10 Langkah Belajar** dengan Menu Langkah ☰ dan tombol "Lanjut ke [langkah berikutnya] →".
- **Tampilan auto-fit:** Mode Genggam (HP) dan Mode Panggung (laptop/IFP), game satu layar dalam satu kolom tiga pita.
- **Gerbang Baca** dan **Ruang Baca** dengan hitung mundur berbasis jumlah kata, serta **Kunci Senyap**.
- Game dengan **sentuh langsung**, **Jeda Paham**, dan **Level Kecepatan**.
- **Sinematik Pra-Aktivitas**, **Final Boss** (Bandel atau Tuntas), dan **Sertifikat** PDF dengan kode verifikasi.
- **Header Baku** seragam di semua series.

## Riwayat versi

V.2 (TKA) → V.3 → V.3.1 → V.3.2 → V.4 → V.4.1 → V.4.2 → V.4.2.1 → V.4.3 → **V.4.4**

Situs: [totogutomo.com](https://totogutomo.com)

---

SCTG V.4.4 © Toto Gutomo, Guru SMA Negeri 3 Maliku

## Khusus ChatGPT — bukan untuk Claude

Folder [`CHATGPT_ONLY/`](CHATGPT_ONLY/) berisi **SCTG Course Factory V1.4** (engine, benchmark, QA, dan arsip penuh) yang **HANYA DIGUNAKAN OLEH CHATGPT**. Folder ini **bukan bagian standar umum SCTG dan tidak perlu dibaca Claude**. Pengguna Claude cukup membaca dokumen standar resmi [`SCTG_V4.4.md`](SCTG_V4.4.md). Factory menyertakan arsip V4.3 untuk reproduksi historis; **jika ada perbedaan, standar resmi V4.4 di root tetap berlaku**.
