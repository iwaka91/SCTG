# Protokol QA Teknis — SCTG V4.3 + Visual Gate V1.1

## Gerbang teknis rinci

**Catatan V1.1:** G0–G6 berikut adalah subpemeriksaan, bukan bobot penilaian. Keputusan akhir memakai lima gate Ya/Tidak (`docs/RUBRIK_VISUAL_GAME.md`), semuanya wajib Ya dengan bukti; nilai subjektif berasal dari Toto Gutomo.

**G0 — Pedagogi**: CP/AKM relevan; 1–3 TP, kombinasi realistis 1 JP; setiap TP punya mengajar, melatih dengan feedback, dan instrumen menguji; sinematik penawaran disetujui. Keputusan TP HOTS C6 hanya melalui kinerja/produk.

**G1 — Teknis**: HTML tunggal offline, tidak ada CDN; tidak ada error JS; localStorage + explicit resume; reset/ulang terpisah; benar/salah + Fasil/EZ; PDF valid; antarmuka keyboard HP tidak rusak; tanpa horizontal overflow.

**G2 — Layout**: Genggam 100% lebar; game Genggam dan Panggung muat satu layar (tiga pita); Ruang Baca Panggung tanpa scroll halaman; menu/header A5 lengkap; minimal ukuran sentuh sesuai SCTG.

**G3 — Mekanik**: game Canvas *playable* dengan cara sentuh langsung dan mouse/keyboard, state berpengaruh pada permainan, kondisi akhir jelas; jika berbasis refleks wajib Jeda Paham, pilihan kecepatan; keterangan jawaban benar/salah bukan kosmetik.

**G4 — Sinematik**: narasi 4–6 beat, durasi baca sesuai rumus, pseudo-3D dan komposisi visual kontekstual, suara, kejutan berbeda per course, CTA tertahan, replay, Fasil/EZ boleh skip. Sinematik bukan slideshow teks biasa.

**G5 — Visual**: 4–6 sampel layar: cover, game Panggung 1280×650, Ruang Baca Panggung, Final Boss, game/produk Genggam tema gelap, sinematik. Bandingkan standar *rasa* dengan NUM09 Claude: kedalaman, kualitas bentuk objek, grid, hierarki, warna dan animasi. Jangan menyalin tema NUM09 ke course gambut. Tinjau contoh nyata, catat kekurangan dan lakukan perbaikan sebelum lolos.

**G6 — Serah**: `qa-result.json` full matrix tanpa FAIL/BLOCKED; hash HTML identik; `QA_REPORT.md`, sampel screenshot, catatan perubahan. Rating pengguna **tidak** diproduksi oleh QA otomatis. Sertakan `visual-review.json` lima gate Ya/Tidak tanpa persentase. Pengujian Android/IFP asli dilaporkan terpisah, belum dilakukan jika tidak tersedia.

## Matriks layar baku

Genggam: **360×560, 390×700, 430×780, 600×900, 768×1024**.
Panggung: **1024×768, 1366×768, 1920×1080, 1280×650**.
Batas: **899×700 (Genggam), 900×499 (Genggam), 900×500 (Panggung)**.
HP mendatar: **800×360 (ajakan putar saat game)**.

## Seandainya salah satu gagal

- Input kehilangan fokus/isi saat keyboard muncul → **STOP**.
- `scrollWidth > innerWidth + 1` untuk halaman aktif → **STOP**.
- `scrollHeight > innerHeight + 1` untuk langkah game atau Ruang Baca Panggung → **STOP**.
- Canvas tidak terlukis / tidak ada reaksi input / permainan mustahil selesai → **STOP**.
- Timer habis mengeluarkan bunyi, auto-scroll, atau fokus meloncat → **STOP**.
- Kunci baca aktif saat tab hidden, atau reset timer saat panel ditutup → **STOP**.
- Final Boss tanpa bank 12+4/sesi 8+2, damage PGK salah, atau tanpa loop → **STOP**.
- Placeholder, tombol mati, sertifikat PDF rusak, akses Fasil/EZ bocor → **STOP**.

Penguji otomatis hanya bisa membuktikan perilaku yang terprogram dalam profil QA. **Profil tidak lengkap = BLOCKED**, bukan PASS.

## Aturan disiplin bukti

Setiap ``approved`` di profil manual memerlukan deskripsi atau lokasi screenshot/log yang sungguh ada. Jangan menghasilkan laporan kosmetik atau nilai 9,9 secara otomatis.
